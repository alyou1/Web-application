from flask import Blueprint, render_template,url_for,redirect,\
    session,flash
from src.forms import LoginForm
from src.models import Utilisateur,Admin
from src import TEMPLATE_PATH

connexion_view = Blueprint('connexion_view', __name__,
                        template_folder=TEMPLATE_PATH)

@connexion_view.route('/utilisateurs')
def utilisateurs():
    users = Utilisateur.query.all()
    return render_template('utilisateurs.html', utilisateurs=users)

@connexion_view.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin and admin.check_password(form.password.data):
            session['admin'] = admin.username
            return redirect(url_for('index'))
        else:
            flash('Identifiants invalides')
    return render_template('login.html', form=form)

@connexion_view.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('login'))