from flask import render_template, Blueprint, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user

from app import db
from booking.booking_form import CreateBookingForm, EditBookingForm
from models.booking import Booking
from models.customer import Customer
from models.vehicle import Vehicle

booking = Blueprint("booking", __name__, static_folder="static", template_folder="templates")


@booking.route('/')
@login_required
def view_booking():
    return render_template('booking.html')


@booking.route('/data', methods=["GET"])
@login_required
def view_booking_data():
    query = Booking.query

    # search filter
    search = request.args.get('search')
    if search:
        query = query(db.joinedload(Booking.customer_no)).filter(db.or_(
            Booking.booking_no.like(f'%{search}%'),
            Booking.model.like(f'%{search}%'),
            Booking.frame_no.like(f'%{search}%'),
            Booking.status.like(f'%{search}%'),
        ))
    total = query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['booking_no', 'model', 'frame_no', 'status']:
                name = 'booking_no'
            col = getattr(Booking, name)
            if direction == '-':
                col = col.desc()
            order.append(col)
        if order:
            query = query.order_by(*order)
    else:
        query = query.order_by(Booking.booking_no.desc())

    # pagination
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query.offset(start).limit(length)
    query.options(db.joinedload(Booking.customer_no))
    print(query)
    return {
        'data': [bookings.to_dict() for bookings in query],
        'total': total,
    }


@booking.route('/create', methods=['GET', 'POST'])
@login_required
def create_booking():
    print("Entered create booking")
    booking_form = CreateBookingForm()
    if booking_form.validate_on_submit():
        print("Entered booking submit")
        frame_no_array = booking_form.frame_no.data.split("-")
        vehicle_by_id = Vehicle.query.filter_by(frame_no=frame_no_array[0]).first()
        booking_to_create = Booking(booking_date=booking_form.booking_date.data,
                                    accessories=booking_form.accessories.data,
                                    delivery_chellan_no=booking_form.delivery_chellan_no.data,
                                    description=booking_form.description.data,
                                    delivery_date=booking_form.delivery_date.data,
                                    # exchange_vehicle_frame_no=booking_form.exchange_vehicle_frame_no.data,
                                    frame_no=frame_no_array[0],
                                    dealer=frame_no_array[2],
                                    customer_no=booking_form.customer_no.data,
                                    status="Open",
                                    model=frame_no_array[1],
                                    comments=booking_form.comments.data,
                                    GST=booking_form.GST.data,
                                    vehicle_type=booking_form.vehicle_type.data,
                                    helmet=booking_form.helmet.data,
                                    # invoice_no=booking_form.invoice_no.data,
                                    rc_issue_date=booking_form.rc_issue_date.data,
                                    tools=booking_form.tools.data,
                                    vehicle_registration_no=booking_form.vehicle_registration_no.data,
                                    last_updated_by=current_user.id()
                                    )
        print(booking_to_create)
        db.session.add(booking_to_create)
        vehicle_by_id.status = "Booked"
        db.session.commit()
        flash(f'Booking {booking_to_create.booking_no} created successfully!', category='success')
        return redirect(url_for("booking.view_booking"))
    print("render create booking.html")
    return render_template('create_booking.html', form=booking_form)


@booking.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_booking(id):
    print("Entered update vehicle")
    update_booking_form = EditBookingForm()
    booking_by_id = Booking.query.filter_by(booking_no=id).first()
    if update_booking_form.validate_on_submit():
        frame_no_array = update_booking_form.frame_no.data.split("-")
        booking_by_id.booking_date = update_booking_form.booking_date.data
        booking_by_id.customer_no = update_booking_form.customer_no.data
        booking_by_id.vehicle_registration_no = update_booking_form.vehicle_registration_no.data
        booking_by_id.accessories = update_booking_form.accessories.data
        booking_by_id.helmet = update_booking_form.helmet.data
        booking_by_id.tools = update_booking_form.tools.data
        booking_by_id.delivery_chellan_no = update_booking_form.delivery_chellan_no.data
        booking_by_id.description = update_booking_form.description.data
        booking_by_id.frame_no = frame_no_array[0]
        booking_by_id.model = frame_no_array[1]
        booking_by_id.dealer = frame_no_array[2]
        booking_by_id.comments = update_booking_form.comments.data
        booking_by_id.vehicle_type = update_booking_form.vehicle_type.data
        booking_by_id.GST = update_booking_form.GST.data
        booking_by_id.status = update_booking_form.status.data
        booking_by_id.delivery_date = update_booking_form.delivery_date.data
        booking_by_id.rc_issue_date = update_booking_form.rc_issue_date.data
        booking_by_id.last_updated_by = current_user.id()
        booking_by_id.registration_date = update_booking_form.registration_date.data
        db.session.commit()
        flash(f'Booking {id} updated successfully!', category='success')
        return redirect(url_for("booking.view_booking"))
    update_booking_form.booking_date.data = booking_by_id.booking_date
    update_booking_form.vehicle_registration_no.data = booking_by_id.vehicle_registration_no
    update_booking_form.accessories.data = booking_by_id.accessories
    update_booking_form.helmet.data = booking_by_id.helmet
    update_booking_form.tools.data = booking_by_id.tools
    update_booking_form.delivery_chellan_no.data = booking_by_id.delivery_chellan_no
    update_booking_form.description.data = booking_by_id.description
    update_booking_form.comments.data = booking_by_id.comments
    update_booking_form.vehicle_type.data = booking_by_id.vehicle_type
    update_booking_form.GST.data = booking_by_id.GST
    update_booking_form.status.data = booking_by_id.status
    update_booking_form.delivery_date.data = booking_by_id.delivery_date
    update_booking_form.rc_issue_date.data = booking_by_id.rc_issue_date
    update_booking_form.registration_date.data = booking_by_id.registration_date
    return render_template('edit_booking.html', form=update_booking_form, customer_no=booking_by_id.customer_no,
                           frame_no=str(booking_by_id.frame_no) + "-" + str(
                               booking_by_id.model) + "-" + booking_by_id.dealer)


@booking.route('/delete/<int:id>', methods=["GET"])
@login_required
def delete_booking(id):
    print("Entered delete vehicle")
    try:
        Booking.query.filter(Booking.booking_no == id).delete()
        db.session.commit()
        flash(f'Booking {id} deleted successfully!', category='success')
    except Exception as e:
        print(e)
        flash(f'Vehicle {id} deletion failed!Message: {e.__cause__}', category='danger')
    return redirect(url_for("booking.view_booking"))


@booking.route('/cancel/<int:id>', methods=["GET"])
@login_required
def cancel_booking(id):
    print("Entered cancel booking")
    try:
        booking = Booking.query.filter(Booking.booking_no == id).first()
        booking.status = "Cancel"
        vehicle = Vehicle.query.filter(Vehicle.frame_no == booking.frame_no).first()
        vehicle.status = "Available"
        db.session.commit()
        flash(f'Booking {id} canceled successfully!', category='success')
    except Exception as e:
        print(e)
        flash(f'Vehicle {id} cancel failed!Message: {e.__cause__}', category='danger')
    return redirect(url_for("booking.view_booking"))


@booking.route('/<int:id>', methods=["GET"])
@login_required
def get_booking_by_id(id):
    print("Entered get_vehicle_by_id vehicle")
    try:
        customer = Booking.query.get_or_404(int(id))
    except Exception as e:
        print(e)
        flash(f'Vehicle {id} updated successfully! retrieval failed.Message: {e.__cause__}', category='danger')
    return redirect(url_for("booking.edit_booking"))


@booking.route('/customer/search', methods=["GET"])
@login_required
def customer_search():
    customer_name = request.args.get('qry')
    customer_results = Customer.query.filter(db.or_(
        Customer.customer_name.like(f'%{customer_name}%')))
    results = [customers.as_dict() for customers in customer_results]
    return jsonify(matching_results=results)


@booking.route('/vehicle/search', methods=["GET"])
@login_required
def vehicle_search():
    print("Entered vehicle search")
    print(request)
    model = request.args.get('qry')
    print(model)
    vehicle_results = Vehicle.query.filter(
        Vehicle.model.like(f'%{model}%'), Vehicle.status == "Available")
    print(vehicle_results)
    results = [vehicles.as_dict() for vehicles in vehicle_results]
    print(results)
    return jsonify(matching_results=results)
