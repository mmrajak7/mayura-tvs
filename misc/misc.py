from flask import Blueprint, render_template, request
from flask_login import login_required

from app import db
from models.bank import Bank
from models.cashbook import Cashbook
from models.exchange import Exchange
from models.insurance import Insurance
from models.pos import Pos
from models.soa import Soa

misc = Blueprint("misc", __name__, static_folder="static", template_folder="templates")


@misc.route('/bank')
@login_required
def view_bank():
    return render_template('bank.html')


@misc.route('/bank/data', methods=["GET"])
@login_required
def view_bank_data():
    query = Bank.query

    # search filter
    search = request.args.get('search')
    if search:
        query = query.filter(db.or_(
            Bank.bank_no.like(f'%{search}%'),
            Bank.tran_date.like(f'%{search}%'),
            Bank.balance.like(f'%{search}%'),
        ))
    total = query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['bank_no', 'tran_date', 'balance']:
                name = 'bank_no'
            col = getattr(Bank, name)
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
    print(query)
    return {
        'data': [banks.to_dict() for banks in query],
        'total': total,
    }


@misc.route('/cashbook')
@login_required
def view_cashbook():
    return render_template('cashbook.html')


@misc.route('/cashbook/data', methods=["GET"])
@login_required
def view_cashbook_data():
    query = Cashbook.query

    # search filter
    search = request.args.get('search')
    print(search)
    if search:
        query = query.filter(db.or_(
            Cashbook.cashbook_no.like(f'%{search}%'),
            Cashbook.cashbook_date == search,
            Cashbook.nature_of_expenses.like(f'%{search}%'),
            Cashbook.customer_name.like(f'%{search}%'),
        ))
    total = query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['cashbook_no', 'cashbook_date', 'nature_of_expenses', 'customer_name']:
                name = 'cashbook_no'
            col = getattr(Cashbook, name)
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
    print(query)
    return {
        'data': [cashbooks.to_dict() for cashbooks in query],
        'total': total,
    }


@misc.route('/pos')
@login_required
def view_pos():
    return render_template('pos.html')


@misc.route('/pos/data', methods=["GET"])
@login_required
def view_pos_data():
    query = Pos.query

    # search filter
    search = request.args.get('search')
    if search:
        query = query.filter(db.or_(
            Pos.pos_no.like(f'%{search}%'),
            Pos.tran_date.like(f'%{search}%'),
            Pos.card_type.like(f'%{search}%'),
            Pos.frame_no.like(f'%{search}%'),
        ))
    total = query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['pos_no', 'tran_date', 'card_type', 'frame_no']:
                name = 'pos_no'
            col = getattr(Pos, name)
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
    print(query)
    return {
        'data': [poss.to_dict() for poss in query],
        'total': total,
    }


@misc.route('/exchange')
@login_required
def view_exchange():
    return render_template('exchange.html')


@misc.route('/exchange/data', methods=["GET"])
@login_required
def view_exchange_data():
    query = Exchange.query

    # search filter
    search = request.args.get('search')
    if search:
        query = query.filter(db.or_(
            Exchange.exchange_no.like(f'%{search}%'),
            Exchange.frame_no.like(f'%{search}%'),
            Exchange.payment_status.like(f'%{search}%'),
        ))
    total = query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['exchange_no', 'frame_no', 'payment_status']:
                name = 'exchange_no'
            col = getattr(Exchange, name)
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
    print(query)
    return {
        'data': [exchanges.to_dict() for exchanges in query],
        'total': total,
    }


@misc.route('/insurance')
@login_required
def view_insurance():
    return render_template('insurance.html')


@misc.route('/insurance/data', methods=["GET"])
@login_required
def view_insurance_data():
    print("Entered view_insurance_data")
    query = Insurance.query

    # search filter
    search = request.args.get('search')
    if search:
        query = query.filter(db.or_(
            Insurance.insurance_no.like(f'%{search}%'),
            Insurance.customer_name.like(f'%{search}%'),
            Insurance.type.like(f'%{search}%'),
            Insurance.chasis_no.like(f'%{search}%'),
        ))
    total = query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['insurance_no', 'customer_name', 'type', 'chasis_no']:
                name = 'insurance_no'
            col = getattr(Insurance, name)
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
    print(query)
    return {
        'data': [insurances.to_dict() for insurances in query],
        'total': total,
    }


@misc.route('/soa')
@login_required
def view_soa():
    return render_template('soa.html')


@misc.route('/soa/data', methods=["GET"])
@login_required
def view_soa_data():
    query = Soa.query

    # search filter
    search = request.args.get('search')
    if search:
        query = query.filter(db.or_(
            Soa.soa_no.like(f'%{search}%'),
            Soa.date.like(f'%{search}%'),
            Soa.frame_no.like(f'%{search}%'),
        ))
    total = query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['soa_no', 'date', 'frame_no']:
                name = 'soa_no'
            col = getattr(Soa, name)
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
    print(query)
    return {
        'data': [soas.to_dict() for soas in query],
        'total': total,
    }
