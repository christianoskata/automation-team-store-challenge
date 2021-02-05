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
    <p class="alert-success p-1 m-3" v-if="csv.success">Csv enviado com sucesso!</p>
  </div>
</div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'csv',
  data() {
    return {
      file: '',
      success: ''
    };
  },
  computed: mapState({
    csv: state => state.csv
  }),
  methods: mapActions('csv', [
    'sendCsv',
    'handleFileUpload'
  ]),
};
</script>

<style scoped>

</style>