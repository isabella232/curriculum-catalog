from flask import Flask, request
from flask_mail import Mail, Message
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('requester_email')
parser.add_argument('requester_company')
parser.add_argument('requested_courses')

app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='quansighttesting@gmail.com',
    MAIL_PASSWORD='Testingpassword101'
)

mail = Mail(app)


class SendMail(Resource):
    def post(self):
        args = parser.parse_args()
        courses = json.loads(args["requested_courses"])
        coursestring = ""
        for course in courses:
            coursestring += course + "\n"

        msg = Message(subject="Course Information Request",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[args["requester_email"]],
                      body=args["requester_company"] + ", you have requested information about:\n\n" +
                      coursestring + "\nand will receive information about them within a week.\n\n" +
                      "Sincerely,\nQuansight")
        mail.send(msg)

        msg = Message(subject="Course Information Request",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[app.config.get("MAIL_USERNAME")],
                      body=args["requester_company"] + " with email " + args["requester_email"] + " has requested" +
                      "information about\n\n" + coursestring + "\nand are waiting on a response.\n\n" +
                      "Sent from Quansight Course Training Email")
        mail.send(msg)


api.add_resource(SendMail, "/sendemail")


if __name__ == "__main__":
    app.run(debug=True)
