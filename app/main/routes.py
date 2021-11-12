from datetime import date

from flask import render_template, request
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import or_

from app import db, login
from app.models import ListingModel
from app.main import bp

ROWS_PER_PAGE = 50


@login.user_loader
def load_user(_id):
    return None


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')


@bp.route('/imoti')
def imoti():
    # Set the pagination configuration
    page = request.args.get('page', 1, type=int)
    imoti = ListingModel.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template('imoti.html', imoti=imoti)


@bp.route('/zemq')
def zemq():
    # Set the pagination configuration
    sql_query = """ select start_price, (case when size_recalc is null then size_int else size_recalc::float end)/1000 as dkr_recalc, 
                            size, floor((start_price_per_sm * 1000)) as per_dekar, url,  city, district, end_period, published_on, category, 
                            description from items
                        where (description like '%%емеделска земя%%' or 
                               category like '%%земя%%')   
                               and not 
                               (description like '%%залесена%%' or 
                                description like '%%горска%%')
                        and end_period >= NOW() - INTERVAL '1 DAY'
                     order by end_period, start_price_per_sm asc"""

    page = request.args.get('page', 1, type=int)
    imoti = ListingModel.query\
        .filter(or_(ListingModel.description.like('%емеделска земя%'), ListingModel.category.like('%земя%')))\
        .filter(or_(ListingModel.category.notlike('%залесена%'), ListingModel.category.notlike('%горска%'))) \
        .filter(ListingModel.end_period >= date.today()) \
        .order_by(ListingModel.end_period) \
        .order_by(ListingModel.start_price) \
        .paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template('imoti.html', imoti=imoti, type='zemq')
