<template>
  <div class="products-page-wrapper">
    <h1>Продукты для переработки</h1>

    <a-button
        type="primary"
        @click="toggleModal"
        style="margin-bottom: 1rem"
        v-if="isAvailable"
    >
      Управление продуктами
    </a-button>

    <the-products-management-modal
        :visible="visible"
        :toggle="toggleModal"
    />

    <div class="products-content">
      <a-tabs
          v-if="categories"
          default-active-key="0"
          tab-position="left"
      >
        <a-tab-pane key="0" tab="Все">
          <the-products-wrapper
              :category="0"
              description="Список всех продуктов для переработки"
              :products="products"
              :danger-levels="dangerLevels"
          />
        </a-tab-pane>
        <a-tab-pane
            v-for="item in categories"
            :key="item.id"
            :tab="item.name"
        >
          <the-products-wrapper
              :category="item.id"
              :description="item.description"
              :products="products"
              :danger-levels="dangerLevels"
          />
        </a-tab-pane>
      </a-tabs>
    </div>

  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import TheProductsManagementModal from '@/components/TheProductsManagementModal';
import TheProductsWrapper from '@/components/TheProductsWrapper';
import {GET_CATEGORIES, GET_DANGER_LEVELS, GET_PRODUCTS} from '@/store/actions.type';
import RolesType from '@/types/roles.type';

export default {
  name: 'TheProductsPage',
  components: {
    TheProductsWrapper,
    TheProductsManagementModal,
  },
  computed: {
    ...mapGetters([
      'user',
      'categories',
      'products',
      'dangerLevels',
    ]),
    isAvailable() {
      return this.user && (this.user.role === RolesType.MANAGER || this.user.role === RolesType.ADMIN);
    },
  },
  data() {
    return {
      visible: false,
    };
  },
  methods: {
    toggleModal() {
      this.visible = !this.visible;
    },
  },
  mounted() {
    this.$store.dispatch(GET_CATEGORIES);
    this.$store.dispatch(GET_DANGER_LEVELS);
    this.$store.dispatch(GET_PRODUCTS);
  },
};
</script>

<style scoped lang="scss">

</style>
