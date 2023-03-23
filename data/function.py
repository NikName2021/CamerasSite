import os
from time import strftime, gmtime
import cv2
from bs4 import BeautifulSoup
import requests
from ultralytics import YOLO

from data.all_models import BreakCamers, Anomal
from data.db_session import create_session

from setting import *


SAVE = 'static/working/bad_640'


def parser(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml")
        allNews = soup.find('source')
        street = soup.find('title').text
        return allNews['src'], street
    except Exception as ex:
        print('Произошла ошибка')
        print(ex)


def image_bot(url, id_camera):
    try:
        capture = cv2.VideoCapture(f'https://camera.lipetsk.ru{url}')
        ret, frame = capture.read()
        name = f'frame_{strftime("%Y_%m_%d_%H_%M_%S", gmtime())}_{id_camera}.jpg'
        frame_stretch = cv2.resize(frame, RESIZE)
        # cv2.imwrite(os.path.join(SAVE, name), img_stretch)
        return name, frame, frame_stretch
    except Exception as ex:
        print(ex)


def prediction(name):
    model = YOLO(MODEL)
    results = model.predict(name[1], save=False, save_txt=False)
    for r in results:
        result = [(round(float(x[0]), 2), model.names[int(x[1])]) for x in zip(r.boxes.conf, r.boxes.cls)]
    if result:
        cv2.imwrite(os.path.join('./static/working/bad_640', name[0]), results[0].plot())
    return result


def analytics(text_id, db):
    id_camera = text_id
    text_id = f'{DOMEN_WITH_ELSE}{text_id}'
    url_camera = parser(text_id)

    if not url_camera:
        return

    image = image_bot(url_camera[0], id_camera)
    if not image:
        return

    anomalies = prediction(image)
    if anomalies:
        res = db.query(BreakCamers).where(BreakCamers.id_camera == id_camera).all()
        if not res:
            u = BreakCamers(id_camera=id_camera, street=url_camera[1], image=image[0])
            db.add(u)
            db.flush()
            for anomaly in anomalies:
                al = Anomal(breakdown=anomaly[1], chance=anomaly[0], break_camera_id=u.id)
                db.add(al)
            db.commit()


def parser_site(start, end, db_session):
    for camera in range(start, end + 1):
        analytics(str(camera), db_session)


if __name__ == '__main__':
    db_session = create_session()
    for i in range(1, 7):
        analytics(str(i), db_session)
    db_session.close()
