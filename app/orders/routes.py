from app.orders import orders  # Import the blueprint object

@orders.route('/order')
def order():
    return "Order page placeholder"
