import os
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import string
import webbrowser



app = Flask(__name__)
####################################################### step-1
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
Migrate(app,db)
##################### create a model ############################
class surl(db.Model):
    __tablename__ = 'bantu'
    id = db.Column(db.Integer, primary_key = True)
    original_url = db.Column(db.Text)
    short_text = db.Column(db.Text)


    def __init__(self,original_url,short_text):
        self.original_url = original_url
        self.short_text = short_text
    def __repr__(self):
        return "{} and https://x.urls/{}".format(self.original_url,self.short_text)
    


#################################################################
@app.route('/',methods = ["GET","POST"])
def homepage():
    if request.method == "POST":
        url = request.form['in_1']
        N=8
        res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
        new_surl = surl(url,res)
        db.session.add(new_surl)
        db.session.commit()
        return render_template("index2.html",linkk=res,url=url)
    return render_template("index.html")


@app.route('/history')
def history():
    sab = surl.query.all()
    return render_template('history.html',urls = sab)

@app.route('/<path:Number>')
def droute(Number):
    x1 = surl.query.filter_by(short_text = Number).first()
    x2 = str(x1)
    a = x2.split(' and ')
    return str(webbrowser.open(a[0]))

#####################################################################
if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)
