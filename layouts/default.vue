<template>
  <v-app>
    <v-toolbar color="white">
      <img src="https://drive.google.com/uc?id=1aj4GIMiWdkSF1uqjJBw63tGUIGNk4nbQ" style="height:36px" alt="Quansight Logo"/>
      <v-toolbar-title v-text="title"></v-toolbar-title>
    </v-toolbar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  export default {
    data () {
      return {
        title: 'Quansight Course Builder'
      }
    }
  }
</script>
