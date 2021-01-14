from werkzeug.urls import url_parse
from flask_login import LoginManager
from flask import Flask, render_template,redirect,url_for,flash
import os
from models import User,users
from form import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "SAzadsfsadfsadfsgsfsdghe3r234ty3yhrg34y4dvgsdfhweqrt23463ergwr2u"
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)



