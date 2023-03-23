<template>
  <header-main></header-main>
  <main>
<!--    <Preloader></Preloader>-->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Удалить все записи?</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
          </div>
          <div class="modal-body">
            Вы уверены, что хотите удалить все записи?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
            <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="delete_all">Да</button>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" id="parserModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Проверка камер</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
          </div>
          <div class="modal-body">
            <div class="mb-3">
              <label for="recipient-name" class="col-form-label">Начальный id</label>
<!--              <i class="alert start alert-md alert-danger"></i>-->
              <input type="number" class="form-control" v-model="start">
            </div>
            <div class="mb-3">
              <label for="message-text" class="col-form-label">Конечный id</label>
<!--              <i class="alert end alert-md alert-danger"></i>-->
              <input type="number" class="form-control" v-model="end">
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
            <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="parser">Начать проверку</button>
          </div>
        </div>
      </div>
    </div>

    <div class="btn-group" style="width: 40%;">
      <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#exampleModal">
        Удалить все
      </button>
      <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#parserModal">
        Парсить
      </button>
    </div>


    <ul class="cards">
      <li class="cards__item" v-for="artist in artists" :key="artist">
        <div class="modal fade" :id="'exampleModal' + artist.id" tabindex="-1" aria-labelledby="exampleModalLabel"
             aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Удалить данную запись?</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal"
                        aria-label="Закрыть"></button>
              </div>
              <div class="modal-body">
                Вы уверены, что хотите удалить данную запись?
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
                <button type="submit" class="btn btn-red" @click="delete_one(artist.id)" data-bs-dismiss="modal">Да
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="card">
          <a :href="artist.image"
             data-fancybox="gallery"
             :data-caption="artist.street">
            <div class="card__image"
                 :style="{ backgroundImage: 'url(' + artist.image + ')' }"></div>
          </a>

          <div class="card__content">
            <div class="card__title">{{ artist.breakdown }} ({{ artist.chance }})"</div>
            <p class="card__text">
              {{ artist.street }}
              <br>
              <br>
              {{ artist.timestamp }}
            </p>
            <a :href="'https://camera.lipetsk.ru/index.php?r=camera/video&id=' + artist.id_camera"
               style="text-decoration: none">
              <button class="btn btn--block card__btn">Перейти</button>
            </a>
            <button type="button" class="btn btn--block card__btn" data-bs-toggle="modal"
                    :data-bs-target="'#exampleModal' + artist.id">
              Удалить
            </button>
          </div>
        </div>
      </li>

    </ul>
  </main>
</template>


<script>
import HeaderMain from "@/components/Header";
import axios from 'axios';
import $ from 'jquery'

export default {
  name: 'App',
  components: {
    HeaderMain
  },
  el: '#app',
  mounted() {
    this.getArtists()
  },
  data() {
    return {
      artists: [],
      start: 0,
      end: 0

    }
  },
  methods: {
    getArtists() {
      axios.get(process.env.VUE_APP_SRC + '/api/network')
          .then(res => {
            this.artists = res.data
            console.log(res.data)

          })
          .catch(e => {
            console.log(e)
          })

    },
    delete_all() {
      axios.get(process.env.VUE_APP_SRC + '/api/delete_all')
          .then(res => {
            this.artists = res.data
            console.log(res.data)

          })
          .catch(e => {
            console.log(e)
          })
    },

    delete_one(network_id) {
      axios.delete(process.env.VUE_APP_SRC + '/api/network/' + network_id)
          .then(res => {
            this.artists = res.data
            console.log(res.data)

          })
          .catch(e => {
            console.log(e)
          })
    },

    checkForm: function () {

      if (!this.start) {
        $(".start").text('Введите число');
      }
      if (!this.end) {
        $(".end").text('Введите число');
      }
      else {
        return true;
      }
      return false;

    },
    parser() {

      axios.get(process.env.VUE_APP_SRC + '/api/parser/' + this.start + '/' + this.end)
          .then(res => {
            this.artists = res.data
            console.log(res.data)

          })
          .catch(e => {
            console.log(e)
          })

      // if (this.checkForm())
      // {
      //   console.log(45678)
      // }

    }


  }
}
</script>

<style>
@import './assets/css/cards.css';
</style>
