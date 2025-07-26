from flask import render_template, request, redirect, url_for, flash
from app.main import main  # import the blueprint object

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Example form processing placeholder
        flash('Thank you for your message!', 'success')
        return redirect(url_for('main.home'))
    return render_template('contact.html')
