import sys

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

app = Flask(__name__)
app.config.from_object(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)

PREFIX="/frozenflasktest"

@app.route(PREFIX+'/')
def index():
    return render_template('index.html', pages=flatpages)

@app.route(PREFIX+'/about')
def about():
    skills = {
        "HTML": 90,
        "CSS": 90,
        "JS": 70,
        "Sass": 60
    }
    return render_template('about.html', skills=skills)

@app.route(PREFIX+"/posts/")
def posts():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=False)
    return render_template('posts.html', posts=posts)

@app.route(PREFIX+'/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
      app.run(port=5000)
