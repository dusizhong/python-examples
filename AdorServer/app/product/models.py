from .. import db

class Product(db.Model):

    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    title = db.Column(db.String(40), nullable=False)
    desc = db.Column(db.String(100))
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())