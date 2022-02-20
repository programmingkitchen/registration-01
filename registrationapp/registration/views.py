import sys
from flask import Flask, Blueprint, request, render_template, redirect, url_for, flash, abort
from registrationapp import db
from registrationapp.models import Member
from registrationapp.registration.forms import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import ValidationError


'''
============================================================
                        REGISTRATION
============================================================
'''

registration_blueprint = Blueprint('registration',
                              __name__,
                              template_folder='templates/registration')

# TODO:  Strip surrounding spaces
@registration_blueprint.route('/registration', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        print("REGISTER:  Valid Form on Register Submit: ", form.validate_on_submit(), file=sys.stderr)
        name = form.name.data
        name = name.lower()
        print("REGISTER:  Valid Form on Register Submit: ", name, file=sys.stderr)
        password = form.password.data

        # Check to see if the email is already registered.
        # TODO: If this gets triggered what do with do with the message and the
        # error.  This is how we propagte a raised error. Don't forget the import.
        try:
            form.checkName(name)
            toAdd = Member(name, password)
            db.session.add(toAdd)
            db.session.commit()
            flash('Thanks for registering! Now you can login!')
            return redirect(url_for('auth.login'))
        except ValidationError as err:
            print("ValidationError: ", err.args, file=sys.stderr)
            flash('Email address already registered.')
            #flash(err.args)
            return render_template('register.html', form=form)

    print("REGISTER:  Valid Form on GET: ", form.validate_on_submit(), file=sys.stderr)
    return render_template('register.html', form=form)
