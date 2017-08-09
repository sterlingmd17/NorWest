from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def index():
    continue

if __name__ == '__main__':
    app.run()
