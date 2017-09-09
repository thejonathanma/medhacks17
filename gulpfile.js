//utilities
var gulp = require('gulp');
var util = require('gulp-util');
var notify = require('gulp-notify');
var gulpif = require('gulp-if');
var rename = require('gulp-rename');
var concat = require('gulp-concat');
var spawn = require('child_process').spawn;
var argv = require('yargs')
    .default('port', 8000)
    .default('address', 'localhost')
    .argv;

//javascript
var source = require('vinyl-source-stream');
var streamify = require('gulp-streamify');
var uglify = require('gulp-uglify');
var browserify = require('browserify');
var babelify = require('babelify');
var watchify = require('watchify');

//css
var sass = require('gulp-sass');
var postcss = require('gulp-postcss');
var autoprefix = require('autoprefixer');
var cssnano = require('cssnano');

//build options
var options = {
    js: {
        src: "./index/static/index/js/index.js",
        dest: "./index/static/index/js",
    },
    css: {
        src: "./index/static/index/sass/index.scss",
        dest: "./index/static/index/css",
        watch: "./index/static/index/sass/**/*.scss"
    },
    app: 'manage.py',
    development: true
}

function checkDevelopment(deploy) {
    if (deploy) {
        options.development = false;
        process.env['NODE_ENV'] = 'production';
        util.log(util.colors.bgGreen('-------- Deployment Build --------'));
    } else {
        delete process.env['NODE_ENV'];
        util.log(util.colors.bgBlue('-------- Development Build --------'));
    }
}

function bundleJS() {
    var appBundler = browserify({
        entries: options.js.src,
        debug: options.development,
        cache: {},
        packageCache: {},
        fullPaths: options.development
    });

    var rebundle = function() {
        util.log(util.colors.yellow("-------- JS rebundle started -------"));
        var timer = Date.now();
        return appBundler.transform('babelify', {presets: ['es2015', 'react']})
            .bundle()
            .on('error', util.log)
            .pipe(source('index.js'))
            .pipe(gulpif(!options.development, streamify(uglify())))
            .pipe(rename('bundle.js'))
            .pipe(gulp.dest(options.js.dest))
            .pipe(notify(function() {
                util.log(util.colors.yellow('JS'), 'rebundle finished in',
                            util.colors.yellow((Date.now() - timer) + ' ms'));
            }));
    }

    if (options.development) {
        var watcher = watchify(appBundler);
        watcher.on('update', rebundle);
    }

    return rebundle();
}

function bundleCSS() {
    if (options.development) {
        var processors = [
            autoprefix({browsers: ['last 2 versions']})
        ];
    } else {
        var processors = [
            autoprefix({browsers: ['last 2 versions']}),
            cssnano()
        ];
    }

    var rebundle = function() {
        util.log(util.colors.green('-------- CSS rebundle started --------'));
        var timer = Date.now();
        return gulp.src(options.css.src)
            .pipe(concat('index.scss'))
            .pipe(sass().on('error', sass.logError))
            .pipe(postcss(processors))
            .pipe(rename('bundle.css'))
            .pipe(gulp.dest(options.css.dest))
            .pipe(notify(function() {
                util.log(util.colors.green('CSS'), 'rebundle finished in',
                            util.colors.green((Date.now() - timer) + ' ms'));
            }));
    }

    if (options.development) {
        gulp.watch(options.css.watch, rebundle);
    }

    return rebundle();
}

function runserver() {
    /*var args = [options.app, 'runserver'];
    var python = process.env['VIRTUAL_ENV'] + '/bin/python';
    var runserver = spawn(python, args, {
        stdio: "inherit"
    });
    runserver.on('close', function(code) {
        if (code != 0) {
            util.log(util.colors.red('Django runserver exited with error code: ') + code);
        } else {
            util.log(util.colors.green('Django runserver exited normally.'));
        }
    });*/
}

function rebuild(deploy) {
    checkDevelopment(deploy);
    bundleJS();
    bundleCSS();

    if (options.development) {
        runserver();
    }
}

gulp.task('default', function() {
    rebuild(false);
});

gulp.task('deploy', function() {
    rebuild(true);
});
