<template>
  <v-layout justify-center>
    <v-flex xs12 sm12 md10>

      <v-autocomplete
        v-model="selected_fields"
        :items="field_options"
        chips
        label="Field of Study"
        item-text="name"
        item-value="name"
        multiple
      >
        <template
          slot="selection"
          slot-scope="data"
        >
          <v-chip
            :selected="data.selected"
            close
            color="primary"
            outline
            class="chip--select-multi"
            @input="remove_field(data.item)"
          >
            <v-avatar>
              <v-icon v-if="data.item.avatar">{{ data.item.avatar }}</v-icon>
              <img v-if="data.item.avatar_url" :src="data.item.avatar_url">
            </v-avatar>
            {{ data.item.name }}
          </v-chip>
        </template>
        <template
          slot="item"
          slot-scope="data"
        >
          <template v-if="typeof data.item !== 'object'">
            <v-list-tile-content v-text="data.item"></v-list-tile-content>
          </template>
          <template v-else>
            <v-list-tile-avatar>
              <v-icon v-if="data.item.avatar">{{ data.item.avatar }}</v-icon>
              <img v-if="data.item.avatar_url" :src="data.item.avatar_url">
            </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title v-html="data.item.name"></v-list-tile-title>
              <v-list-tile-sub-title v-html="data.item.group"></v-list-tile-sub-title>
            </v-list-tile-content>
          </template>
        </template>
      </v-autocomplete>

      <v-autocomplete
        v-model="selected_levels"
        :items="level_options"
        chips
        label="Level"
        item-text="name"
        item-value="name"
        multiple
      >
        <template
          slot="selection"
          slot-scope="data"
        >
          <v-chip
            :selected="data.selected"
            close
            color="primary"
            outline
            class="chip--select-multi"
            @input="remove_level(data.item)"
          >
            <v-avatar>
              <v-icon v-if="data.item.avatar">{{ data.item.avatar }}</v-icon>
              <img v-if="data.item.avatar_url" :src="data.item.avatar_url">
            </v-avatar>
            {{ data.item.name }}
          </v-chip>
        </template>
        <template
          slot="item"
          slot-scope="data"
        >
          <template v-if="typeof data.item !== 'object'">
            <v-list-tile-content v-text="data.item"></v-list-tile-content>
          </template>
          <template v-else>
            <v-list-tile-avatar>
              <v-icon v-if="data.item.avatar">{{ data.item.avatar }}</v-icon>
              <img v-if="data.item.avatar_url" :src="data.item.avatar_url">
            </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title v-html="data.item.name"></v-list-tile-title>
              <v-list-tile-sub-title v-html="data.item.group"></v-list-tile-sub-title>
            </v-list-tile-content>
          </template>
        </template>
      </v-autocomplete>

      <v-autocomplete
        v-model="selected_backgrounds"
        :items="background_options"
        chips
        label="Attendee Background"
        item-text="name"
        item-value="name"
        multiple
      >
        <template
          slot="selection"
          slot-scope="data"
        >
          <v-chip
            :selected="data.selected"
            close
            color="primary"
            outline
            class="chip--select-multi"
            @input="remove_background(data.item)"
          >
            <v-avatar>
              <v-icon v-if="data.item.avatar">{{ data.item.avatar }}</v-icon>
              <img v-if="data.item.avatar_url" :src="data.item.avatar_url">
            </v-avatar>
            {{ data.item.name }}
          </v-chip>
        </template>
        <template
          slot="item"
          slot-scope="data"
        >
          <template v-if="typeof data.item !== 'object'">
            <v-list-tile-content v-text="data.item"></v-list-tile-content>
          </template>
          <template v-else>
            <v-list-tile-avatar>
              <v-icon v-if="data.item.avatar">{{ data.item.avatar }}</v-icon>
              <img v-if="data.item.avatar_url" :src="data.item.avatar_url">
            </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title v-html="data.item.name"></v-list-tile-title>
              <v-list-tile-sub-title v-html="data.item.group"></v-list-tile-sub-title>
            </v-list-tile-content>
          </template>
        </template>
      </v-autocomplete>

      <v-expansion-panel>
        <v-expansion-panel-content
          v-for="(item,i) in 5"
          :key="i"
        >
          <div slot="header">Item</div>
          <v-card dark color="blue" class="darken-4">
            <v-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</v-card-text>
          </v-card>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-flex>
  </v-layout>
</template>

<style>
  .toggle-button-active {
    background-color: red
  }
</style>

<script>
  export default {
    components: {
    },
    data () {
      var d = {

        field_options: [
          { name: 'Python', avatar_url: './Python.svg' },
          { name: 'AI / ML', avatar: 'memory' },
          { name: 'Data Scientist', avatar: 'scatter_plot' }
        ],

        level_options: [
          { name: 'Introduction', avatar: 'exposure_zero' },
          { name: 'Intermediate', avatar: 'exposure_plus_1' },
          { name: 'Advanced', avatar: 'exposure_plus_2' }
        ],

        background_options: [
          { name: 'Business', avatar: 'golf_course' }, // alt: money
          { name: 'Developer', avatar: 'settings' },
          { name: 'Scientist', avatar: 'wb_sunny' }
        ]

      }

      d.selected_fields = d.field_options.map(rec => rec.name)
      d.selected_levels = d.level_options.map(rec => rec.name)
      d.selected_backgrounds = d.background_options.map(rec => rec.name)

      return d
    },
    methods: {
      remove_field (item) {
        const index = this.selected_fields.indexOf(item.name)
        if (index >= 0) this.selected_fields.splice(index, 1)
      },
      remove_level (item) {
        const index = this.selected_levels.indexOf(item.name)
        if (index >= 0) this.selected_levels.splice(index, 1)
      },
      remove_background (item) {
        const index = this.selected_backgrounds.indexOf(item.name)
        if (index >= 0) this.selected_backgrounds.splice(index, 1)
      }
    }
  }
</script>
