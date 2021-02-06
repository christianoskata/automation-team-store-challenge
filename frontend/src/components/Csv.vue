<template>
<div class="container col-12 w-100">
  <p>Enviar um CSV</p>
  <br/>
  <div>
    <label>Selecione um arquivo CSV:
      <input type="file"  id="file" ref="file" v-on:change="handleFileUpload"/>
    </label>
    <div>
      <input
        class="btn btn-primary"
        type="submit"
        value="Enviar"
        v-on:click="sendCsv(csv.file)"
        :disabled="!csv.file">
    </div>
  </div>
  <b-modal id="modalCsv" size="md"  title="Csv" v-model="csv.show">
    <template #csv> Csv </template>
    <div class="d-block text-center">
      <h3>Csv enviado com sucesso!</h3>
    </div>
    <div slot="modal-footer" class="">
      <b-button class="mt-3" variant="primary" @click="csv.show=false" value="Fechar">Fechar</b-button>
    </div>
  </b-modal>
</div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'csv',
  data() {
    return {
      file: '',
    };
  },
  computed: mapState({
    csv: state => state.csv,
  }),
  methods: mapActions('csv', [
    'sendCsv',
    'handleFileUpload'
  ]),
};
</script>

<style scoped>

</style>