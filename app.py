import os
from data.all_models import BreakCamers, Anomal
from data.db_session import create_session
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from data.function import parser_site

app = Flask(__name__)
CORS(app)
api = Api(app)
db = create_session()
parser = reqparse.RequestParser()


def network_resource():
    res = db.query(BreakCamers).all()
    resource = [i.serialize() for i in res]
    return jsonify(resource)


class Network(Resource):
    def get(self):
        return network_resource()

    def delete(self, network_id):
        res = db.query(BreakCamers).get(network_id)
        try:
            for am in res.anomal:
                db.delete(am)
            os.remove(f'static/working/bad_640/{res.image}')
            db.delete(res)
            db.commit()
        except Exception as ex:
            print(ex)

        return network_resource()


class DeleteAll(Resource):
    def get(self):
        folder = 'static/working/bad_640'
        db.query(Anomal).delete()
        db.query(BreakCamers).delete()
        try:
            db.commit()
            files = os.listdir(f'{folder}')
            for file in files:
                os.remove(f'{folder}/{file}')
        except Exception as ex:
            db.rollback()
            print(ex)

        return network_resource()


class ParserNetwork(Resource):
    def get(self, start, end):
        print(start, end)
        parser_site(int(start), int(end), db)
        return network_resource()


api.add_resource(Network, '/api/network/<network_id>', '/api/network/')
api.add_resource(DeleteAll, '/api/delete_all')
api.add_resource(ParserNetwork, '/api/parser/<start>/<end>')

api.init_app(app)

if __name__ == '__main__':
    app.run()
    # flask run - -host = 0.0.0.0 - -port = 80
