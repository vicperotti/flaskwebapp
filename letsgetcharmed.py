from flask import Flask, flash, redirect, render_template, request, session, abort
import models
from config import Config
from flask_sqlalchemy import SQLAlchemy
from forms import AddQuoteForm

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route("/")
def index():
    return redirect('/quotelist')

@app.route('/addquote', methods=['GET', 'POST'])
def addquote():
    theform = AddQuoteForm()
    if theform.validate_on_submit():
        flash('OH! You entered..."%s", post=%s' %
              (theform.author.data, theform.quote.data))
        q = models.Quote(author=theform.author.data,quote=theform.quote.data,image=theform.image.data)
        db.session.add(q)
        db.session.commit()
        return redirect('/quotelist')
    return render_template('addquote.html', title='Add a Quote', form=theform)

#@app.route("/hello/<string:name>")
@app.route("/quotelist")
def hello():
#    return name
#    q1 = Quote("'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.'", "John Louis von Neumann","a2849481626_16.jpg")
#    q2 = Quote("'Computer science is no more about computers than astronomy is about telescopes'", "Edsger Dijkstra","Edsger_Wybe_Dijkstra.jpg")
#    q3 = Quote("'To understand recursion you must first understand recursion..'","Unknown","unknown.png")
#    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
#               "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
#               "'To understand recursion you must first understand recursion..' -- Unknown",
#               "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
#               "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
#               "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
#    quotelist = [q1,q2,q3]
#    randomNumber = randint(0,len(quotelist)-1)
#    quote = quotelist[randomNumber]
    query = models.Quote.query.all()

    return render_template(
        'test.html',**locals())

@app.route("/detail/<int:theid>/")
def detail(theid):
    query = models.Quote.query.filter_by(id=theid)
    return render_template(
        'detail.html',**locals())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
