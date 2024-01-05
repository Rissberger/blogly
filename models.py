"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DEFAULT_URL = "https://1drv.ms/i/s!AtpDfDgD9bZlg6w6PMzrwQpERDQEDA?e=hmslim"

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)  
    last_name = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=True, default=DEFAULT_URL)
    
    @property
    def first_name(self):
        return f"{self.First} {self.Last}"



    def connect_db(app):

        db.app = app
        db.init_app(app)
        