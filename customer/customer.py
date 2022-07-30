from datetime import datetime

from flask import render_template, Blueprint, flash, redirect, url_for, request
from flask_login import login_required

from customer.customer_form import CreateCustomerForm, UpdateCustomerForm
from app import db

from models.customer import Customer

customer = Blueprint("customer", __name__, static_folder="static", template_folder="templates")


@customer.route('/', methods=["GET"])
@login_required
def view_customer():
    return render_template('customer.html')


@customer.route('/data', methods=["GET"])
# @customer.route('/<int:page>', methods=['GET', 'POST'])
@login_required
def view_customer_data():
    query = Customer.query

    # search filter
    search = request.args.get('search')
    if search:
        query = query.filter(db.or_(
            Customer.customer_no.like(f'%{search}%'),
            Customer.customer_name.like(f'%{search}%'),
            Customer.email.like(f'%{search}%')
        ))
    total = query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['customer_no', 'customer_name', 'email']:
                name = 'customer_name'
            col = getattr(Customer, name)
            if direction == '-':
                col = col.desc()
            order.append(col)
        if order:
            query = query.order_by(*order)

    # pagination
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query.offset(start).limit(length)

    return {
        'data': [customers.to_dict() for customers in query],
        'total': total,
    }


@customer.route('/create', methods=['GET', 'POST'])
@login_required
def create_customer():
    print("Entered create customer")
    customer_form = CreateCustomerForm()
    if customer_form.validate_on_submit():
        customer_to_create = Customer(customer_name=customer_form.customer_name.data,
                                      email=customer_form.email.data,
                                      dob=customer_form.dob.data,
                                      mobile1=customer_form.mobile1.data,
                                      mobile2=customer_form.mobile2.data,
                                      mobile3=customer_form.mobile3.data,
                                      comment=customer_form.comment.data,
                                      GST=customer_form.GST.data,
                                      city=customer_form.city.data,
                                      street=customer_form.street.data,
                                      pincode=customer_form.pincode.data
                                      )
        db.session.add(customer_to_create)
        db.session.commit()
        flash(f'Customer {customer_to_create.customer_name} created successfully!', category='success')
        return redirect(url_for("customer.view_customer"))
    return render_template('create_customer.html', form=customer_form)


@customer.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_customer(id):
    print("Entered update customer")
    update_customer_form = UpdateCustomerForm()
    customer_by_id = Customer.query.filter_by(customer_no=id).first()
    if update_customer_form.validate_on_submit():
        customer_by_id.comment = update_customer_form.comment.data
        customer_by_id.customer_name = update_customer_form.customer_name.data
        customer_by_id.email = update_customer_form.email.data
        customer_by_id.dob = update_customer_form.dob.data
        customer_by_id.mobile1 = update_customer_form.mobile1.data
        customer_by_id.mobile2 = update_customer_form.mobile2.data
        customer_by_id.mobile3 = update_customer_form.mobile3.data
        customer_by_id.GST = update_customer_form.GST.data
        customer_by_id.city = update_customer_form.city.data
        customer_by_id.street = update_customer_form.street.data
        customer_by_id.pincode = update_customer_form.pincode.data
        db.session.commit()
        flash(f'Customer {customer_by_id.customer_name} updated successfully!', category='success')
        return redirect(url_for("customer.view_customer"))
    update_customer_form.customer_name.data = customer_by_id.customer_name
    update_customer_form.email.data = customer_by_id.email
    update_customer_form.dob.data = datetime.strptime(customer_by_id.dob, '%Y-%m-%d')
    update_customer_form.mobile1.data = customer_by_id.mobile1
    update_customer_form.mobile2.data = customer_by_id.mobile2
    update_customer_form.mobile3.data = customer_by_id.mobile3
    update_customer_form.comment.data = customer_by_id.comment
    update_customer_form.GST.data = customer_by_id.GST
    update_customer_form.city.data = customer_by_id.city
    update_customer_form.street.data = customer_by_id.street
    update_customer_form.pincode.data = customer_by_id.pincode
    return render_template('update_customer.html', form=update_customer_form)


@customer.route('/delete/<int:id>', methods=["GET"])
@login_required
def delete_customer(id):
    print("Entered delete customer")
    try:
        Customer.query.filter(Customer.customer_no == id).delete()
        db.session.commit()
        flash(f'Customer {id} deleted successfully!', category='success')
    except Exception as e:
        print(e)
        flash(f'Customer {id} deletion failed!Message: {e.__cause__}', category='danger')
    return redirect(url_for("customer.view_customer"))


@customer.route('/<int:id>', methods=["GET"])
@login_required
def get_customer_by_id(id):
    print("Entered get_customer_by_id customer")
    try:
        customer = Customer.query.get_or_404(int(id))
    except Exception as e:
        print(e)
        flash(f'Customer {id} updated successfully! retrieval failed.Message: {e.__cause__}', category='danger')
    return redirect(url_for("customer.view_customer"))
