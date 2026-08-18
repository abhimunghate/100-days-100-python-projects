# This is Day 38 project : Contact Form App

from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp
import csv
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'your_secret_key'

CONTACT_FILE = "contacts.csv"

SENDER_EMAIL = "my_email@gmail.com"
SENDER_PASSWORD = "my_app_password"

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField("Phone Number", validators=[DataRequired(), Regexp(r"^\+?[0-9]{10,15}$", message="Enter a valid phone number.")])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')
    
def save_submission(name, email, phone, message):
    file_exists = os.path.exists(CONTACT_FILE)
    with open(CONTACT_FILE, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        if not file_exists:
            writer.writerow(["Name", "Email", "Phone", "Message"])
        writer.writerow([name, email, phone, message])
        
def send_confirmation_email(name, email):
    msg = EmailMessage()
    msg["Subject"] = "Contact Form Confirmation"
    msg["From"] = SENDER_EMAIL
    msg["To"] = email

    msg.set_content(f"""Hello {name}, Thank you for contacting us. We have successfully received your message. We will get back to you as soon as possible. Regards, Contact Form App""")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)
    
@app.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        message = form.message.data
        save_submission(name, email, phone, message)
        
        email_sent = False
        try:
            send_confirmation_email(name, email)
            email_sent = True
        except Exception as error:
            print("Email could not be sent:", error)
            
        flash(f"Thank you, {name}! Your message has been submitted successfully.", "success")
        return render_template("success.html", email_sent=email_sent)
    return render_template('contact.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
    
# Done