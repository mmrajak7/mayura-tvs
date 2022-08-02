from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, TextAreaField
from wtforms.validators import Length, Email, DataRequired


class CreateCustomerForm(FlaskForm):
    customer_name = StringField(label='Customer Name:', validators=[Length(min=2, max=50), DataRequired()])
    email = StringField(label='Email:', validators=[Length(min=2, max=50), Email(), DataRequired()])
    dob = DateField(label='Date of birth:', validators=[DataRequired()])
    mobile1 = IntegerField(label='Primary mobile number:', validators=[DataRequired()])
    mobile2 = IntegerField(label='Secondary mobile number:')
    mobile3 = IntegerField(label='Alternate mobile number:')
    comment = TextAreaField(label='Comment:', validators=[Length(min=2, max=250)])
    GST = StringField(label='GST:', validators=[Length(min=2, max=60)])
    city = StringField(label='City:', validators=[Length(min=2, max=60)])
    street = StringField(label='Street:', validators=[Length(min=2, max=60)])
    pincode = StringField(label='Pincode:', validators=[Length(min=2, max=60)])
    submit = SubmitField(label='Submit')


class UpdateCustomerForm(FlaskForm):
    customer_name = StringField(label='Customer Name:', render_kw={'readonly': True}, validators=[Length(min=2, max=50), DataRequired()])
    email = StringField(label='Enter email:', validators=[Length(min=2, max=50), Email(), DataRequired()])
    dob = DateField(label='Date of birth:', validators=[DataRequired()])
    mobile1 = IntegerField(label='Primary mobile number:', validators=[DataRequired()])
    mobile2 = IntegerField(label='Secondary mobile number:')
    mobile3 = IntegerField(label='Alternate mobile number:')
    comment = TextAreaField(label='Comment:', validators=[Length(min=2, max=250)])
    GST = StringField(label='GST:', validators=[Length(min=2, max=60)])
    city = StringField(label='City:', validators=[Length(min=2, max=60)])
    street = StringField(label='Street:', validators=[Length(min=2, max=60)])
    pincode = StringField(label='Pincode:', validators=[Length(min=2, max=60)])
    submit = SubmitField(label='Submit')
