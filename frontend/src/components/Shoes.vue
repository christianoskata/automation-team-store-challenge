<template>
  <div class="container">
    <h1>Shoes</h1>
    <p align="center">
      <img src="https://i.imgur.com/SA8cjs8.png">
    </p>
    <p>The data below is added/removed from the Database using Django's ORM and Rest Framework.</p>
    <br/>
    <p>Name</p>
    <input type="text" v-model="name">
    <p>Brand</p>
    <input type="text" v-model="brand">
    <br><br>
    <input
      type="submit"
      value="Add"
      @click="addShoe({ name: name, brand: brand })"
      :disabled="!name || !brand">

    <hr/>

    <h3>Shoes List</h3>
    <p v-if="shoes_data.length === 0">No Shoes</p>
    <div class="shoe" v-for="(shoe, index) in shoes_data" :key="index">
        <p class="shoe-index">[{{index}}]</p>
        <p class="shoe-name" v-html="shoe.name"></p>
        <p class="shoe-brand" v-html="shoe.brand"></p>
        <input type="submit" @click="deleteShoe(shoe.pk)" value="Delete" />
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: "Shoes",
  data() {
    return {
      name: "",
      brand: "",
    };
  },
  computed: mapState({
    shoes_data: state => state.shoes.shoes
  }),
  methods: mapActions('shoes', [
    'getShoes',
    'addShoe',
    'deleteShoe'
  ]),
  created() {
    this.$store.dispatch('shoes/getShoes')
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  h1 {
    text-align: center;
  }
  hr {
    max-width: 65%;
  }
  .shoe {
    margin: 0 auto;
    max-width: 30%;
    text-align: left;
    border-bottom: 1px solid #ccc;
    padding: 1rem;
  }
  .shoe-index {
    color: #ccc;
    font-size: 0.8rem;
  }
  img {
    width: 250px;
    padding-top: 50px;
    padding-bottom: 50px;
  }
</style>
