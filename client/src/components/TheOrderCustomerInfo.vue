<template>
  <div class="customer-wrapper">
    <span>Полное имя: {{customer.firstName}} {{customer.lastName}}</span>
    <span>Имя пользователя: {{customer.username}}</span>
    <span>Номер телефона: {{customer.phone}}</span>
    <span>Почта: {{customer.email}}</span>
    <span>Адрес проживания: {{customer.address}}</span>
    <span>Дата регистрации: {{getDateJoined}}</span>
    <br>
    <span>Примечание к заказу: {{note}}</span>
    <span>Дата создания заказа: {{getCreatedDate}}</span>
  </div>
</template>

<script>
import moment from 'moment';

export default {
  name: 'TheOrderCustomerInfo',
  props: {
    customer: Object,
    note: String,
    createdAt: String,
  },
  computed: {
    getDateJoined() {
      return moment(this.customer.dateJoined).format('DD.MM.YYYY');
    },
    getCreatedDate() {
      return moment(this.createdAt).format('dddd, MMMM Do YYYY, h:mm:ss a');
    },
  },
};
</script>

<style lang="scss">

</style>
