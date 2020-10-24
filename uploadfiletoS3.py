from flask import Flask
from flask_s3 import FlaskS3
import flask_s3


app = Flask(__name__)
app.config['FLASKS3_BUCKET_NAME'] = 'users12'
s3 = FlaskS3(app)

flask_s3.create_all(app)


