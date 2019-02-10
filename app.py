from app import app

if __name__ == "__main__":
    app.run(debug=True)

"""

<<<<<< TERMINAL COMMANDS >>>>>>
import db as an instance since <db> is the variable used to communicate to the database using sqlalchemy
- create all the structure of the database
db.create_all()

variable = <Model Class> ( insert the parameters )
to save the data into the database 
db.session.add(the_variable)
db.session.commit()
db.drop.all()

user.id is for the user_id because it is used as the foreign key
>>>>>>>>>>>>>>>
<QUERY>

User.query.all()
User.query.filter_by(username='the username').all()
User.query.get(1)

>>>>>>>>>>>>
"""