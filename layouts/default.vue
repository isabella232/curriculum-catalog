<template>
  <v-app>
    <v-toolbar app>
      <!-- <img height=50 src="/curriculum-catalog/quansight_logo.png" /> -->
      <v-toolbar-title v-text="title"></v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-content>
      <v-container fluid>
        <nuxt />
      </v-container>
    </v-content>
    <v-footer app></v-footer>
  </v-app>
</template>

<script>
  export default {
    data () {
      return {
        title: 'Quansight Course Catalog'
      }
    }
  }
</script>
