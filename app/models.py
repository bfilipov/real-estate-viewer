from app import db


class ListingModel(db.Model):
    """Sqlalchemy products model"""
    __tablename__ = "items"

    item_id = db.Column('item_id', db.String, primary_key=True)
    start_price = db.Column('start_price', db.Float)
    start_price_per_sm = db.Column('start_price_per_sm', db.Float)
    category = db.Column('category', db.String)
    size = db.Column('size', db.String)
    size_int = db.Column('size_int', db.String)
    size_recalc = db.Column('size_recalc', db.Integer)
    city = db.Column('city', db.String)
    district = db.Column('district', db.String)
    address = db.Column('address', db.String)
    izpalnitel = db.Column('izpalnitel', db.String)
    published_on = db.Column('published_on', db.DateTime)
    period = db.Column('period', db.String)
    start_period = db.Column('start_period', db.DateTime)
    end_period = db.Column('end_period', db.DateTime)
    auction_on = db.Column('auction_on', db.DateTime)
    documents = db.Column('documents', db.ARRAY(db.String))
    url = db.Column('url', db.String)
    article_id = db.Column('article_id', db.String)
    description = db.Column('description', db.String)
    timestamp = db.Column('timestamp', db.DateTime)
    images = db.Column('images', db.ARRAY(db.String))
    crawler = db.Column('crawler', db.String)
    has_description = db.Column('has_description', db.Integer)
    has_fraction = db.Column('has_fraction', db.Integer)
