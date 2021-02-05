<template>
  <div id="app">
    <h1>Dafiti Challenge - Shoes</h1>
    <div id="nav">
      <router-link :to="{ name: 'shoes' }">Shoes List</router-link> |
      <router-link :to="{ name: 'csv' }">CSV</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

<script>
export default {
  name: 'App'
}
</script>