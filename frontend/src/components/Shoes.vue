<template>
  <div class="container col-12 w-100">
    <p>Cadastrar um novo calçado</p>
    <br/>
    <div class="d-flex flex-row justify-content-between">
      <div class="col-2 d-flex flex-column align-items-end">
        <label>Marca <input type="text" v-model="brand"></label>
        <label>Nome <input type="text" v-model="name"></label>
        <label>Cor <input type="text" v-model="color"></label>
      </div>
      <div class="col-2 d-flex flex-column align-items-end">
        <label>Ref <input type="text" v-model="ref"></label>
        <label>Material <input type="text" v-model="material"></label>
        <label>Tamanho <input type="number" v-model="size"></label>
      </div>
      <div class="col-2 d-flex flex-column align-items-end">
        <label>Peso <input type="number" v-model="weight"></label>
        <label>Quantidade <input type="number" v-model="quantity"></label>
        <label>Lucro %<input type="number" v-model="tax"></label>
      </div>
      <div class="col-2 col-offset-2 d-flex flex-column align-items-end">
        <label>Preço de Custo <input type="number" v-model="net_price"></label>
        <label>Detalhes <input type="text" v-model="description"></label>
      </div>
    </div>
    <div>
      <input
        class="btn btn-primary"
        type="submit"
        value="Add"
        @click="addShoe(
        { brand: brand, name: name, color: color, ref: ref, material: material, size: size,
               weight: weight, quantity: quantity, tax: tax, net_price: net_price, description: description
           })"
        :disabled="!name || !brand || !ref || !material || !color || !size || !quantity || !net_price || !tax">
      <hr/>
    </div>

    <p class="alert-danger" v-if="shoes.length === 0">Nenhum calçado cadastrado</p>
    <table class="table" v-if="shoes.length != 0">
      <thead class="thead-dark">
        <tr>
          <th scope="col">Item</th>
          <th scope="col">Marca</th>
          <th scope="col">Nome</th>
          <th scope="col">Cor</th>
          <th scope="col">Ref</th>
          <th scope="col">Material</th>
          <th scope="col">Tamanho</th>
          <th scope="col">Peso</th>
          <th scope="col">Quantidade</th>
          <th scope="col">Lucro %</th>
          <th scope="col">Preço de Custo</th>
          <th scope="col">Preço Venda</th>
          <th scope="col">Detalhes</th>
          <th scope="col">Deletar</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(shoe, index) in shoes" :key="index">
          <td> [{{index+1}}] </td>
          <td> {{ shoe.brand }} </td>
          <td> {{ shoe.name }} </td>
          <td> {{ shoe.color }} </td>
          <td> {{ shoe.ref }} </td>
          <td> {{ shoe.material }} </td>
          <td> {{ shoe.size }} </td>
          <td> {{ shoe.weight }} </td>
          <td> {{ shoe.quantity }} </td>
          <td> {{ shoe.tax }} </td>
          <td> {{ shoe.net_price }} </td>
          <td> {{ shoe.gross_price }} </td>
          <td> <input class="btn btn-primary" type="submit" value="Detalhes" /> </td>
          <td> <input class="btn btn-danger" type="submit" @click="deleteShoe(shoe.id)" value="Deletar" /> </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: "shoes",
  data() {
    return {
      name: "",
      brand: "",
      ref: "",
      material: "",
      color: "",
      size: "",
      quantity: "",
      net_price: "",
      tax: "",
      description: "",
      weight: "",
    };
  },
  computed: mapState({
    shoes: state => state.shoes.shoes
  }),
  methods: mapActions('shoes', [
    'getShoes',
    'addShoe',
    'deleteShoe'
  ]),
  created() {
    this.$store.dispatch('shoes/getShoes')
  },
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
  img {
    width: 250px;
    padding-top: 50px;
    padding-bottom: 50px;
  }
</style>
