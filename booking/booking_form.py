from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, DateField, BooleanField
from wtforms.validators import Length, DataRequired


class CreateBookingForm(FlaskForm):
    booking_date = DateField(label='Enter booking date:', validators=[DataRequired()])
    vehicle_registration_no = StringField(label='Enter vehicle registration number:',
                                          validators=[Length(min=2, max=50), DataRequired()])
    frame_no = SelectField(label='Enter frame number:',
                           validate_choice=False, choices=[])
    customer_no = SelectField(label='Enter customer number:', validate_choice=False, choices=[])
    # status = StringField(label='Status:', render_kw={'readonly': True}, validators=[DataRequired()])
    # status = SelectField(label='Select status:', render_kw={'readonly': True}, choices=["Open", "Cancel", "Completed"],
    #                      validators=[DataRequired()])
    rc_issue_date = DateField(label='RC issue date:', validators=[DataRequired()])
    delivery_date = DateField(label='Delivery date:', validators=[DataRequired()])
    tools = BooleanField(label='Tools:')
    helmet = BooleanField(label='Helmet:')
    accessories = BooleanField(label='Accessories:')
    description = StringField(label='Enter description:', validators=[Length(min=2, max=100)])
    vehicle_type = StringField(label='Enter vehicle type:', validators=[Length(min=2, max=60)])
    comments = TextAreaField(label='Enter comments:', validators=[Length(min=2, max=250)])
    GST = StringField(label='Enter GST:', validators=[Length(min=2, max=60)])
    delivery_chellan_no = StringField(label='Enter delivery chellan number:',
                                      validators=[Length(min=2, max=50), DataRequired()])
    registration_date = DateField(label='Registration date:', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class EditBookingForm(FlaskForm):
    booking_date = DateField(label='Enter booking date:', validators=[DataRequired()])
    vehicle_registration_no = StringField(label='Enter vehicle registration number:',
                                          validators=[Length(min=2, max=50), DataRequired()])
    frame_no = SelectField(label='Enter frame number:',
                           validate_choice=False, choices=[])
    customer_no = SelectField(label='Enter customer number:', validate_choice=False, choices=[])
    # status = StringField(label='Status:', render_kw={'readonly': True}, validators=[DataRequired()])
    status = SelectField(label='Select status:', choices=["Open", "Cancel", "Completed"],
                         validators=[DataRequired()])
    rc_issue_date = DateField(label='RC issue date:', validators=[DataRequired()])
    delivery_date = DateField(label='Delivery date:', validators=[DataRequired()])
    tools = BooleanField(label='Tools:')
    helmet = BooleanField(label='Helmet:')
    accessories = BooleanField(label='Accessories:')
    description = StringField(label='Enter description:', validators=[Length(min=2, max=100)])
    vehicle_type = StringField(label='Enter vehicle type:', validators=[Length(min=2, max=60)])
    comments = TextAreaField(label='Enter comments:', validators=[Length(min=2, max=250)])
    GST = StringField(label='Enter GST:', validators=[Length(min=2, max=60)])
    delivery_chellan_no = StringField(label='Enter delivery chellan number:',
                                      validators=[Length(min=2, max=50), DataRequired()])
    registration_date = DateField(label='Registration date:')
    submit = SubmitField(label='Submit')
