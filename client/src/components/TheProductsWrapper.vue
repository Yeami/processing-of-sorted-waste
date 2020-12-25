<template>
  <div class="products-wrapper" v-if="products">
    <h3>{{description}} - {{getProducts.length}} (шт.)</h3>

    <div class="product-card">
      <a-card
          v-for="item in getProducts"
          :key="item.id"
          :title="item.name"
          style="max-width: 300px"
      >
        <img
          slot="cover"
          :alt="item.name"
          :src="item.picture ? item.picture : imageNotFound"
        />

        <a-popover slot="extra" :title="item.name">
          <template slot="content">
            <span>{{item.description}}</span>
          </template>
          <a href="#">Подробнее</a>
        </a-popover>

        <span>Цена: ${{item.price}} за 1 тонну</span>
        <span>Доступен:
          <span :style="`color: ${item.is_available ? 'green' : 'red'}`"> {{isAvailable(item.is_available)}}</span>
        </span>
        <span>Влияет на окружающую среду:
          <span :style="`color: ${item.is_impact_on_environment ? 'green' : 'red'}`"> {{isAvailable(item.is_impact_on_environment)}}</span>
        </span>
        <span>Уровень опастности:
          <a-tag>{{getLevelById(item.danger_level)}}</a-tag>
        </span>

        <a-button
            type="primary"
            style="margin-top: 0.5rem"
            :disabled="!item.is_available"
            @click="onClick(item)"
        >
          <a-icon type="shopping-cart" /> Добавить в корзину
        </a-button>

      </a-card>
    </div>
  </div>
</template>

<script>
import { UPDATE_BASKET } from '@/store/mutations.type';

export default {
  name: 'TheProductsWrapper',
  props: {
    category: Number,
    description: String,
    products: Array,
    dangerLevels: Array,
  },
  computed: {
    getProducts() {
      if (this.category) {
        return this.products.filter((product) => product.category === this.category);
      }
      return this.products;
    },
  },
  data() {
    return {
      imageNotFound: '/image-not-found.png',
    };
  },
  methods: {
    getLevelById(id) {
      return this.dangerLevels.find((level) => level.id === id).name;
    },
    isAvailable(availability) {
      return availability ? 'Да' : 'Нет';
    },
    onClick(product) {
      this.$store.commit(UPDATE_BASKET, product);
    },
  },
};
</script>

<style lang="scss">
  .products-wrapper {
    width: 100%;

    .product-card {
      display: flex;
      flex-wrap: wrap;
      max-width: 60rem;

      .ant-card {
        flex-grow: 1;
        margin: 0 1rem 1rem 0;

        &-body {
          display: flex;
          flex-direction: column;
        }
      }

      img {
        width: 18.625rem;
        height: 18.625rem;
      }
    }
  }

  .ant-popover {
    width: 20rem;
  }
</style>
