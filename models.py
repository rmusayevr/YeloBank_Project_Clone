from extensions import *
from flask_admin.contrib.sqla import ModelView


class News(db.Model):
    __tablename__ = "News"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    slug = db.Column(db.String(255), nullable = False)
    date = db.Column(db.String(40), nullable = False)
    description = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return self.title
    
    def __init__(self, title, slug, date, description):
        self.title = title
        self.slug = slug
        self.date = date
        self.description = description

    def save(self):
        db.session.add(self)
        db.session.commit()

admin.add_view(ModelView(News, db.session))


class Stories(db.Model):
    __tablename__ = "Stories"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    img = db.Column(db.String(255), nullable = False)
    description = db.Column(db.Text, nullable = False)
    text_bg = db.Column(db.String(50), nullable = False)
    text = db.Column(db.String(50), nullable = False)

    def __repr__(self):
        return self.title
    
    def __init__(self, title, img, description, text_bg, text):
        self.title = title
        self.img = img
        self.description = description
        self.text_bg = text_bg
        self.text = text
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
admin.add_view(ModelView(Stories, db.session))
    
class Cards(db.Model):
        __tablename__ = "Cards"
        id = db.Column(db.Integer, primary_key = True)
        card_img = db.Column(db.Text)
        card_name = db.Column(db.String(50))
        description = db.Column(db.Text)
        duration = db.Column(db.String(40), default = "Müddət")
        duration_v = db.Column(db.String(50))
        currency = db.Column(db.String(50), default = "Valyuta")
        currency_v = db.Column(db.String(50))
        cahsback =  db.Column(db.String(50), default = "Cashback")
        cashback_v = db.Column(db.String(255), nullable=False)
        card_detail = db.Column(db.Text)
        

        def __repr__(self):
            return self.card_name

        def __init__(self,card_img, card_name, description, duration_v, currency_v, cashback_v, duration=None, currency=None, cashback=None):
            self.card_img = card_img
            self.card_name = card_name
            self.description = description
            self.duration = duration
            self.duration_v = duration_v
            self.currency = currency
            self.currency_v = currency_v
            self.cashback = cashback
            self.cashback_v = cashback_v

        def save(self):
            db.session.add(self)
            db.session.commit()

class Deposits(db.Model):
        __tablename__ = "Deposits"
        id = db.Column(db.Integer, primary_key = True)
        deposit_img = db.Column(db.Text)
        deposit_name = db.Column(db.String(50))
        description = db.Column(db.Text)
        amount = db.Column(db.String(40), default = "Məbləğ")
        amount_v = db.Column(db.String(50))
        durration = db.Column(db.String(50), default = "Valyuta")
        durration_v = db.Column(db.String(50))
        percentage_pay =  db.Column(db.String(50), default = "Cashback")
        percentage_pay_v = db.Column(db.String(255), nullable=False)

        def __repr__(self):
            return self.deposit_name

        def __init__(self,deposit_img, deposit_name, description, amount_v, durration_v, percentage_pay_v, amount=None, durration=None, percentage_pay=None):
            self.deposit_img = deposit_img
            self.deposit_name = deposit_name
            self.description = description
            self.amount = amount
            self.amount_v = amount_v
            self.durration = durration
            self.durration_v = durration_v
            self.percentage_pay = percentage_pay
            self.percentage_pay_v = percentage_pay_v

        def save(self):
            db.session.add(self)
            db.session.commit()

class CardOrder(db.Model):
    __tablename__ = "CardOrder"
    id = db.Column(db.Integer, primary_key = True)
    card_type = db.Column(db.String(30), nullable = False)
    currency = db.Column(db.String(20), nullable = False)
    name = db.Column(db.String(30), nullable = False)
    surname =  db.Column(db.String(30), nullable = False)
    prefix = db.Column(db.String(3), nullable = False)
    mobile_number = db.Column(db.String(7), nullable = False)
    secred_word = db.Column(db.String(30), nullable = False)
    branch = db.Column(db.String(100), nullable = False)
    filename1 = db.Column(db.String(50))
    data1 = db.Column(db.LargeBinary)
    filename2 = db.Column(db.String(50))
    data2 = db.Column(db.LargeBinary)
    card_id = db.Column(db.Integer, db.ForeignKey("Cards.id"))
    

    def __repr__(self):
            return self.name

    def __init__(self, card_type,currency,name, surname, prefix, mobile_number, secred_word, branch,filename1, data1, filename2, data2, card_id ):
        self.card_type = card_type
        self.currency = currency
        self.name = name
        self.surname = surname
        self.prefix = prefix
        self.mobile_number = mobile_number
        self.secred_word = secred_word
        self.branch = branch
        self.filename1 = filename1
        self.data1 = data1
        self.filename2 = filename2
        self.data2 = data2
        self.card_id = card_id

    def save(self):
        db.session.add(self)
        db.session.commit()

class OnlineCredit(db.Model):
    __tablename__ = "OnlineCredit"
    id = db.Column(db.Integer, primary_key = True)
    salary = db.Column(db.Integer, nullable = False )
    credit = db.Column(db.Integer, nullable = False )
    name = db.Column(db.String(30), nullable = False)
    surname =  db.Column(db.String(30), nullable = False)
    work_place = db.Column(db.Text)
    prefix = db.Column(db.String(3), nullable = False)
    mobile_number = db.Column(db.String(7), nullable = False)

    def __repr__(self):
            return self.name

    def __init__(self, salary, credit, name, surname, work_place, prefix, mobile_number):
        self.salary = salary
        self.credit = credit
        self.name = name
        self.surname = surname
        self.work_place = work_place
        self.prefix = prefix
        self.mobile_number = mobile_number
            
        
    def save(self):
        db.session.add(self)
        db.session.commit()

# class Upload(db.Model):
#     __tablename__ = "Upload"
#     id = db.Column(db.Integer, primary_key = True)
    

admin.add_view(ModelView(OnlineCredit, db.session))
admin.add_view(ModelView(CardOrder, db.session))
admin.add_view(ModelView(Deposits, db.session))
admin.add_view(ModelView(Cards, db.session))