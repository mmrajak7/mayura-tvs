import os

import pandas as pd
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from werkzeug.utils import secure_filename

from app import app, db

stocks = Blueprint("stocks", __name__, static_folder="static", template_folder="templates")


@stocks.route('/', methods=['GET', 'POST'])
@login_required
def view_stocks():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        print("file name")
        print(uploaded_file)
        print(app.config['UPLOAD_PATH'])
        if uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                flash(f'Invalid file extension {file_ext}!', category='danger')
                return render_template('stocks.html')
            print(os.path.join(app.config['UPLOAD_PATH']))
            file_path = os.path.join(app.config['UPLOAD_PATH'], filename)
            uploaded_file.save(file_path)

            update_cashbook(file_path)
            update_bank(file_path)
            update_pos(file_path)
            update_exchange(file_path)
            update_insurance(file_path)
            update_soa(file_path)

            uploaded_file.close()
            os.remove(file_path)
            flash(f'File {file_ext} upload successfully!', category='success')
            return redirect(url_for("stocks.view_stocks"))
    return render_template('stocks.html')


def update_cashbook(file_path):
    cashbook = pd.read_excel(file_path, header=None,
                             names=["cashbook_date", "nature_of_expenses", "details", "customer_name",
                                    "payments",
                                    "receipts", "closing_balance"], sheet_name='cashbook', skiprows=1,
                             usecols=[0, 1, 2, 3, 4, 5, 6])
    cashbook.to_sql("cashbook", db.engine, index=False, if_exists="append")


def update_bank(file_path):
    bank = pd.read_excel(file_path, header=None,
                         names=["tran_date", "value_date", "chq_no", "transaction_particulars", "amount",
                                "dr_cr", "balance", "branch_name", "comments", "marker"], sheet_name='Bank',
                         skiprows=1,
                         usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    bank.to_sql("bank", db.engine, index=False, if_exists="append")


def update_pos(file_path):
    pos = pd.read_excel(file_path, header=None,
                        names=["tran_date", "batch_no", "card_type", "ti", "card_no",
                               "approve_code", "gross_amt", "mdr", "gst", "net_amount", "process_date",
                               "frame_no"], sheet_name='POS', skiprows=1,
                        usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    pos.to_sql("pos", db.engine, index=False, if_exists="append")


def update_exchange(file_path):
    exchange = pd.read_excel(file_path, header=None,
                             names=["exchange_no", "frame_no", "vehicle_type", "vehicle_name",
                                    "exchange_vehicle_value",
                                    "exchange_vehicle_name", "payment_status", "in_date", "out_date"],
                             sheet_name='Exch', skiprows=1,
                             usecols=[0, 1, 2, 3, 4, 5, 6, 7])
    exchange.to_sql("exchange", db.engine, index=False, if_exists="append")


def update_insurance(file_path):
    insurance = pd.read_excel(file_path, header=None,
                              names=["customer_name", "vehicle", "type", "policy_company", "date",
                                     "chasis_no", "policy_no", "amount"], sheet_name='Insurance', skiprows=1,
                              usecols=[0, 1, 2, 3, 4, 5, 6, 7])
    insurance.to_sql("insurance", db.engine, index=False, if_exists="append")


def update_soa(file_path):
    soa = pd.read_excel(file_path, header=None,
                        names=["date", "dr_cr", "particulars", "reference", "vehicle_type",
                               "vehicle_no", "debit", "credit", "frame_no", "cash_bank_finance", "ad_margin",
                               "dealer"], sheet_name='SOA', skiprows=1,
                        usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    soa.to_sql("soa", db.engine, index=False, if_exists="append")
