<template>
  <div class="orders-page-wrapper">
    <h1>Заказы</h1>

    <div class="orders-content" v-if="orders">
      <a-card
          v-for="item in orders"
          :key="item.id"
          :title="`Заказ №${item.id}`"
          :tab-list="tabList"
          :active-tab-key="tabKey"
          @tabChange="(key) => onTabChange(key)"
      >
        <div class="customer-info" v-if="tabKey === 'customer'">
          <the-order-customer-info
              :customer="item.customer"
              :note="item.note"
              :created-at="item.created_at"
          />
        </div>

        <div class="products-info" v-if="tabKey === 'products'">
          <b>Общая цена за все продукты: ${{calculateOrderPrice(item.products)}}</b>

          <div
              class="product-item card"
              v-for="product in item.products"
              :key="product.product.id"
          >
            <span>Название: {{product.product.name}}</span>
            <span>Цена: ${{product.product.price}} (за 1 т.)</span>
            <span>Количество: {{product.amount}} (т.)</span>
            <span>Уровень опасности:
              <a-tag :color="getLevelColorById(product.product.danger_level)">
                {{getLevelById(product.product.danger_level)}}
              </a-tag>
            </span>
            <br>
            <span>
              Общая цена за продукт: ${{calculateProductsPrice(product.amount, product.product.price)}}
            </span>
          </div>
        </div>

      </a-card>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import TheOrderCustomerInfo from '@/components/TheOrderCustomerInfo';
import {GET_CUSTOMER_ORDERS, GET_DANGER_LEVELS} from '@/store/actions.type';

export default {
  name: 'TheOrdersPage',
  components: {
    TheOrderCustomerInfo,
  },
  computed: {
    ...mapGetters([
      'orders',
      'dangerLevels',
    ]),
  },
  data() {
    return {
      tabKey: 'customer',
      tabList: [
        {
          key: 'customer',
          tab: 'Заказчик',
        },
        {
          key: 'products',
          tab: 'Продукты',
        },
      ],
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
    onTabChange(key) {
      this.tabKey = key;
    },
    calculateProductsPrice(amount, price) {
      return amount * parseFloat(price);
    },
    calculateOrderPrice(products) {
      let price = 0;
      products.forEach((p) => {
        price += this.calculateProductsPrice(p.amount, p.product.price);
      });

      return price;
    },
  },
  mounted() {
    this.$store.dispatch(GET_DANGER_LEVELS);
    this.$store.dispatch(GET_CUSTOMER_ORDERS);
  },
};
</script>

<style lang="scss">
  .orders-content {
    display: flex;
    flex-wrap: wrap;
    max-width: 60rem;

    .ant-card {
      flex-grow: 1;
      margin: 0 1rem 1rem 0;

      &-body div {
        display: flex;
        flex-direction: column;
      }
    }
  }

  .product-item {
    padding: 0.5rem;
  }
</style>
