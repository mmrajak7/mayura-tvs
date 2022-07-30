from flask import render_template, Blueprint
from flask_login import login_required

invoice = Blueprint("invoice", __name__, static_folder="static", template_folder="templates")


@invoice.route('/')
@login_required
def generate_invoice():
    headings = ("Name", "Phone", "Barcode", "Price")
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150},
        {'id': 3, 'name': 'invoice', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('invoice.html', headings=headings, item_name='Phone', items=items)
