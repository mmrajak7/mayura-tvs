from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Length, DataRequired


class CreateVehicleForm(FlaskForm):
    engine_no = StringField(label='Enter engine no:', validators=[Length(min=2, max=100), DataRequired()])
    dealer = StringField(label='Enter dealer:', validators=[Length(min=2, max=100), DataRequired()])
    delivery_chellan_no = StringField(label='Enter delivery chellan number:',
                                       validators=[Length(min=2, max=50), DataRequired()])
    # status = SelectField(label='Select status:', choices=["Available", "Register-completed"],
    #                      validators=[DataRequired()])
    description = StringField(label='Enter description:', validators=[Length(min=2, max=100)])
    model = StringField(label='Enter model:', validators=[Length(min=2, max=60)])
    comments = TextAreaField(label='Enter comments:', validators=[Length(min=2, max=250)])
    GST = StringField(label='Enter GST:', validators=[Length(min=2, max=60)])
    vehicle_type = StringField(label='Enter vehicle type:', validators=[Length(min=2, max=60)])
    submit = SubmitField(label='Submit')


class UpdateVehicleForm(FlaskForm):
    engine_no = StringField(label='Enter engine no:', render_kw={'readonly': True},
                            validators=[Length(min=2, max=100), DataRequired()])
    dealer = StringField(label='Enter dealer:', validators=[Length(min=2, max=100), DataRequired()])
    delivery_chellan_no = StringField(label='Enter delivery chellan number:',
                                       validators=[Length(min=2, max=50), DataRequired()])
    status = SelectField(label='Select status:', choices=["Available", "Booked", "Register-completed", "Delivered"],
                         validators=[DataRequired()])
    description = StringField(label='Enter description:', validators=[Length(min=2, max=100)])
    model = StringField(label='Enter model:', validators=[Length(min=2, max=60)])
    comments = TextAreaField(label='Enter comments:', validators=[Length(min=2, max=250)])
    GST = StringField(label='Enter GST:', validators=[Length(min=2, max=60)])
    vehicle_type = StringField(label='Enter vehicle type:', validators=[Length(min=2, max=60)])
    submit = SubmitField(label='Submit')
