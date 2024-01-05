from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def root():

    return redirect("/users")

@app.route('/users')
def user_index():

    users = User.query.order_by(User.last_name, User.frist_name).all()
    return render_template('/users/index.html', users=users)

@app.route("/users", ["GET"])
def new_user(): 

  return render_template('/users/index.html')

@app.route("/users", ["POST"])
def post_user():
    new_user = User(
        first_name=request.from['First']
        last_name=request.from['Last']
       image_url=request.from['image'] or None )

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

    @app.route('/users/<int:user_id>')
    def show_users(user_id):
        user = user.query.get_or_404(user_id)
        return render_template('/user/show.html', user=user)
    
    @app.route('/user/<int:user_id>/edit', methods=["POST"])
    def edit_user(user_id):
        user = user.query.get_or_404(user_id)
        return render_template('/user/edit.html', user=user)

    @app.route('/user/<int:user_id>/edit', methods=["POST"])
    def post_edit(user_id):
        user = user.query.get_or_404(user_id)
        user.first = request.form['First']
        user.last = request.form['Last']
        user.image_url = request.form['Image']
    
        db.session.add(user)
        db.session.commit()
        return redirect("/users")

    @app.route('/users/<int:user_id>/delete', methods=["POST"])
    def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return redirect("/users")