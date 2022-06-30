import imp
from flask import render_template, request, send_file
from io import BytesIO
from app import app
from datetime import datetime
import requests
import xmltodict 
from models import *
from form_model import *




@app.route("/")
def index():
    all_stories = Stories.query.all()
    all_news = News.query.limit(3).all()
    date = datetime.now().strftime("%d.%m.%Y")
    r = requests.get(f"https://www.cbar.az/currencies/{date}.xml")
    dict_data = xmltodict.parse(r.content)
    USD_buy = dict_data["ValCurs"]["ValType"][1]["Valute"][0]["Value"]
    EUR_buy = dict_data["ValCurs"]["ValType"][1]["Valute"][1]["Value"]
    USD_sell = float(USD_buy) + 0.0020
    EUR_sell = float(EUR_buy) + 0.0020
    return render_template("index.html", Individiual_active = True, stories = all_stories, all_news = all_news, dollar_buy = USD_buy, euro_buy = EUR_buy, dollar_sell = USD_sell, euro_sell = EUR_sell)

@app.route("/az/news/")
def news():
    all_news = News.query.all()
    return render_template("news.html",  Individiual_active = False, all_news = all_news)
@app.route("/az/news/<slug>")
def news_slug(slug):
    all_news = News.query.all()
    for news in all_news:
        if slug == news.slug:
            news_slug = news
    return render_template("news_slug.html",  Individiual_active = False, the_news = news_slug)

@app.route("/az/individuals/cards/")
def cards():
    r = Cards.query.all()
    all_stories = Stories.query.all()
    return render_template('cards.html', Individiual_active = True , cards = r, stories = all_stories)


@app.route("/az/individuals/cards/<int:id>", methods = ["GET" , "POST"])
def card(id):
    all_stories = Stories.query.all()
    r = Cards.query.filter(Cards.id == id).first()
    post_data = request.form
    order_card_form = OrderCard()
    if request.method == "POST":
        order_card_form = OrderCard(data = post_data)
        file1 = request.files['file1']
        file2 = request.files['file2']
        if order_card_form.validate_on_submit():
            ordered_card = CardOrder(card_id = id,card_type=order_card_form.cardType.data, currency=order_card_form.currency.data, name = order_card_form.name.data, surname = order_card_form.surname.data, prefix=order_card_form.prefix.data, mobile_number = order_card_form.mobile_number.data, secred_word = order_card_form.secret_word.data, branch=order_card_form.branch.data,  filename1 = file1.filename, data1 = file1.read() ,filename2 = file2.filename, data2 = file2.read())
            ordered_card.save()

    return render_template('card.html', form = order_card_form, Individiual_active = True, card = r, id = id, stories = all_stories)



@app.route("/az/individuals/online-services/loan_request",  methods = ["GET" , "POST"])
def onlineCredit():
    all_stories = Stories.query.all()
    post_data = request.form
    order_credit_form = OnlineCreditForm()
    if request.method == "POST":
        order_credit_form = OnlineCreditForm(data = post_data)
        if order_credit_form.validate_on_submit():
            print("second")
            order_credit = OnlineCredit(salary=order_credit_form.salary.data, credit=order_credit_form.credit.data, name = order_credit_form.name.data, work_place = order_credit_form.work_place.data,surname = order_credit_form.surname.data,prefix=order_credit_form.prefix.data, mobile_number = order_credit_form.mobile_number.data)
            order_credit.save()
    return render_template('online-credit.html', form = order_credit_form, Individiual_active = True, stories = all_stories)



@app.route("/az/individuals/deposits/")
def deposit():
    r = Deposits.query.all()
    all_stories = Stories.query.all()
    return render_template('deposits.html', Individiual_active = True , deposits = r, stories = all_stories)
