<template>
  <div class="basket-page-wrapper">
    <h1>Корзина</h1>

    <div class="basket-content">
      <div class="header">

        <a-statistic
          title="Общая сумма заказа"
          :value="basketSum"
          :precision="2"
          prefix="$"
          style="margin-right: 50px"
        />

        <a-textarea v-model="note" placeholder="Комментарий к заказу" :rows="1" />

        <a-button
            type="primary"
            :disabled="!basket.length"
            @click="confirmOrder"
        >
          Подтвердить заказ
        </a-button>

      </div>

      <div class="basket-card">
        <a-card
            v-for="(item, index) in basket"
            :key="index"
            :title="item.name"
            size="small"
            style="max-width: 300px"
        >
          <img
              slot="cover"
              :alt="item.name"
              :src="item.picture ? item.picture : imageNotFound"
          />

          <span>Цена: ${{item.price}}</span>
          <span>Опасность:
            <a-tag :color="getLevelColorById(item.danger_level)">{{getLevelById(item.danger_level)}}</a-tag>
          </span>

        </a-card>
      </div>

    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import { CONFIRM_ORDER } from '@/store/actions.type';

export default {
  name: 'TheBasketPage',
  computed: {
    ...mapGetters([
      'basket',
      'basketSum',
      'dangerLevels',
    ]),
  },
  data() {
    return {
      imageNotFound: '/image-not-found.png',
      note: '',
    };
  },
  methods: {
    getLevelById(id) {
      return this.dangerLevels.find((level) => level.id === id).name;
    },
    getLevelColorById(id) {
      const level = this.dangerLevels.find((level) => level.id === id);
      return (level && level.color) ? level.color : '';
    },
    confirmOrder() {
      this.$store.dispatch(CONFIRM_ORDER, { note: this.note, basket: this.basket });
    },
  },
};
</script>

<style lang="scss">
  .basket-page-wrapper {
    width: 100%;

    .basket-content {
      max-width: 80rem;

      .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;

        button {
          margin-right: 2.275rem;
        }
      }

      .basket-card {
        display: flex;
        flex-wrap: wrap;

        .ant-card {
          flex-grow: 1;
          margin: 0 1rem 1rem 0;
          max-width: 12.125rem !important;

          &-body {
            display: flex;
            flex-direction: column;
          }
        }

        img {
          width: 12rem;
          height: 12rem;
        }
      }
    }
  }
</style>
