from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import json
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app)
api = Api(app)


class SendEmail(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('requester_email')
        parser.add_argument('requester_company')
        parser.add_argument('requested_courses')

        sender_email = "quansighttesting@gmail.com"
        password = "ynrkzeshfyybmmqo"

        userMessage = MIMEMultipart("alternative")
        userMessage["Subject"] = "Course Information Request"
        userMessage["From"] = sender_email

        qMessage = MIMEMultipart("alternative")
        qMessage["Subject"] = "Course Information Request"
        qMessage["From"] = sender_email

        args = parser.parse_args()
        courses = json.loads(args["requested_courses"])
        coursestring = ""
        for course in courses:
            coursestring += course + "<br/>"

        imagesrc = "\"https://drive.google.com/uc?id=1aj4GIMiWdkSF1uqjJBw63tGUIGNk4nbQ\""
        htmlmessage = args["requester_company"] + ", you have requested information about:<br/><br/>" + \
                      coursestring + "<br/>You will receive information about them within a week.<br/><br/>" + \
                      "Thank you,<br/>Quansight<br/>"
        msg = """\
        <html>
            <body>
                <p> 
                    """ + htmlmessage + """
                    <img src =""" + imagesrc + """ style=\"width:200px\"/>
                </p>
            </body>
        </html>
        """

        qhtmlmessage = args["requester_company"] + " with email " + args["requester_email"] + " has requested " + \
                       "information about<br/><br/>" + coursestring + "<br/>and are waiting on a response.<br/><br/>" \
                       + "Sent from Quansight Course Training Email<br/>"
        qmsg = """\
        <html>
            <body>
                <p> 
                    """ + qhtmlmessage + """
                    <img src =""" + imagesrc + """/>
                </p>
            </body>
        </html>
        """

        qMessage.attach(MIMEText(qmsg, "html"))
        userMessage.attach(MIMEText(msg, "html"))
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, args["requester_email"], userMessage.as_string())
            server.sendmail(sender_email, sender_email, qMessage.as_string())


class SendCourseEmail(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('requester_email')
        parser.add_argument('requester_company')
        parser.add_argument('requested_courses')

        sender_email = "quansighttesting@gmail.com"
        password = "ynrkzeshfyybmmqo"

        userMessage = MIMEMultipart("alternative")
        userMessage["Subject"] = "Courses Selected Notification"
        userMessage["From"] = sender_email

        qMessage = MIMEMultipart("alternative")
        qMessage["Subject"] = "Courses Selected Notification"
        qMessage["From"] = sender_email

        args = parser.parse_args()
        courses = json.loads(args["requested_courses"])
        coursestring = ""
        for course in courses:
            coursestring += course + "<br/>"

        imagesrc = "\"https://drive.google.com/uc?id=1aj4GIMiWdkSF1uqjJBw63tGUIGNk4nbQ\""
        htmlmessage = args["requester_company"] + ", you have selected these courses:<br/><br/>" + \
                      coursestring + "<br/>If you would like more information about pricing and the courses, " + \
                      "please email us with your list at training@quansight.com.<br/><br/>" + \
                      " Thank you for your interest,<br/>Quansight<br/>"
        msg = """\
                <html>
                    <body>
                        <p> 
                            """ + htmlmessage + """
                            <img src =""" + imagesrc + """ style=\"width:200px\"/>
                        </p>
                    </body>
                </html>
                """

        qhtmlmessage = args["requester_company"] + " with email " + args["requester_email"] + " has saved their " + \
                       "courses about<br/><br/>" + coursestring + "<br/>They may request more info later.<br/><br/>" \
                       + "Sent from Quansight Course Training Email<br/>"
        qmsg = """\
                <html>
                    <body>
                        <p> 
                            """ + qhtmlmessage + """
                            <img src =""" + imagesrc + """/>
                        </p>
                    </body>
                </html>
                """

        qMessage.attach(MIMEText(qmsg, "html"))
        userMessage.attach(MIMEText(msg, "html"))
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, args["requester_email"], userMessage.as_string())
            server.sendmail(sender_email, sender_email, qMessage.as_string())


class SendInfoHelpEmail(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('requester_email')
        parser.add_argument('requester_company')

        sender_email = "quansighttesting@gmail.com"
        password = "ynrkzeshfyybmmqo"

        userMessage = MIMEMultipart("alternative")
        userMessage["Subject"] = "Course Builder Help Request"
        userMessage["From"] = sender_email

        qMessage = MIMEMultipart("alternative")
        qMessage["Subject"] = "Course Builder Help Request"
        qMessage["From"] = sender_email

        args = parser.parse_args()

        imagesrc = "\"https://drive.google.com/uc?id=1aj4GIMiWdkSF1uqjJBw63tGUIGNk4nbQ\""
        htmlmessage = args["requester_company"] + ",<br/>Thank you for your interest in Quansight's training program!" \
                                                  "<br/>You should receive an email within a week requesting a good " \
                                                  "time for a phone, video, or voice call to discuss what it is you " \
                                                  "need help training.<br/><br/>" \
                                                  "We look forward to helping you,<br/>Quansight<br/>"
        msg = """\
                <html>
                    <body>
                        <p> 
                            """ + htmlmessage + """
                            <img src =""" + imagesrc + """ style=\"width:200px\"/>
                        </p>
                    </body>
                </html>
                """

        qhtmlmessage = args["requester_company"] + " with email " + args["requester_email"] + " has requested help " \
                        "with developing a training program for their company.<br/>They are waiting to set up a time " \
                        "to talk with a Quansight representative.<br/><br/>Sent from Quansight Course Training Email" \
                        "<br/>"
        qmsg = """\
                <html>
                    <body>
                        <p> 
                            """ + qhtmlmessage + """
                            <img src =""" + imagesrc + """/>
                        </p>
                    </body>
                </html>
                """

        qMessage.attach(MIMEText(qmsg, "html"))
        userMessage.attach(MIMEText(msg, "html"))
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, args["requester_email"], userMessage.as_string())
            server.sendmail(sender_email, sender_email, qMessage.as_string())


api.add_resource(SendEmail, "/sendmainemail")
api.add_resource(SendCourseEmail, "/sendcourseemail")
api.add_resource(SendInfoHelpEmail, "/sendinfohelpemail")


if __name__ == "__main__":
    app.run(debug=True)
