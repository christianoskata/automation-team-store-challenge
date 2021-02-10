<template>
  <div class="container col-12 w-100">
    <p>Ver os detalhes e atualizar um registro!</p>
    <br/>
    <div class="d-flex flex-row justify-content-between">
      <div class="col-2 d-flex flex-column align-items-end">
        <label>Marca <input type="text" v-model="shoe.brand"></label>
        <label>Nome <input type="text" v-model="shoe.name"></label>
        <label>Cor <input type="text" v-model="shoe.color"></label>
      </div>
      <div class="col-2 d-flex flex-column align-items-end">
        <label>Ref <input type="text" v-model="shoe.ref"></label>
        <label>Material <input type="text" v-model="shoe.material"></label>
        <label>Tamanho <input type="number" v-model="shoe.size"></label>
      </div>
      <div class="col-2 d-flex flex-column align-items-end">
        <label>Peso <input type="number" v-model="shoe.weight"></label>
        <label>Quantidade <input type="number" v-model="shoe.quantity"></label>
        <label>Lucro %<input type="number" v-model="shoe.tax"></label>
      </div>
      <div class="col-2 col-offset-2 d-flex flex-column align-items-end">
        <label>Preço de Custo <input type="number" v-model="shoe.net_price"></label>
        <label>Detalhes <input type="text" v-model="shoe.description"></label>
      </div>
    </div>
    <div>
      <input
        class="btn btn-primary"
        type="submit"
        value="Atualizar"
        @click="updateShoe(shoe)"
        :disabled="!shoe.name || !shoe.brand || !shoe.ref || !shoe.material || !shoe.color || !shoe.size ||
        !shoe.quantity || !shoe.net_price || !shoe.tax">
    </div>
    <b-modal id="modalList" size="md"  title="Update" v-model="shoes.show">
      <template #shoe> Atualizar </template>
      <div class="d-block text-center">
        <h3>Calçado atualizado com sucesso!</h3>
      </div>
      <div slot="modal-footer" class="">
        <b-button class="mt-3" variant="primary" @click="shoes.show=false" value="Fechar">Fechar</b-button>
      </div>
    </b-modal>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'shoeDetail',
  data() {
    return {
      name: '',
      brand: '',
      ref: '',
      material: '',
      color: '',
      size: '',
      quantity: '',
      net_price: '',
      tax: '',
      description: '',
      weight: '',
    }
  },
  computed: mapState({
    shoe: state => state.shoes.shoe,
    shoes: state => state.shoes
  }),
  methods: mapActions('shoes', [
    'detailShoe',
    'updateShoe'
  ]),
}
</script>

<style scoped>

</style>