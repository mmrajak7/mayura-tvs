from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Length, DataRequired


class CreateVehicleForm(FlaskForm):
    engine_no = StringField(label='Engine no:', validators=[Length(min=2, max=100), DataRequired()])
    dealer = StringField(label='Dealer:', validators=[Length(min=2, max=100), DataRequired()])
    delivery_chellan_no = StringField(label='Delivery chellan number:',
                                       validators=[Length(min=2, max=50), DataRequired()])
    status = SelectField(label='Select status:', choices=["Available", "Booked", "Register-completed", "Delivered"],
                         validators=[DataRequired()])
    description = StringField(label='Description:', validators=[Length(min=2, max=100)])
    model = StringField(label='Model:', validators=[Length(min=2, max=60)])
    comments = TextAreaField(label='Comments:', validators=[Length(min=2, max=250)])
    GST = StringField(label='GST:', validators=[Length(min=2, max=60)])
    vehicle_type = StringField(label='Vehicle type:', validators=[Length(min=2, max=60)])
    submit = SubmitField(label='Submit')


class UpdateVehicleForm(FlaskForm):
    engine_no = StringField(label='Engine no:', render_kw={'readonly': True},
                            validators=[Length(min=2, max=100), DataRequired()])
    dealer = StringField(label='Dealer:', validators=[Length(min=2, max=100), DataRequired()])
    delivery_chellan_no = StringField(label='Delivery chellan number:',
                                       validators=[Length(min=2, max=50), DataRequired()])
    status = SelectField(label='Select status:', choices=["Available", "Booked", "Register-completed", "Delivered"],
                         validators=[DataRequired()])
    description = StringField(label='Description:', validators=[Length(min=2, max=100)])
    model = StringField(label='Model:', validators=[Length(min=2, max=60)])
    comments = TextAreaField(label='Comments:', validators=[Length(min=2, max=250)])
    GST = StringField(label='GST:', validators=[Length(min=2, max=60)])
    vehicle_type = StringField(label='Vehicle type:', validators=[Length(min=2, max=60)])
    submit = SubmitField(label='Submit')
