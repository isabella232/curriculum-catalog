<template>
  <v-container>
    <v-layout row>
      <v-flex xs12 sm12 md12>
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
      </v-flex>
    </v-layout>

    <v-layout row>
      <v-flex xs7 sm7 md7>
        <h2 class="mt-3 mb-3">Course Listing</h2>
        <h3>Each course lasts for half a day (3 hours)</h3>
        <v-expansion-panel>
          <transition-group name="list" tag="v-expansion-panel">
          <v-expansion-panel-content
            v-for="c in active_courses"
            :key="c.index"
          >
            <v-layout slot="header" fill-height align-center>
              <input type="checkbox" :id="c.index" :value="c.title" v-model="selectedCourses" @click.stop/>
              <v-avatar class="ml-2" size=35 :tile="false">
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
          </transition-group>
        </v-expansion-panel>
      </v-flex>

      <v-flex offset-xs1 offset-sm1 offset-md1 xs4 sm4 md4>
        <v-layout column fill-height>
          <div class="sticky">
            <h2 class="mt-3">Selected Courses</h2>
            <h4>Use the checkboxes to select courses you are interested in learning more about</h4>
            <h5 class="mt-3 mb-3">Selected courses will take {{ selectedCourses.length * 0.5}} days ({{ selectedCourses.length * 3}} hours total)</h5>
            <div class="scrollable">
              <li v-for="course in selectedCourses">
                {{course.toString()}}
              </li>

            </div>

            <v-text-field
              label="Insert Company Name"
              hint="Example Inc."
              v-model="company"
              :error-messages="companyErrors"
              required
              persistent-hint
              @input="$v.company.$touch()"
              @blur="$v.company.$touch()"
              ></v-text-field>

            <v-text-field
              label="Insert Email"
              hint="example@email.com"
              v-model="email"
              :error-messages="emailErrors"
              required
              persistent-hint
              @input="$v.email.$touch()"
              @blur="$v.email.$touch()"
              ></v-text-field>

            <v-btn block @click="send" :disabled="!is_complete">Start Conversation</v-btn>
          </div>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<style>
  .list-enter-active,
  .list-leave-active {
    transition: all 0.3s;
  }

  .list-enter,
  .list-leave-to {
    opacity: 0;
    transform: translateX(5vw);
  }

  .list-enter-to,
  .list-leave {
    opacity: 1;
  }

  .list-move {
    transition: all 0.3s;
  }

  .sticky {
    position: -webkit-sticky;
    position: sticky;
    top: 100px;
    bottom: 32px;
  }

  .scrollable {
    max-height: 20vh;
    min-height: 20vh;
    overflow: hidden;
    overflow-y: auto;
  }

</style>

<script>
  import { validationMixin } from 'vuelidate'
  import { required, email } from 'vuelidate/lib/validators'

  export default {
    mixins: [validationMixin],

    validations: {
      company: { required },
      email: { required, email }
    },

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

        selectedCourses: [],

        company: '',

        email: '',

        custom: {
          company: {
            required: () => 'Company Name cannot be empty'
          },
          email: {
            required: () => 'Email cannot be empty'
          }
        },

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
              },
              {
                text: 'LAB: Practice Python by finding Happy Numbers!',
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
                text: 'Apply the idiomatic ways to loop in Python: enumerate, zip, sorted, reversed, itertools.',
                sublist: []
              },
              {
                text: 'Build their own iterable objects (the `__iter__` and `__next__` methods).',
                sublist: []
              },
              {
                text: 'Use and build generators (functions that `yield`).',
                sublist: []
              },
              {
                text: 'Construct generator expressions and list comprehensions.',
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
                text: 'Implement the most common coding conventions from both PEP8 and Google’s Python Style Guide.',
                sublist: []
              },
              {
                text: 'Demonstrate what it means to be “Pythonic”: The Python Manifesto, Coding with Intent, writing “Beautiful” code.',
                sublist: []
              }
            ]
          },

          {
            title: 'Python Built-in Modules and Data Structures',
            avatar_url: './Python_color.png',
            tags: ['Python', 'Intermediate'],
            objectives: [
              {
                text: 'Use and distinguish between the features of the `collections` built-in module: defaultdict, Counter, namedtuple, deque, etc.',
                sublist: []
              },
              {
                text: 'Call low-level OS function through the built-in `os` module.',
                sublist: []
              },
              {
                text: 'Read/write files with various formats: XML, JSON, CSV, MS Excel, SQLite, pickle.',
                sublist: []
              },
              {
                text: 'Manipulate strings and dates in Python.',
                sublist: []
              },
              {
                text: 'LAB: Practice Python: Process CSV files to answers questions about weather patterns.',
                sublist: []
              }
            ]
          },

          {
            title: 'Python Functions: First-class Objects, Callbacks, Closures, and Decorators',
            avatar_url: './Python_color.png',
            tags: ['Python', 'Intermediate'],
            objectives: [
              {
                text: 'Explain the significance of functions being first-class objects in Python.',
                sublist: []
              },
              {
                text: 'Pass functions as parameters to other functions (e.g. sort, pd.apply, etc.)',
                sublist: []
              },
              {
                text: 'Write function closures:',
                sublist: []
              },
              {
                text: 'Return new functions from another function.',
                sublist: []
              },
              {
                text: 'Construct and apply function decorators appropriately',
                sublist: []
              },
              {
                text: 'Explain the significance of decorators as a design pattern.',
                sublist: []
              },
              {
                text: 'Write code using Python’s decorator syntax (“syntactic sugar”).',
                sublist: []
              },
              {
                text: '(optional) Use the `pdb` module (the “python debugger” module).',
                sublist: []
              },
              {
                text: '(optional) Explore graphical python debuggers.',
                sublist: []
              },
              {
                text: 'LAB: Practice the “DRY” principle; a small codebase will be provided:',
                sublist: [
                  'Refactor the codebase to eliminate the repeated code. “Don’t repeat yourself!” Use closures and decorators to achieve this goal.',
                  'Document the code with docstrings.'
                ]
              }
            ]
          },

          {
            title: 'Python Classes and Inheritance for the Experienced Developer',
            avatar_url: './Python_color.png',
            tags: ['Python', 'Advanced'],
            objectives: [
              {
                text: 'Utilize Python’s class syntax and scoping rules (not what you’d expect!)',
                sublist: []
              },
              {
                text: 'Explain the difference between statically-typed languages and dynamically-typed languages, and be able to articulate the pros and cons of each.',
                sublist: []
              },
              {
                text: 'Use Python’s dynamic typing system to write reusable functions (embrace “duck typing”).',
                sublist: []
              },
              {
                text: 'Utilize Python’s magic methods.',
                sublist: []
              },
              {
                text: 'Describe when inheritance makes sense in Python.',
                sublist: []
              }
            ]
          },

          {
            title: 'Python Case Study: Write a DataFrame object using only Python builtins',
            avatar_url: './Python_color.png',
            tags: ['Python', 'Advanced'],
            objectives: [
              {
                text: 'Case study requirements:',
                sublist: [
                  'Use only Python’s builtin modules, data structures and language features.',
                  'Build a `DataFrame` class (similar to Pandas, but with your own spin on things).',
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
                text: 'Articulate what the GIL is, why it exists, and how to parallelize code despite the GIL (i.e. how to release the GIL in your C-extension to allow parallelism).',
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
                text: 'Utilize basic functionality of SciPy, NumPy, and Pandas.',
                sublist: []
              },
              {
                text: 'Describe the multitude of uses for SciPy.',
                sublist: []
              },
              {
                text: 'Describe NumPy n-dimensional arrays and why NumPy is groundbreaking.',
                sublist: []
              },
              {
                text: 'Explain the use and importance of DataFrames in Pandas.',
                sublist: []
              },
              {
                text: 'Articulate how StatsModels is used for … you guessed it, statistical models!',
                sublist: []
              }
            ]
          },

          {
            title: 'Scientific Computing in Python: Fast Numeric Computation',
            avatar_url: './pydata-logo.png',
            tags: ['Data Science', 'Intermediate'],
            objectives: [
              {
                text: 'Write vectorized operations in NumPy,',
                sublist: []
              },
              {
                text: 'Avoid and describe inefficient combinations of operations with NumPy,',
                sublist: []
              },
              {
                text: 'Explain distributed computation with Dask',
                sublist: []
              },
              {
                text: 'Describe in detail GPU computation with Numba.',
                sublist: []
              }
            ]
          },

          {
            title: 'NumPy Full Tour',
            avatar_url: './numpy-logo-300.png',
            tags: ['Data Science', 'Intermediate'],
            objectives: [
              {
                text: 'Explore the entire NumPy API (very quickly!) to obtain a solid understanding of its overall capabilities.',
                sublist: []
              },
              {
                text: 'LAB: Code golf',
                sublist: [
                  'Given a set of challenges, write code to solve each challenge and minimize the number of NumPy function calls. I.e. For each challenge, find and use the most appropriate NumPy function (or collection of functions).'
                ]
              }
            ]
          },

          {
            title: 'Statistics with Python: Hypothesis Testing and Confidence Intervals',
            avatar_url: './pydata-logo.png',
            tags: ['Data Science', 'Introduction'],
            objectives: [
              {
                text: 'Answer precisely the question “What actually is a p-value?”',
                sublist: []
              },
              {
                text: 'Apply the tenets of random sampling and hypothesis testing, and understand their strengths and weaknesses.',
                sublist: []
              },
              {
                text: 'Compute confidence intervals and understand how they relate to hypothesis testing.',
                sublist: []
              },
              {
                text: 'Calculate p-values, confidence intervals, and run hypothesis tests in Python with SciPy.',
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
                text: 'Define what a random variable is.',
                sublist: []
              },
              {
                text: 'Articulate the difference between continuous random variables and discrete random variables.',
                sublist: []
              },
              {
                text: 'Describe the the common probability distributions (normal, uniform, gamma, poison, bernoulli, binomial, etc).',
                sublist: []
              },
              {
                text: 'Compute PDFs, PMFs, CDFs, etc using Python with SciPy.',
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
                text: 'Understand and apply Bootstrap Method',
                sublist: []
              },
              {
                text: 'Apply Bayesian statistics to datasets using Python',
                sublist: []
              },
              {
                text: 'Articulate “modern” statistical methods in Python',
                sublist: []
              }
            ]
          },

          {
            title: 'Exploratory Data Analysis with Pandas: Basic Operations',
            avatar_url: './pandas_logo.png',
            tags: ['Data Science', 'Introduction'],
            objectives: [
              {
                text: 'Read data into DataFrames from common formats: CSV, TSV, JSON, XML, HTML, HDF5, SAS, Excel',
                sublist: []
              },
              {
                text: 'Convert to the proper datatypes, and view summary statistics of a DataFrame.',
                sublist: []
              },
              {
                text: 'Filter data using Series objects, indexing, and boolean masks.',
                sublist: []
              },
              {
                text: 'Merge, append, and concatenate DataFrames.',
                sublist: []
              },
              {
                text: 'Export data to common formats: CSV, TSV, JSON, XML, HTML, HDF5, SAS, Excel',
                sublist: []
              },
              {
                text: 'Construct basic plots through Pandas.',
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
                text: 'Transform data within DataFrames and Series using datetime and string transformations.',
                sublist: []
              },
              {
                text: 'Utilize group-by operations and workflow of aggregation, transformation, and filtration.',
                sublist: []
              }
            ]
          },

          {
            title: 'Exploratory Data Analysis with Pandas: Optimizations, Multi-index, and Time Series',
            avatar_url: './pandas_logo.png',
            tags: ['Data Science', 'Advanced'],
            objectives: [
              {
                text: 'Articulate why vectorized operations are fast and should always be used.',
                sublist: []
              },
              {
                text: 'Recognize and avoid n^2 operations which kill performance in Pandas.',
                sublist: []
              },
              {
                text: 'Learn how Pandas manages memory, slices, views, and copies.',
                sublist: []
              },
              {
                text: 'Demonstrate the intricacies of the multi-index DataFrames.',
                sublist: []
              },
              {
                text: 'Store time-series in Pandas applying date/time manipulation and resampling.',
                sublist: []
              },
              {
                text: 'LAB: Speed up a slow Pandas pipeline by removing the inefficiencies; a dataset and a small script will be provided:',
                sublist: [
                  'Modify the code to make it run faster (we’re talking several orders of magnitude faster).',
                  'Examine the memory usage of your refactored code. Extrapolate to estimate how large of a similar dataset you would be able to handle on your computer.'
                ]
              }
            ]
          },

          {
            title: 'Processing Excel Files',
            avatar_url: './logo-connector-excel.png',
            tags: ['Data Science', 'Intermediate'],
            objectives: [
              {
                text: 'Use OpenPyXL and XlsxWriter to:',
                sublist: [
                  'Generate automated reports of Excel usage patterns, such as uses of formulas and external references.',
                  'Automate the conversion of various data sources to Excel.',
                  'Automate the standardization of cell formatting and styling.',
                  'Perform automated validation on a large number of Excel files.'
                ]
              },
              {
                text: 'Use xlwings to enable real-time integration of Excel and Python.',
                sublist: []
              }
            ]
          },

          {
            title: 'Plotting in Python with Matplotlib and Convenience Layers',
            avatar_url: './matplotlib-logo-300.png',
            tags: ['Data Science', 'Introduction'],
            objectives: [
              {
                text: 'Create plots in Matplotlib using two interfaces: global, OOP',
                sublist: []
              },
              {
                text: 'Use Seaborn as a convenience layer atop Matplotlib',
                sublist: []
              },
              {
                text: 'Construct plots using Pandas as another convenience layer',
                sublist: []
              }
            ]
          },

          {
            title: 'Plotting in Python with Bokeh',
            avatar_url: './bokeh-logo-300.png',
            tags: ['Data Science', 'Intermediate'],
            objectives: [
              {
                text: 'Explore the capabilities of the Bokeh plotting library.',
                sublist: []
              },
              {
                text: 'Use Bokeh to create interactive plots in Jupyter.',
                sublist: []
              },
              {
                text: 'Publish interactive plots to the web using Bokeh.',
                sublist: []
              },
              {
                text: 'LAB: Extend a sample Bokeh application to include more functionality',
                sublist: [
                  'Given a small codebase which produces a Bokeh plot, extend the codebase to add new functionality. A dataset and a prompt will also be provided.'
                ]
              }
            ]
          },

          {
            title: 'Plotting in Python with Specialized Libraries',
            avatar_url: './PyViz_logo_wm.png',
            tags: ['Data Science', 'Advanced'],
            objectives: [
              {
                text: 'Create plots using alternative plotting libraries:',
                sublist: [
                  'Datashader',
                  'GeoViews'
                ]
              },
              {
                text: 'Use PyViz as a high-level plotting library.',
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
                text: 'Differentiate between the three main subfields of Machine Learning, supervised, unsupervised, and reinforcement, through a hands-on approach',
                sublist: []
              },
              {
                text: 'Apply the fundamental methodology of Supervised Machine Learning (function estimation and model validation).',
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
                text: 'Work with several simple supervised ML models:',
                sublist: [
                  'Linear regression',
                  'kNN',
                  'Decision trees',
                  'Random Forests'
                ]
              },
              {
                text: 'Explore and run simple unsupervised ML models:',
                sublist: [
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
                text: 'Dive into more complex supervised ML models:',
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
                text: 'Explore basic functionality of scikit-learn with a hands-on approach.',
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
                text: 'Use scikit-learn’s Pipelines and FeatureUnions to ensure proper reproducibility, validation methodology, and code reusability.',
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
                text: 'Explore basic functionality of PyTorch hands-on.',
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
          },

          {
            title: 'Google Protocol Buffers in Python',
            avatar_url: './Python_color.png',
            tags: ['Other', 'Advanced'],
            objectives: [
              {
                text: 'Learn what Google Protocol Buffers are for, and discuss when it makes sense to use them.',
                sublist: []
              },
              {
                text: 'Create and save a .proto file, which will define the format in which your data will be stored in.',
                sublist: []
              },
              {
                text: 'Compile the .proto file to generate fast, efficient, robust Python code.',
                sublist: []
              },
              {
                text: 'Use the generated Python code to store and retrieve objects in the format defined by the original .proto file.',
                sublist: []
              },
              {
                text: 'Specify a group of fields where at most one of the fields will be set within a single message, using the language\'s "oneof" feature.',
                sublist: []
              },
              {
                text: 'Split your data definition into several .proto files, and use the language\'s "import" statement to reference definitions which are outside the current file.',
                sublist: []
              }
            ]
          }

        ]

      }

      d.selected_fields = d.field_options.map(rec => rec.name)
      d.selected_levels = d.level_options.map(rec => rec.name)
      // d.selected_backgrounds = d.background_options.map(rec => rec.name)

      for (var i = 0; i < d.mini_courses.length; i++) {
        d.mini_courses[i].index = i
      }

      return d
    },

    computed: {
      active_courses () {
        var active = []
        for (var i = 0; i < this.mini_courses.length; i++) {
          var fieldTag = this.mini_courses[i].tags[0]
          var levelTag = this.mini_courses[i].tags[1]
          if (this.selected_fields.includes(fieldTag) && this.selected_levels.includes(levelTag)) {
            active.push(this.mini_courses[i])
          }
        }
        return active
      },

      is_complete () {
        return this.company && this.email && this.selectedCourses && this.selectedCourses.length && this.$v.email.email && this.$v.email.required && this.$v.company.required
      },

      companyErrors () {
        const errors = []
        if (!this.$v.company.$dirty) return errors
        !this.$v.company.required && errors.push('Name is required.')
        return errors
      },

      emailErrors () {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.email && errors.push('Must be valid e-mail')
        !this.$v.email.required && errors.push('E-mail is required')
        return errors
      }
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

      send () {
        alert('Success! Email Sent! We will get back to you within a week')
        window.location = 'https://www.quansight.com/learning'
      }
    }
  }
</script>
