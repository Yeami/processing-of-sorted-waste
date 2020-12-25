<template>
  <a-modal
      :visible="visible"
      title="Управление продуктами"
      @ok="toggle"
      @cancel="toggle"
      width="50rem"
  >
    <div class="modal-content">
      <div class="brand-card card">
        <h3>Уровень опасности</h3>
        <a-input v-model="dangerLevelName" placeholder="Уровень" style="margin-bottom: 0.5rem"/>
        <a-input v-model="dangerLevelColor" placeholder="Цвет" style="margin-bottom: 0.5rem"/>
        <a-button type="primary" @click="createDangerLevel">Добавить уровень опасности</a-button>
      </div>

      <div class="category-card card">
        <h3>Категория</h3>
        <a-input v-model="categoryName" placeholder="Название" style="margin-bottom: 0.5rem"/>
        <a-input v-model="categoryDescription" placeholder="Описание" style="margin-bottom: 1rem"/>
        <a-button type="primary" @click="createCategory">Добавить категорию</a-button>
      </div>

      <div class="product-card card" style="margin-top: 1rem">
        <h3>Продукт переработки</h3>
        <a-form :form="form">
          <a-form-item>
            <a-input
                v-decorator="['name']"
                placeholder="Название"
            />
          </a-form-item>
          <a-form-item>
            <a-input
                v-decorator="['description']"
                placeholder="Описание"
            />
          </a-form-item>
          <a-form-item>
            <a-input
                v-decorator="['price']"
                placeholder="Цена"
            />
          </a-form-item>
          <a-form-item>
            <a-input
                v-decorator="['picture']"
                placeholder="Ссылка на фото"
            />
          </a-form-item>
          <a-form-item>
            <a-checkbox
                v-decorator="['isAvailable']"
                :checked="isAvailable"
                @change="handleChange"
            >
              Доступен
            </a-checkbox>
          </a-form-item>
          <a-form-item>
            <a-checkbox
                v-decorator="['isImpact']"
                :checked="isImpact"
                @change="handleChange2"
            >
              Влияет на окружающею среду
            </a-checkbox>
          </a-form-item>
          <a-form-item v-if="selectedLevel">
            <a-dropdown>
              <a-menu slot="overlay" @click="selectLevel">
                <a-menu-item
                    v-for="item in dangerLevels"
                    :key="item.id"
                >
                  {{item.name}}
                </a-menu-item>
              </a-menu>
              <div class="brand-dropdown">
                Уровни опасности:
                <a-button>
                  {{selectedLevel.name}}
                  <a-icon type="down"/>
                </a-button>
              </div>
            </a-dropdown>
          </a-form-item>
          <a-form-item v-if="selectedCategory">
            <a-dropdown>
              <a-menu slot="overlay" @click="selectCategory">
                <a-menu-item
                    v-for="item in categories"
                    :key="item.id"
                >
                  {{item.name}}
                </a-menu-item>
              </a-menu>
              <div class="brand-dropdown">
                Категории:
                <a-button>
                  {{selectedCategory.name}}
                  <a-icon type="down"/>
                </a-button>
              </div>
            </a-dropdown>
          </a-form-item>
          <a-form-item>
            <a-button type="primary" @click="createProduct">
              Добавить продукт
            </a-button>
          </a-form-item>
        </a-form>
      </div>
    </div>

  </a-modal>
</template>

<script>
import { mapGetters } from 'vuex';

import { CREATE_DANGER_LEVEL, CREATE_CATEGORY, CREATE_PRODUCT } from '@/store/actions.type';

export default {
  name: 'TheProductsManagementModal',
  computed: {
    ...mapGetters([
      'dangerLevels',
      'categories',
    ]),
  },
  props: {
    visible: Boolean,
    toggle: Function,
  },
  data() {
    return {
      dangerLevelName: '',
      dangerLevelColor: '',
      categoryName: '',
      categoryDescription: '',
      isAvailable: false,
      isImpact: false,
      form: this.$form.createForm(this),
      selectedLevel: null,
      selectedCategory: null,
    };
  },
  methods: {
    createDangerLevel() {
      this.$store.dispatch(CREATE_DANGER_LEVEL, {
        name: this.dangerLevelName,
        color: this.dangerLevelColor,
      });
    },
    createCategory() {
      this.$store.dispatch(CREATE_CATEGORY, {
        name: this.categoryName,
        description: this.categoryDescription,
      });
    },
    selectLevel(e) {
      this.selectedLevel = this.dangerLevels.find((l) => l.id === e.key);
    },
    selectCategory(e) {
      this.selectedCategory = this.categories.find((c) => c.id === e.key);
    },
    createProduct() {
      this.form.validateFields((errors, fields) => {
        if (!errors) {
          this.$store.dispatch(CREATE_PRODUCT, {
            ...fields,
            level: this.selectedLevel.id,
            category: this.selectedCategory.id,
          });
        }
      });
    },
    handleChange(e) {
      this.isAvailable = e.target.checked;
    },
    handleChange2(e) {
      this.isImpact = e.target.checked;
    },
  },
  watch: {
    dangerLevels() {
      [this.selectedLevel] = this.dangerLevels;
    },
    categories() {
      [this.selectedCategory] = this.categories;
    },
  },
};
</script>

<style scoped lang="scss">
  .modal-content {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    flex: 2;

    .brand-card,
    .category-card,
    .product-card {
      width: 23rem;
      padding: 1rem;
    }
  }

  .ant-form-item {
    margin: 0;
  }
</style>
