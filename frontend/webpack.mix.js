const mix = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel applications. By default, we are compiling the CSS
 | file for the application as well as bundling up all the JS files.
 |
 */

mix.js('src/js/index.js', 'js')
    .postCss('src/styles/main.css', 'css', [
        require('tailwindcss'),
        require('autoprefixer'),
    ])
    .setPublicPath('../backend/static/build');

// If you want to use Sass
// mix.sass('src/scss/app.scss', 'css');

if (mix.inProduction()) {
    mix.version();
}
