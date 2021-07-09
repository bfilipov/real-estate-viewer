from app import app, login
from flask import render_template, request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import ListingModel

@login.user_loader
def load_user(id):
    return None

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/imoti')
def imoti():
    ROWS_PER_PAGE = 50
    # Set the pagination configuration
    page = request.args.get('page', 1, type=int)
    imoti = ListingModel.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template('imoti.html', imoti=imoti)
