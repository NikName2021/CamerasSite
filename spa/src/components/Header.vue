<template>
  <header class="header">

    <div class="text-box">
      <h1 class="heading-primary">
        <span class="heading-primary-main">Безопасный город</span>
        <span class="heading-primary-sub">Поиск неисправностей на видеокамерах</span>
      </h1>
      <!--<a href="#" class="btn btn-white btn-animated">Discover our tours</a>-->
    </div>
  </header>
</template>

<script>
export default {
  name: 'HeaderMain',
  props: {
    msg: String
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header {
  height: 100vh;
  background-image: linear-gradient(to right bottom,
  rgba(250, 243, 211, 0.8),
  rgba(174, 154, 118, 0.8)),
  url('https://farm5.staticflickr.com/4760/24988691837_dfa7e4d69b_b.jpg');

  background-size: cover;
  background-position: top;
  position: relative;

  clip-path: polygon(0 0, 100% 0, 100% 75vh, 0 100%);
}

.brand-box {
  position: absolute;
  top: 40px;
  left: 40px;
}

.brand {
  font-size: 20px;
}

.text-box {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}

.heading-primary {
  color: #fff;
  text-transform: uppercase;

  backface-visibility: hidden;
  margin-bottom: 30px;
}

.heading-primary-main {
  display: block;
  font-size: 26px;
  font-weight: 400;
  letter-spacing: 5px;
}

.heading-primary-sub {
  display: block;
  font-size: 18px;
  font-weight: 700;
  letter-spacing: 7.4px;
}

.btn:link,
.btn:visited {
  text-transform: uppercase;
  text-decoration: none;
  padding: 10px 20px;
  display: inline-block;
  border-radius: 100px;
  transition: all .2s;
  position: relative;
}

.btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.btn:active {
  transform: translateY(-1px);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}

.btn-white {
  background-color: #fff;
  color: #777;
  font-size: 14px;
}
</style>
