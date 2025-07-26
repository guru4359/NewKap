from app.main import main  # Import the blueprint object defined above

@main.route('/')
def home():
    return "Hello from the main blueprint"
 from flask import render_template, request, redirect, url_for, flash
from app.orders import orders
#import stripe  # Uncomment and configure if integrating real payments

@orders.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        email = request.form['email']
        youtube_link = request.form['youtube']
        country = request.form['country']

        # -- Placeholder for order processing and Stripe payment link generation --
        # Example: payment_url = create_stripe_payment(...)
        # For now, just flash a message and redirect
        flash('Order received! You will receive a payment link soon.', 'success')
        return redirect(url_for('main.home'))

    return render_template('order.html')
