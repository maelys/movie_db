from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms import validators
from wtforms.validators import Required

class AnaelleRateForm(Form):
    rate = TextField('my_rating',validators = [Required()])
