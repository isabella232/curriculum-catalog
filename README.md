# Quansight Curriculum Catalog

### Project from template

This project was generated from a template, like this:

```bash
sudo npm install -g @vue/cli
sudo npm install -g @vue/cli-init
vue init vuetifyjs/nuxt curriculum-catalog
```

### Local dev

Install the project dependecies with:

``` bash
npm install
```

Run an SSR local dev server (with hot reload):

```bash
npm run dev
```

### Production

Run an SSR production-grade server:

```bash
npm run build
npm start
```

Or generate static files for a stand-alone (no `node.js`) deployment:

```bash
npm run generate
```

To deploy to GitHub pages, use the following commands:
```bash
npm run generate
rm -rf docs
cp -r dist docs
git add docs
git commit
git push
```

It sometimes takes GitHub pages a minute or two to update, but you should see
the site go live after pushing (and some patience).


