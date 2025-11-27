from flask import Flask, render_template, url_for, flash, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from models import db, User, Post
from forms import RegisterForm, LoginForm, PostForm, DeleteForm
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'secretkey123'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    # Loads the user from the database using the stored session user_id
    return User.query.get(int(user_id))

@app.route('/')
def index():
    # Display posts ordered by newest first
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        # Check if username already exists
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already taken. Choose another.', 'danger')
        else:
            # Create new user
            new_user = User(username=form.username.data)
            new_user.set_password(form.password.data)  # Hash the password
            db.session.add(new_user)
            try:
                db.session.commit()  # Try saving to DB
            except IntegrityError:
                db.session.rollback()  # Roll back if DB error occurs
                flash('Database error — please try again.', 'danger')
            else:
                flash(f'Registration successful for {form.username.data}!', 'success')
                return redirect(url_for('index'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        # Check if username exists
        if not User.query.filter_by(username=form.username.data).first():
            flash('Username does not exists. Please try again.', 'danger')
        else:
            user = User.query.filter_by(username=form.username.data).first()

            # Validate password hash
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)  # Log user in
                flash('Successfully logged in', 'success')
                return redirect(url_for('index'))

            flash('Wrong password. Please try again.', 'danger')

    return render_template('login.html', form=form)

@app.route('/logout', methods = ['GET'])
@login_required
def logout():
    logout_user()  # End session
    flash('You just logged out.')
    return redirect(url_for('index'))

@app.route('/post', methods=['GET', 'POST'])
@login_required
def add_post():
    form = PostForm()

    if form.validate_on_submit():
        # Create new post with current_user.id
        post = Post(title=form.title.data, body=form.body.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Blog post submitted successfully.', 'success')
        return redirect(url_for('index'))

    return render_template('add_post.html', form=form)

@app.route('/delete/<int:post_id>', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    # Fetch post or show 404
    post = Post.query.get_or_404(post_id)
    form = DeleteForm()

    # Prevent deleting others' posts
    if current_user.id != post.user_id:
        flash('You can only delete your own posts!', 'danger')
        return redirect(url_for('index'))

    # Form must be POST + validated
    if form.validate_on_submit():
        db.session.delete(post)  # Delete the post
        db.session.commit()
        flash('Post deleted successfully!', 'success')
        return redirect(url_for('index'))

    # Render confirmation page
    return render_template('delete_post.html', form=form, post=post)

with app.app_context():
    db.create_all()  # Create tables if not existing

if __name__ == "__main__":
    app.run(debug=True)
