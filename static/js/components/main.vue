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
  <main>
    <ul class="cards">
      <li class="cards__item" v-for="index in 10" :key="index">
        <div class="card">
          <a href="/static/img/10 (1).jpg"
             data-fancybox="gallery"
             data-caption="Optional caption">
            <div class="card__image"
                 style="background-image: url('/static/img/10 (1).jpg')"></div>
          </a>

          <div class="card__content">
            <div class="card__title">Flex Grow</div>
            <p class="card__text">This defines the ability for a flex item to grow if necessary. It accepts a
              unitless value that serves as a proportion. It dictates what amount of the available space
              inside the flex container the item should take up.</p>
            <button class="btn btn--block card__btn">Button</button>
          </div>
        </div>
      </li>

    </ul>
  </main>
</template>

<script>
export default {
  name: "Main",

};
</script>

<!-- Use preprocessors via the lang attribute! e.g. <style lang="scss"> -->
<style>

</style>