from email.policy import default
from multiprocessing.sharedctypes import Value
from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,  IntegerField, RadioField, FileField, IntegerRangeField
from wtforms.validators import DataRequired,  NumberRange


class OrderCard(FlaskForm):
    cardType = SelectField(label = "Kartın növünü seçin", name = "Card_Type", id="inputState", choices= [("", "Kartın növünü seçin"), ("Visa", "Visa"), ("Master card", "Master card")], validators=[DataRequired()])
    currency = RadioField( name = "currency", choices= [("AZN", "Manat"), ("USD", "Dollar"), ("EUR", "Avro")], validators=[DataRequired()])
    name = StringField( name = "name", validators=[DataRequired()], render_kw={'placeholder' : 'Ad'})
    surname = StringField( name = "surname", validators=[DataRequired()], render_kw={'placeholder' : 'Soyad'})
    prefix = SelectField(label = "Prefiks", name = "prefix", choices= [("", "Prefiks"), ("050", "050"), ("051", "051"), ("055", "055") , ("070", "070"), ("077", "077") , ("099", "099") , ("010", "010")], validators=[DataRequired()], render_kw={'placeholder' : 'Prefix'})
    mobile_number = IntegerField(name = "mobile_number", validators=[DataRequired()], render_kw={'placeholder' : 'Mobil nömrə'})
    secret_word = StringField(name = "secret_word", validators=[DataRequired()], render_kw={'placeholder' : 'Kod sözü'})
    branch = SelectField(  name = "branches",choices= [("", "Filial seç"), ("Baş ofis / MXM (20 yanvar m/s)", "Baş ofis / MXM (20 yanvar m/s)"), ("28 May filialı (Qış parkı)", "28 May filialı (Qış parkı)"), ("Filial № 5 (Sahil m/s)", "Filial № 5 (Sahil m/s)") , ("Mərkəz filialı", "Mərkəz filialı"), ("Filial № 11 (Elmlər Akademiyası m/s)", "Filial № 11 (Elmlər Akademiyası m/s)") , ("Filial Nərimanov", "Filial Nərimanov"),("Filial № 4 (Xalqlar Dostluğu m/s)", "Filial № 4 (Xalqlar Dostluğu m/s)"), ("Mərdəkan filialı", "Mərdəkan filialı") , ("Filial Sədərək TM", "Filial Sədərək TM") , ("Filial Sumqayıt", "Filial Sumqayıt") , ("Filial Gəncə", "Filial Gəncə") , ("Filial Bərdə", "Filial Bərdə") , ("Filial Lənkaran", "Filial Lənkaran"), ("Ağcabədi filialı", "Ağcabədi filialı")], validators=[DataRequired()])
    id_front = FileField(label = "Ş.V.-in ön tərəfi",  name = "front_side")
    id_back = FileField(label = "Ş.V.-in ön tərəfi",  name = "back_side" )



class OnlineCreditForm(FlaskForm):
    salary = IntegerRangeField(label = "Aylıq əməkhaqqı", name = "Aylıq əməkhaqqı", default = 2500 ,validators=[DataRequired(), NumberRange(min = 350, max = 5000)], id = "salary_range")
    credit = IntegerRangeField(label = "Kreditin məbləği", name = "Kreditin məbləği",default = 15000 ,validators=[DataRequired(), NumberRange(min = 300, max = 30000)], id = "amount_range")
    name = StringField(label = "name", validators=[DataRequired()], render_kw={'placeholder' : 'Ad'},id="inputEmail4")
    surname = StringField(label = "surname", validators=[DataRequired()], render_kw={'placeholder' : 'Soyad'})
    work_place = StringField(label = "Work Place", validators=[DataRequired()], render_kw={'placeholder' : 'İş yeri'})
    prefix = SelectField(label = "Prefix", choices= [("", "Prefiks"), ("050", "050"), ("051", "051"), ("055", "055") , ("070", "070"), ("077", "077") , ("099", "099") , ("010", "010")], validators=[DataRequired()], render_kw={'placeholder' : 'Prefix'})
    mobile_number = IntegerField(label = "mobile number", validators=[DataRequired()], render_kw={'placeholder' : 'Mobil Nömrə'})