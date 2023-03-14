"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import Property
from .forms import MyForm
from .config import Config



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['post', 'get'])
def new_property():
    """Render the website's create page"""
    propertyform = MyForm()
    if request.method == "POST":
        if propertyform.validate_on_submit():
            title = propertyform.title.data
            numberofbedrooms = propertyform.numberofbedrooms.data
            numberofbathrooms = propertyform.numberofbathrooms.data
            location = propertyform.location.data
            price = propertyform.price.data
            type = propertyform.type.data
            description = propertyform.description.data
            photo = propertyform.photo.data

            property = Property(title, numberofbedrooms, numberofbathrooms, location, price, type, description, photo)
            db.session.add(property)
            db.session.commit()

            flash('Property added successfully!')
            redirect(url_for('properties'))

        flash_errors(propertyform)
        return render_template('create.html', form=propertyform)

        # db = connect_db()
        # cur = db.cursor()
        # cur.execute('insert into properties () values ()', request.form)
    

    return render_template('create.html', form = propertyform)

@app.route('/properties')
def properties():
    form = MyForm()
    return render_template('create.html', form=form)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
