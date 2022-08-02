from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import login_required

from app import db
from models.vehicle import Vehicle
from vehicle.vehicle_form import CreateVehicleForm, UpdateVehicleForm

vehicle = Blueprint("vehicle", __name__, static_folder="static", template_folder="templates")


@vehicle.route('/')
@login_required
def view_vehicle():
    return render_template('vehicle.html')


@vehicle.route('/data', methods=["GET"])
@login_required
def view_vehicle_data():
    query = Vehicle.query

    # search filter
    search = request.args.get('search')
    if search:
        query = query.filter(db.or_(
            Vehicle.frame_no.like(f'%{search}%'),
            Vehicle.engine_no.like(f'%{search}%'),
            Vehicle.model.like(f'%{search}%'),
            Vehicle.dealer.like(f'%{search}%'),
        ))
    total = query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['frame_no', 'engine_no', 'model', 'dealer']:
                name = 'frame_no'
            col = getattr(Vehicle, name)
            if direction == '-':
                col = col.desc()
            order.append(col)
        if order:
            query = query.order_by(*order)
    else:
        query = query.order_by(Vehicle.frame_no.desc())
    # pagination
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query.offset(start).limit(length)

    return {
        'data': [vehicles.to_dict() for vehicles in query],
        'total': total,
    }


@vehicle.route('/create', methods=['GET', 'POST'])
@login_required
def create_vehicle():
    print("Entered create vehicle")
    vehicle_form = CreateVehicleForm()
    if vehicle_form.validate_on_submit():
        vehicle_to_create = Vehicle(engine_no=vehicle_form.engine_no.data,
                                    dealer=vehicle_form.dealer.data,
                                    delivery_chellan_no=vehicle_form.delivery_chellan_no.data,
                                    description=vehicle_form.description.data,
                                    status=vehicle_form.status,
                                    model=vehicle_form.model.data,
                                    comments=vehicle_form.comments.data,
                                    GST=vehicle_form.GST.data,
                                    vehicle_type=vehicle_form.vehicle_type.data
                                    )
        print(vehicle_to_create)
        db.session.add(vehicle_to_create)
        db.session.commit()
        flash(f'Vehicle {vehicle_to_create.engine_no} created successfully!', category='success')
        return redirect(url_for("vehicle.view_vehicle"))
    print("render create vehicle.html")
    return render_template('create_vehicle.html', form=vehicle_form)


@vehicle.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_vehicle(id):
    print("Entered update vehicle")
    update_vehicle_form = UpdateVehicleForm()
    vehicle_by_id = Vehicle.query.filter_by(frame_no=id).first()
    if update_vehicle_form.validate_on_submit():
        vehicle_by_id.engine_no = update_vehicle_form.engine_no.data
        vehicle_by_id.dealer = update_vehicle_form.dealer.data
        vehicle_by_id.delivery_chellan_no = update_vehicle_form.delivery_chellan_no.data
        vehicle_by_id.description = update_vehicle_form.description.data
        vehicle_by_id.model = update_vehicle_form.model.data
        vehicle_by_id.comments = update_vehicle_form.comments.data
        vehicle_by_id.vehicle_type = update_vehicle_form.vehicle_type.data
        vehicle_by_id.GST = update_vehicle_form.GST.data
        vehicle_by_id.status = update_vehicle_form.status.data
        db.session.commit()
        flash(f'Vehicle {vehicle_by_id.frame_no} updated successfully!', category='success')
        return redirect(url_for("vehicle.view_vehicle"))
    update_vehicle_form.engine_no.data = vehicle_by_id.engine_no
    update_vehicle_form.dealer.data = vehicle_by_id.dealer
    update_vehicle_form.delivery_chellan_no.data = vehicle_by_id.delivery_chellan_no
    update_vehicle_form.description.data = vehicle_by_id.description
    update_vehicle_form.model.data = vehicle_by_id.model
    update_vehicle_form.comments.data = vehicle_by_id.comments
    update_vehicle_form.vehicle_type.data = vehicle_by_id.vehicle_type
    update_vehicle_form.GST.data = vehicle_by_id.GST
    update_vehicle_form.status.data = vehicle_by_id.status
    return render_template('update_vehicle.html', form=update_vehicle_form)


@vehicle.route('/delete/<int:id>', methods=["GET"])
@login_required
def delete_customer(id):
    print("Entered delete vehicle")
    try:
        Vehicle.query.filter(Vehicle.customer_no == id).delete()
        db.session.commit()
        flash(f'Vehicle {id} deleted successfully!', category='success')
    except Exception as e:
        print(e)
        flash(f'Vehicle {id} deletion failed!Message: {e.__cause__}', category='danger')
    return redirect(url_for("vehicle.view_vehicle"))


@vehicle.route('/<int:id>', methods=["GET"])
@login_required
def get_customer_by_id(id):
    print("Entered get_vehicle_by_id vehicle")
    try:
        customer = Vehicle.query.get_or_404(int(id))
    except Exception as e:
        print(e)
        flash(f'Vehicle {id} updated successfully! retrieval failed.Message: {e.__cause__}', category='danger')
    return redirect(url_for("vehicle.view_vehicle"))
