<template>
  <div class="profile-page-wrapper">
    <h1>Мой профиль</h1>

    <div class="profile-content card" v-if="user">

      <div class="left-column">
        <span>Имя пользователя: {{user.username}}</span>
        <span>Дата регистрации: {{getDateJoined}}</span>
        <span>Роль: {{user.role}}</span>
      </div>

      <div class="right-column">
        <a-form
            :form="form"
            @submit="handleSubmit"
        >
          <a-form-item label="Имя:">
            <a-input
                v-decorator="firstName"
                placeholder="Имя"
            />
          </a-form-item>
          <a-form-item label="Фамилия:">
            <a-input
                v-decorator="lastName"
                placeholder="Фамилия"
            />
          </a-form-item>
          <a-form-item label="Почта:">
            <a-input
                v-decorator="email"
                placeholder="Почта"
            />
          </a-form-item>
          <a-form-item label="Номер телефона:">
            <a-input
                v-decorator="phone"
                placeholder="Номер телефона"
            />
          </a-form-item>
          <a-form-item label="Адрес проживания:">
            <a-input
                v-decorator="address"
                placeholder="Адрес проживания"
            />
          </a-form-item>
          <a-form-item>
            <a-button type="primary" html-type="submit">
              Обновить информацию
            </a-button>
          </a-form-item>
        </a-form>
      </div>

      <div class="footer">
        <div class="logout-block">
          <p class="text">
            Выйти с аккаунта
          </p>
          <a-button
              type="primary"
              @click="logout()"
          >
            Выход
          </a-button>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import moment from 'moment';
import { mapGetters } from 'vuex';

import { LOGOUT_USER, UPDATE_USER } from '@/store/actions.type';

export default {
  name: 'TheProfilePage',
  computed: {
    ...mapGetters([
      'user',
    ]),
    getDateJoined() {
      return moment(this.user.dateJoined).format('DD.MM.YYYY');
    },
  },
  data() {
    return {
      form: null,
      firstName: ['firstName', {
        rules: [{
          required: true,
          message: 'firstName',
        }],
      }],
      lastName: ['lastName', {
        rules: [{
          required: true,
          message: 'lastName',
        }],
      }],
      email: ['email', {
        rules: [{
          required: true,
          message: 'email',
        }],
      }],
      phone: ['phone', {
        rules: [{
          required: true,
          message: 'phone',
        }],
      }],
      address: ['address', {
        rules: [{
          required: true,
          message: 'address',
        }],
      }],
    };
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFieldsAndScroll((errors, fields) => {
        if (!errors) {
          this.$store.dispatch(UPDATE_USER, fields);
        }
      });
    },
    setFormFields() {
      this.form.getFieldDecorator(
        'firstName', { initialValue: this.user?.firstName },
      );
      this.form.getFieldDecorator(
        'lastName', { initialValue: this.user?.lastName },
      );
      this.form.getFieldDecorator(
        'email', { initialValue: this.user?.email },
      );
      this.form.getFieldDecorator(
        'phone', { initialValue: this.user?.phone },
      );
      this.form.getFieldDecorator(
        'address', { initialValue: this.user?.address },
      );
    },
    logout() {
      this.$store.dispatch(LOGOUT_USER);
    },
  },
  mounted() {
    this.form = this.$form.createForm(this);
    if (this.user) {
      this.setFormFields();
    }
  },
  watch: {
    user() {
      if (this.form) {
        this.setFormFields();
      }
    },
  },
};
</script>

<style lang="scss">
  .profile-content {
    display: flex;
    flex-wrap: wrap;
    width: 50rem;
    padding: 2rem;

    .left-column {
      display: flex;
      flex-direction: column;
      flex: 1;

      span {
        margin-bottom: 1rem;
      }
    }

    .right-column {
      display: flex;
      flex: 1;
    }

    .footer {
      display: flex;
      justify-content: space-between;
      flex: 1 100%;
      margin-top: 2rem;
    }
  }

  .ant-form-item {
    width: 18.75rem !important;
    height: 3.125rem !important;
  }

  .ant-form-item-label {
    line-height: 1.5 !important;
  }

  .ant-form-item-control {
    line-height: 1.5 !important;
  }

  .ant-input {
    width: 18.75rem !important;
  }
</style>
