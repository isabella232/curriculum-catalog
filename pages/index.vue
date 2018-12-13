<template>
  <v-layout justify-center>
    <v-flex xs12 sm12 md10>

      <h2 class="mt-3 mb-3">Course Filters</h2>

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

      <h2 class="mt-3 mb-3">Course Listing</h2>

      <v-expansion-panel>
        <v-expansion-panel-content
          v-for="(c,i) in mini_courses"
          :key="i"
        >
          <v-layout slot="header" fill-height>
            <v-avatar size=35 :tile="false">
              <v-icon v-if="c.avatar">{{ c.avatar }}</v-icon>
              <img v-if="c.avatar_url" :src="c.avatar_url">
            </v-avatar>
            <v-flex align-self-center ml-2>
              {{ c.title }}
            </v-flex>
            <v-flex align-self-center shrink>
              <v-chip small disabled outline
               v-for="(tag,i) in c.tags" :key="i"
              >
                {{ tag }}
              </v-chip>
            </v-flex>
          </v-layout>
          <v-card dark color="blue" class="darken-4">
            <v-card-text>
              <ul v-for="(objective,i) in c.objectives" :key="i">
                <li>{{ objective.text }}</li>
                <ul v-if="objective.sublist" v-for="sl in objective.sublist">
                  <li>{{ sl }}</li>
                </ul>
              </ul>
            </v-card-text>
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
          { name: 'Python', avatar_url: './Python_color.png' },
          { name: 'AI / ML', avatar: 'memory' },
          { name: 'Data Science', avatar: 'scatter_plot' },
          { name: 'Other', avatar: 'code' }
        ],

        level_options: [
          { name: 'Introduction', avatar: 'exposure_zero' },
          { name: 'Intermediate', avatar: 'exposure_plus_1' },
          { name: 'Advanced', avatar: 'exposure_plus_2' }
        ],

        // background_options: [
        //   { name: 'Business', avatar: 'golf_course' }, // alt: money
        //   { name: 'Developer', avatar: 'settings' },
        //   { name: 'Scientist', avatar: 'wb_sunny' }
        // ],

        mini_courses: [
          {
            title: 'A Taste of Python for Experienced Developers',
            avatar_url: './Python_color.png',
            tags: ['Python', 'Introduction'],
            objectives: [
              {
                text: 'Learn the basic language features (and syntax) of Python: Objects, Looping, Conditionals, List, Dictionaries, Functions',
                sublist: []
              },
              {
                text: 'Be able to use:',
                sublist: [
                  'The Python interpreter,',
                  'IPython as a more feature-full interpreter,',
                  'Jupyter as the next-generation of IPython,',
                  'and stand-alone python scripts.'
                ]
              },
              {
                text: 'Be able to write simple Python scripts (e.g. to replace bash scripts or other simple scripts).',
                sublist: []
              }
            ]
          },

          {
            title: 'The Python Ecosystem for Full-scale Apps',
            avatar_url: './Python_color.png',
            tags: ['Python', 'Introduction'],
            objectives: [
              {
                text: 'Discover the broad Python ecosystem which facilitate building full-scale applications in Python, e.g.:',
                sublist: [
                  '`modules` and `packages`,',
                  'virtual environment,',
                  'testing frameworks,',
                  'application frameworks (for web and otherwise),',
                  'packaging systems, and',
                  'data science toolkits and the “PyData stack”.'
                ]
              }
            ]
          },

          {
            title: 'Python Looping Idioms',
            avatar_url: './Python_color.png',
            tags: ['Python', 'Intermediate'],
            objectives: [
              {
                text: 'Learn the idiomatic ways to loop in Python: enumerate, zip, sorted, reversed, itertools.',
                sublist: []
              },
              {
                text: 'Build their own iterable objects (the `__iter__` and `__next__` methods).',
                sublist: []
              },
              {
                text: 'Use and build generator (functions that `yield`).',
                sublist: []
              },
              {
                text: 'Learn generator expressions and list comprehensions.',
                sublist: []
              }
            ]
          },

          {
            title: 'Python Ideologies',
            avatar_url: './Python_color.png',
            tags: ['Python', 'Intermediate'],
            objectives: [
              {
                text: 'Learn the most common coding conventions from both PEP8 and Google’s Python Style Guide.',
                sublist: []
              },
              {
                text: 'Learn a little what it means to be “Pythonic”: The Python Manifesto, Coding with Intent, writing “Beautiful” code.',
                sublist: []
              }
            ]
          },

          {
            title: 'Python Builtin Modules and Data Structures',
            avatar_url: './Python_color.png',
            tags: ['Python', 'Intermediate'],
            objectives: [
              {
                text: 'Learn the features of the `collections` builtin module: defaultdict, Counter, namedtuple, deque, etc.',
                sublist: []
              },
              {
                text: 'Be able to call low-level OS function through the builtin `os` module.',
                sublist: []
              },
              {
                text: 'Be able to read/write files with various formats: XML, JSON, CSV, MS Excel, SQLite, pickle.',
                sublist: []
              },
              {
                text: 'Learn how to manipulate strings and dates in Python.',
                sublist: []
              }
            ]
          },

          {
            title: 'Python Functions: First-class-ness, Callbacks, Closures, and Decorators',
            avatar_url: './Python_color.png',
            tags: ['Python', 'Intermediate'],
            objectives: [
              {
                text: 'Understand functions as a first-class type in Python:',
                sublist: []
              },
              {
                text: 'Be able to pass functions as parameters to other functions (e.g. sort, pd.apply, etc.)',
                sublist: []
              },
              {
                text: 'Understand and be able to write function closures:',
                sublist: []
              },
              {
                text: 'Be able to return new functions from another function.',
                sublist: []
              },
              {
                text: 'Understand and be able to write function decorators:',
                sublist: []
              },
              {
                text: 'Understand decorators as a design pattern.',
                sublist: []
              },
              {
                text: 'Understand Python’s decorator syntax (“syntactic sugar”).',
                sublist: []
              }
            ]
          },

          {
            title: 'Python Classes and Inheritance for the Experienced Developer',
            avatar_url: './Python_color.png',
            tags: ['Python', 'Advanced'],
            objectives: [
              {
                text: 'Learn Python’s class syntax and scoping rules (not what you’d expect!)',
                sublist: []
              },
              {
                text: 'Understand the difference between statically-typed languages and dynamically-typed languages, and be able to articulate the pros and cons of each.',
                sublist: []
              },
              {
                text: 'Use Python’s dynamic typing system to write reusable functions (embrace “duck typing”).',
                sublist: []
              },
              {
                text: 'Learn (a handful of) Python’s magic methods.',
                sublist: []
              },
              {
                text: 'Learn when inheritance makes sense in Python.',
                sublist: []
              }
            ]
          },

          {
            title: 'Python Case Study: Write a DataFrame object using only Python builtins!',
            avatar_url: './Python_color.png',
            tags: ['Python', 'Advanced'],
            objectives: [
              {
                text: 'Case study requirements:',
                sublist: [
                  'Use only Python’s builtin modules, data structures and language features.',
                  'Build a `DataFrame` class (similar to Panda\'s, but with your own spin on things).',
                  'Use magic methods to create a flexible and readable interface.',
                  'Write documentation about what features your DataFrame supports, and what features it does not support.'
                ]
              }
            ]
          },

          {
            title: 'Packaging in Python for Internal and External Distribution',
            avatar_url: './Conda.png',
            tags: ['Python', 'Advanced'],
            objectives: [
              {
                text: 'Learn the differences between `conda-forge` and `PyPI`.',
                sublist: []
              },
              {
                text: 'Learn how to use Conda to package Python for both internal and/or external distribution.',
                sublist: []
              }
            ]
          },

          {
            title: 'Python C-extensions and the GIL',
            avatar_url: './Python_color.png',
            tags: ['Python', 'Advanced'],
            objectives: [
              {
                text: 'Write, compile, and use a C-extension from scratch.',
                sublist: []
              },
              {
                text: 'Wrap, compile, and use an existing C-library.',
                sublist: []
              },
              {
                text: 'Learn what the GIL is, why it exists, and how to parallelize code despite the GIL (i.e. how to release the GIL in your C-extension to allow parallelism).',
                sublist: []
              }
            ]
          },

          {
            title: 'Scientific Computing in Python: Overview',
            avatar_url: './pydata-logo.png',
            tags: ['Data Science', 'Introduction'],
            objectives: [
              {
                text: 'Explore, learn, and practice:',
                sublist: [
                  'SciPy for so many things,',
                  'NumPy for n-dimensional arrays,',
                  'Pandas for DataFrames,',
                  'StatsModels for … you guessed it, statistical models!'
                ]
              }
            ]
          },

          {
            title: 'Scientific Computing in Python: Fast Numeric Computation',
            avatar_url: './pydata-logo.png',
            tags: ['Data Science', 'Intermediate'],
            objectives: [
              {
                text: 'Explore, learn, and practice:',
                sublist: [
                  'vectorized operations in NumPy,',
                  'avoiding inefficient combinations of operations with NumPy,',
                  'distributed computation with Dask (introduction only),',
                  'GPU computation with Numba (introduction only).'
                ]
              }
            ]
          },

          {
            title: 'NumPy Full Tour',
            avatar_url: './numpy-logo-300.png',
            tags: ['Data Science', 'Intermediate'],
            objectives: [
              {
                text: 'Explore the entire NumPy API (very quickly!) in order to obtain a gut-feeling for it’s overall capabilities (don’t reinvent the wheel).',
                sublist: []
              }
            ]
          },

          {
            title: 'Statistics with Python: Hypothesis Testing and Confidence Intervals',
            avatar_url: './pydata-logo.png',
            tags: ['Data Science', 'Introduction'],
            objectives: [
              {
                text: 'Be able to recite precisely the answer to “What actually is a p-value?”',
                sublist: []
              },
              {
                text: 'Understand the tenets of random sampling and hypothesis testing, and understand its strengths and weaknesses.',
                sublist: []
              },
              {
                text: 'Be able to compute confidence intervals and understand how they relate to hypothesis testing.',
                sublist: []
              },
              {
                text: 'Be able to compute p-values, confidence intervals, and run hypothesis tests in Python with SciPy.',
                sublist: []
              }
            ]
          },

          {
            title: 'Statistics with Python: Random Variables and Common Distributions',
            avatar_url: './pydata-logo.png',
            tags: ['Data Science', 'Intermediate'],
            objectives: [
              {
                text: 'Learn the concept of random variables.',
                sublist: []
              },
              {
                text: 'Understand the difference between continuous random variables and discrete random variables.',
                sublist: []
              },
              {
                text: 'Understand the the common probability distributions (normal, uniform, gamma, poison, bernoulli, binomial, etc).',
                sublist: []
              },
              {
                text: 'Be able to compute PDFs, PMFs, CDFs, etc using Python with SciPy.',
                sublist: []
              },
              {
                text: 'Use statsmodels to do linear regression and regression analysis.',
                sublist: []
              }
            ]
          },

          {
            title: 'Statistics with Python: Modern Methods',
            avatar_url: './pydata-logo.png',
            tags: ['Data Science', 'Advanced'],
            objectives: [
              {
                text: 'Learn and practice:',
                sublist: [
                  'Bootstrapping,',
                  'Bayesian statistics,',
                  'Why they are “modern” methods.'
                ]
              }
            ]
          },

          {
            title: 'Exploratory Data Analysis with Pandas: Baisc Operations',
            avatar_url: './pandas_logo.png',
            tags: ['Data Science', 'Introduction'],
            objectives: [
              {
                text: 'Learn to read data into Pandas DataFrames from common formats: CSV, TSV, JSON, XML, HTML, HDF5, SAS, Excel',
                sublist: []
              },
              {
                text: 'Be able to convert to the proper datatypes, and view summary statistics of a DataFrame.',
                sublist: []
              },
              {
                text: 'Learn to filtering data using Series objects, indexing, and boolean masks.',
                sublist: []
              },
              {
                text: 'Be able to merge/append/concatenate DataFrames.',
                sublist: []
              },
              {
                text: 'Be able to export data to common formats: CSV, TSV, JSON, XML, HTML, HDF5, SAS, Excel',
                sublist: []
              },
              {
                text: 'Learn how to create basic plots through Pandas.',
                sublist: []
              }
            ]
          },

          {
            title: 'Exploratory Data Analysis with Pandas: Transformation and Aggregation',
            avatar_url: './pandas_logo.png',
            tags: ['Data Science', 'Intermediate'],
            objectives: [
              {
                text: 'Be able to transform data within DataFrames and Series (including datetime and string transformations).',
                sublist: []
              },
              {
                text: 'Understand and use the group-by operations and workflow of:',
                sublist: [
                  'Aggregation',
                  'Transformation',
                  'Filtration'
                ]
              }
            ]
          },

          {
            title: 'Exploratory Data Analysis with Pandas: Optimizations, Milti-index, and Time Series',
            avatar_url: './pandas_logo.png',
            tags: ['Data Science', 'Advanced'],
            objectives: [
              {
                text: 'Learn and practice:',
                sublist: [
                  'Why vectorized operations are fast and should always be used.',
                  'How to recognize and avoid n^2 operations (easy to accidentally do with Pandas; kills performance).',
                  'The intricacies of the multi-index DataFrames.',
                  'How to store time-series in Pandas (and date/time manipulation and resampling).'
                ]
              }
            ]
          },

          {
            title: 'Plotting in Python with Matplotlib',
            avatar_url: './matplotlib-logo-300.png',
            tags: ['Data Science', 'Introduction'],
            objectives: [
              {
                text: 'Learn and practice:',
                sublist: [
                  'Two interfaces to Matplotlib: global, OOP',
                  'Seaborn: A convenience layer atop Matplotlib',
                  'Plotting through Pandas: Another convenience layer'
                ]
              }
            ]
          },

          {
            title: 'Plotting in Python with Bokeh',
            avatar_url: './bokeh-logo-300.png',
            tags: ['Data Science', 'Intermediate'],
            objectives: [
              {
                text: 'Learn the capabilities of the Bokeh plotting library.',
                sublist: []
              },
              {
                text: 'Use Bokeh to create interactive plots in Jupyter.',
                sublist: []
              },
              {
                text: 'Use Bokeh to create interactive plots to publish on the Web.',
                sublist: []
              }
            ]
          },

          {
            title: 'Plotting in Python with Specialized Libraries',
            avatar_url: './PyViz_logo_wm.png',
            tags: ['Data Science', 'Advanced'],
            objectives: [
              {
                text: 'Create plots using other plotting libraries:',
                sublist: [
                  'Datashader',
                  'GeoViews'
                ]
              },
              {
                text: 'Using PyViz as a high-level plotting library.',
                sublist: []
              }
            ]
          },

          {
            title: 'Machine Learning Concepts: Core Concepts',
            avatar: 'memory',
            tags: ['AI / ML', 'Introduction'],
            objectives: [
              {
                text: 'Be introduced to the three main subfields of Machine Learning through examples, three examples from each of: Supervised, Unsupervised, and Reinforcement.',
                sublist: []
              },
              {
                text: 'Learn the fundamental methodology of Supervised Machine Learning (function estimation and model validation).',
                sublist: []
              }
            ]
          },

          {
            title: 'Machine Learning Concepts: Simple Models',
            avatar: 'memory',
            tags: ['AI / ML', 'Intermediate'],
            objectives: [
              {
                text: 'Intro to a few simple supervised ML modes:',
                sublist: [
                  'Linear regression',
                  'kNN',
                  'Decision trees',
                  'Random Forests',
                  'Intro to simple unsupervised ML models:',
                  'K-means',
                  'Hierarchical clustering'
                ]
              }
            ]
          },

          {
            title: 'Machine Learning Concepts: Complex Models',
            avatar: 'memory',
            tags: ['AI / ML', 'Advanced'],
            objectives: [
              {
                text: 'Intro to more supervised ML models:',
                sublist: [
                  'Gradient Boosting (trees, specifically)',
                  'SVMs',
                  'Neural networks'
                ]
              }
            ]
          },

          {
            title: 'Machine Learning in Python: Intro to Scikit-Learn',
            avatar_url: './scikit-learn-logo-notext.png',
            tags: ['AI / ML', 'Introduction'],
            objectives: [
              {
                text: 'Intro to the capabilities of scikit-learn.',
                sublist: []
              },
              {
                text: 'Gain intro experience using scikit-learn with an exercise.',
                sublist: []
              }
            ]
          },

          {
            title: 'Machine Learning in Python: Scikit-Learn\'s Pipelines and Grid Searching',
            avatar_url: './scikit-learn-logo-notext.png',
            tags: ['AI / ML', 'Intermediate'],
            objectives: [
              {
                text: 'Learn and use scikit-learn’s Pipelines and FeatureUnions to ensure proper (1) reproducibility, (2) validation methodology, and (3) code reusability.',
                sublist: []
              },
              {
                text: 'Use grid searching with scikit-learn to find optimal models.',
                sublist: []
              }
            ]
          },

          {
            title: 'Machine Learning in Python: Preprocessing and Meta-models with Scikit-Learn',
            avatar_url: './scikit-learn-logo-notext.png',
            tags: ['AI / ML', 'Advanced'],
            objectives: [
              {
                text: 'Intro to preprocessing data and feature engineering (examples given of images, text, audio, and tabular).',
                sublist: []
              },
              {
                text: 'Intro to committees of models, and cascades of models.',
                sublist: []
              }
            ]
          },

          {
            title: 'Machine Learning in Python: Intro to PyTorch',
            avatar_url: './pytorch-logo.png',
            tags: ['AI / ML', 'Introduction'],
            objectives: [
              {
                text: 'Intro to the capabilities of PyTorch.',
                sublist: []
              },
              {
                text: 'Gain intro experience using PyTorch with an exercise.',
                sublist: []
              }
            ]
          },

          {
            title: 'Webscraping with Python',
            avatar: 'share',
            tags: ['Other', 'Intermediate'],
            objectives: [
              {
                text: 'Learn to parse HTML using BeautifulSoup.',
                sublist: []
              },
              {
                text: 'Learn to automate the web browser (for scraping purposes) using Selenium.',
                sublist: []
              }
            ]
          }
        ]

      }

      d.selected_fields = d.field_options.map(rec => rec.name)
      d.selected_levels = d.level_options.map(rec => rec.name)
      // d.selected_backgrounds = d.background_options.map(rec => rec.name)

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
      }
      // remove_background (item) {
      //   const index = this.selected_backgrounds.indexOf(item.name)
      //   if (index >= 0) this.selected_backgrounds.splice(index, 1)
      // }
    }
  }
</script>
