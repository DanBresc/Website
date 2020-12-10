from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy as SQLA
#from flask_bootstrap import Bootstrap

app = Flask(__name__) #__name__ points to the program that is running it 
#MAKE THIS SQL SHIZNATCHIN WORK
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

app.config.from_object(Config)

#db = SQLA(app)
'''
class UserColor(db.Model): #move this to its own package
    name = db.Column(db.String(80), unique = True, nullable = False)
    favColor = db.Column(db.String(80), unique = True, nullable = False)
    
    def __repr___(self):
        return '<User %r>' %self.name
'''
#CSS BOOTSTAP FRAMEWORK

from app import routes
#bootstrap = Bootstrap(app)
