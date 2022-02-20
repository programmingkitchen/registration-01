'''
    This version requires that we do db.create_all() to set up the database
    before we do anything else.  The creation of the account is optional.
    How can we create the db dynamically using Flask-SQLAlchemy?

'''

# Import database info
from registrationapp import db
from registrationapp.models import Member

# Create the tables in the database
# (Usually won't do it this way!)
db.create_all()

defaultpw = 'password'

users = ['test1', 'test2']

for user in users:
    member = Member(user, 'password-clear')
    member.passwordHash = member.genPassword(defaultpw)
    db.session.add(member)
    db.session.commit()

print ("Setup complete.")
