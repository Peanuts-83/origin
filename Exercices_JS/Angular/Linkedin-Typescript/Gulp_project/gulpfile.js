var gulp = require('gulp');
var ts = require('gulp-typescript');
var browserify = require('browserify')
var tsify = require('tsify')
var source = require('vinyl-source-stream')

gulp.task('html', () => {
    return gulp.src('src/*.html')
        .pipe(gulp.dest('dist'))
})

gulp.task('browsery', function () {
    return browserify({
        basedir: '.',
        debug: true,
        entries: ['src/main.ts'],
        cache: {},
        packageCache: {}
    })
    .plugin(tsify)
    .bundle()
    .pipe(source('bundle.js'))
    .pipe(gulp.dest('dist'));
})

gulp.task('default', gulp.series('html', 'browsery'))
