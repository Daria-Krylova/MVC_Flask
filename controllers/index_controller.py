from flask import Blueprint, render_template
from models.post import Post

index = Blueprint('index', __name__)

@index.route('/')
def show_posts():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)
