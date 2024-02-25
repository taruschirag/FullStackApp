# main endpoints of the app. If the app is big it is split in multiple models.
# """The front end usually creates a request to the server. Each request is a different type. 1. Get request is accessing some type of something
# from the server. Post request is creating something new. Patch request is when we want to update something. Delete request deletes something
# We can also send JSON data. It can be used to handle the request. If we want to delete a contact, we can pass in the info as a json.
# The server then gives a response and it gives a status. (200 is successfull, 404 is error, etc)"""

# jsonify allows to send json
from flask import request, jsonify

# import other stuff
from config import app, db
from models import Contact


# when we reach the contact endpoint, we use the get method.
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})


@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"A value is missing"}), 400

    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)

    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"There was error": str(e)}), 400

    return jsonify({"Created"}), 200


@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"A value is missing"}), 400
    else:
        data = request.json
        contact.first_name = data.get("firstName", contact.first_name)
        contact.last_name = data.get("lastName", contact.last_name)
        contact.email = data.get("email", contact.email)

        db.session.commit()
        return jsonify({"User was updated"}), 200


@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"A value is missing"}), 400

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"User was deleted"}), 200


# if we import main.py and run the other file then it shouldn't run this. Only run this when we run main.py
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
