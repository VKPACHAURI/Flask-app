from flask import Flask
import os
app=Flask(__name__,static_url_path="")
app.config['SQLALCHEMY_DATABASE_URI']=os.geienv("MYSQL_URL_PATTERN")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False