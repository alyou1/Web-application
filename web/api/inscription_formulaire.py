from flask import Blueprint, render_template,url_for,redirect
from src.forms import UtilisateurForm
from src.models import Utilisateur,db
from src import TEMPLATE_PATH

form_view = Blueprint('form_view', __name__,
                        template_folder=TEMPLATE_PATH)

@form_view.route('/')
def index():
    form = UtilisateurForm()
    if form.validate_on_submit():
        nouveau = Utilisateur(nom=form.nom.data,prenom=form.prenom.data ,email=form.email.data)
        db.session.add(nouveau)
        db.session.commit()
        return redirect(url_for('utilisateurs'))
    return render_template('form.html', form=form)