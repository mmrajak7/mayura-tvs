from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, TextAreaField
from wtforms.validators import Length, Email, DataRequired


class CreateCustomerForm(FlaskForm):
    customer_name = StringField(label='Customer Name:', validators=[Length(min=2, max=50), DataRequired()])
    email = StringField(label='Enter email:', validators=[Length(min=2, max=50), Email(), DataRequired()])
    dob = DateField(label='Date of birth:', validators=[DataRequired()])
    mobile1 = IntegerField(label='Enter primary mobile number:', validators=[DataRequired()])
    mobile2 = IntegerField(label='Enter secondary mobile number:')
    mobile3 = IntegerField(label='Enter alternate mobile number:')
    comment = TextAreaField(label='Enter comment:', validators=[Length(min=2, max=250)])
    GST = StringField(label='Enter GST:', validators=[Length(min=2, max=60)])
    city = StringField(label='Enter city:', validators=[Length(min=2, max=60)])
    street = StringField(label='Enter street:', validators=[Length(min=2, max=60)])
    pincode = StringField(label='Enter pincode:', validators=[Length(min=2, max=60)])
    submit = SubmitField(label='Submit')


class UpdateCustomerForm(FlaskForm):
    customer_name = StringField(label='Customer Name:', render_kw={'readonly': True}, validators=[Length(min=2, max=50), DataRequired()])
    email = StringField(label='Enter email:', validators=[Length(min=2, max=50), Email(), DataRequired()])
    dob = DateField(label='Date of birth:', validators=[DataRequired()])
    mobile1 = IntegerField(label='Enter primary mobile number:', validators=[DataRequired()])
    mobile2 = IntegerField(label='Enter secondary mobile number:')
    mobile3 = IntegerField(label='Enter alternate mobile number:')
    comment = TextAreaField(label='Enter comment:', validators=[Length(min=2, max=250)])
    GST = StringField(label='Enter GST:', validators=[Length(min=2, max=60)])
    city = StringField(label='Enter city:', validators=[Length(min=2, max=60)])
    street = StringField(label='Enter street:', validators=[Length(min=2, max=60)])
    pincode = StringField(label='Enter pincode:', validators=[Length(min=2, max=60)])
    submit = SubmitField(label='Submit')
