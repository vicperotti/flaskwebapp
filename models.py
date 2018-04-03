from letsgetcharmed import db


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(512), index=True)
    author = db.Column(db.String(120), index=True)
    image = db.Column(db.String(256), index=True)

#    def __init__(self, quote,author,image):
#        self.quote = quote
#        self.author = author
#        self.image = image

    def __repr__(self):
        return '<A quote by...%r>' % (self.author)
