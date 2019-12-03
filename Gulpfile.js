var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var autoprefixer = require('autoprefixer');
var sourcemaps = require('gulp-sourcemaps');
var postcss = require('gulp-postcss');
var cssnano = require('cssnano');
var uglify = require('gulp-uglify');
var browserSync = require('browser-sync').create();
var reload = browserSync.reload;



// this task can be called from the terminal with 'gulp django'
gulp.task('django', function() {
    const spawn = require('child_process').spawn;
    return spawn('python', ['manage.py', 'runserver'])
        .stderr.on('data', (data) => {
        console.log(`${data}`);
    });
});

// Compile main.sass into autoprefixed style.css
gulp.task('styles', function() {
    gulp.src('/assets/scss/main.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(concat('styles.css'))
        .pipe(sourcemaps.init())
        .pipe(postcss([autoprefixer() ,/*cssnano()*/])) // add browser prefix and minifies
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('/dist/css'));
});


/** JavaScript
*/

gulp.task('js', function(){
  return gulp.src([
    '/assets/js/vendors/jquery.js',
    '/assets/js/vendors/materialize.js',
    '/assets/js/*.js',
  ],{ base: '.', sourcemaps: true })
  // .pipe(uglify()) // minifies the JS
  .pipe(concat('scripts.js', { newline: ';\r\n' })) // One JS file to rule them all
  .pipe(gulp.dest('/dist/js/', { sourcemaps: '.' }));
});

// Initiate browsersync and point it at localhost:8000
gulp.task('browsersync', function() {
    browserSync.init({
        notify: true,
        proxy: "localhost:8000",
    });
});

gulp.task('watch', function() {
    gulp.watch('/assets/scss/**/*.scss', ['styles']);
    gulp.watch('/assets/js/**/*.js', ['js']);

    // Tell browsersync to reload any time sass, css, html, python, or
    // javascript files change
    gulp.watch(['/**/*.{scss,css,html,py,js}'], reload);
});

// This task can be called with `gulp`
gulp.task('default', ['django', 'browsersync', 'watch']);
