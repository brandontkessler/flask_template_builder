from flask import render_template, Blueprint
from flask_login import login_required
from app.decorators import check_confirmed

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route("/secret")
@login_required
@check_confirmed
def secret():
    return "SECRET PAGE"


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', e=e), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


@main.app_errorhandler(403)
def page_not_found(e):
    return render_template('errors/403.html'), 403
