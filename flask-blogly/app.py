"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, User, Post, Tag, PostTag



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'

db.init_app(app)
connect_db(app)

with app.app_context():
    db.create_all()


@ app.route('/')
def root():
    posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    return render_template('homepage.html', posts=posts)

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('user_list.html', users=users)

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/users/new', methods=['POST'])
def add_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form.get('image_url')

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def user_detail(user_id):
    user = User.query.get(user_id)
    return render_template('user_detail.html', user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    user = User.query.get(user_id)
    return render_template('edit_user.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>/posts/new')
def new_post(user_id):
    user = User.query.get(user_id)
    tags = Tag.query.all()
    return render_template('new_post.html', user=user, tags=tags)

@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def add_post(user_id):
    user = User.query.get_or_404(user_id)
    title = request.form['title']
    content = request.form['content']

    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    tag_ids = [int(tag_id) for tag_id in request.form.getlist('tag_id')]
    if tag_ids:
        tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
        new_post.tags = tags
        db.session.commit()

    flash('Post created successfully', 'success')
    return redirect(f'/users/{user_id}')


@app.route('/posts/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get(post_id)
    return render_template('post_detail.html', post=post)

@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    post = Post.query.get(post_id)
    tags = Tag.query.all()
    return render_template('edit_post.html', post=post, tags=tags)

@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def update_post(post_id):
    post = Post.query.get(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    tag_ids = [int(tag_id) for tag_id in request.form.getlist('tag_id')]
    post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

    db.session.add(post)
    db.session.commit()
    flash('Post updated successfully', 'success')

    return redirect(f'/users/{post.user_id}')

@app.route('/posts/<int:post_id>/delete', methods=['GET', 'POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    flash('Post deleted successfully', 'success')
    return redirect(f'/users/{post.user_id}')

@app.route('/tags')
def tags():
    tags = Tag.query.all()
    return render_template('tag_list.html', tags=tags)

@app.route('/tags/new')
def new_tag():
    posts = Post.query.all()
    return render_template('new_tag.html', posts=posts)

@app.route('/tags/new', methods=['GET','POST'])
def add_tag():
    post_ids = [int(post_id) for post_id in request.form.getlist('post_id')]
    posts = Post.query.filter(Post.id.in_(post_ids)).all()
    new_tag = Tag(name=request.form['name'], posts=posts)

    db.session.add(new_tag)
    db.session.commit()
    flash('Tag created successfully', 'success')

    return redirect('/tags')

@app.route('/tags/<int:tag_id>')
def tag_detail(tag_id):
    tag = Tag.query.get(tag_id)
    return render_template('tag_detail.html', tag=tag)

@app.route('/tags/<int:tag_id>/edit')
def edit_tag(tag_id):
    tag = Tag.query.get(tag_id)
    posts = Post.query.all()
    return render_template('edit_tag.html', tag=tag,  posts=posts)

@app.route('/tags/<int:tag_id>/edit', methods=['POST'])
def update_tag(tag_id):
    tag = Tag.query.get(tag_id)
    tag.name = request.form['name']
    post_ids = [int(post_id) for post_id in request.form.getlist('post_id')]
    tag.posts = Post.query.filter(Post.id.in_(post_ids)).all()

    db.session.add(tag)
    db.session.commit()

    flash('Tag updated successfully', 'success')

    return redirect('/tags')

@app.route('/tags/<int:tag_id>/delete', methods=['GET', 'POST'])
def delete_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()

    flash('Tag deleted successfully', 'success')
    return redirect('/tags')

@app.route('/tags/<int:tag_id>/posts/new')
def new_post_tag(tag_id):
    tag = Tag.query.get(tag_id)
    posts = Post.query.all()
    return render_template('new_post_tag.html', tag=tag, posts=posts)

@app.route('/tags/<int:tag_id>/posts/new', methods=['POST'])
def add_post_tag(tag_id):
    post_id = request.form['post_id']

    post_tag = PostTag(post_id=post_id, tag_id=tag_id)
    db.session.add(post_tag)
    db.session.commit()

    return redirect(f'/tags/{tag_id}')

@app.route('/tags/<int:tag_id>/posts/<int:post_id>/delete', methods=['GET', 'POST'])
def delete_post_tag(tag_id, post_id):
    post_tag = PostTag.query.filter(PostTag.post_id == post_id and PostTag.tag_id == tag_id).first()
    db.session.delete(post_tag)
    db.session.commit()

    return redirect(f'/tags/{tag_id}')







if __name__ == '__main__':
    app.run(debug=True)