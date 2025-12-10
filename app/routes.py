from flask import Blueprint, render_template, redirect, url_for, request
from app.demo_data import services, gallery_images, testimonials

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template(
        'home.html',
        services=services[:4],
        gallery_images=gallery_images[:8],
        testimonials=testimonials[:5]
    )

@main.route('/services')
def services_page():
    return render_template('services.html', services=services)

@main.route('/gallery')
def gallery_page():
    return render_template('gallery.html', gallery_images=gallery_images)

@main.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form.get('email')
        event_date = request.form['event_date']
        event_time = request.form['event_time']
        service_id = request.form['service_id']
        message = request.form.get('message')

        # ✅ WhatsApp redirect instead of saving to DB
        whatsapp_message = (
            f"New Booking Request%0A"
            f"Name: {name}%0A"
            f"Phone: {phone}%0A"
            f"Email: {email}%0A"
            f"Service ID: {service_id}%0A"
            f"Date: {event_date}%0A"
            f"Time: {event_time}%0A"
            f"Message: {message}"
        )

        whatsapp_url = f"https://wa.me/91XXXXXXXXXX?text={whatsapp_message}"
        return redirect(whatsapp_url)

    return render_template('booking.html', services=services)

@main.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # ✅ WhatsApp redirect instead of saving to DB
        whatsapp_message = (
            f"New Contact Message%0A"
            f"Name: {name}%0A"
            f"Phone: {phone}%0A"
            f"Email: {email}%0A"
            f"Message: {message}"
        )

        whatsapp_url = f"https://wa.me/8870685588?text={whatsapp_message}"
        return redirect(whatsapp_url)

    return render_template('contact.html')
@main.route("/pricing")
def pricing():
    return render_template("pricing.html")
@main.route("/faq")
def faq():
    return render_template("faq.html")