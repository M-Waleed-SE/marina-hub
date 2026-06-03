import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, template_folder='.') # Points to the current directory for HTML templates

# ================= EMAIL CONFIGURATION =================
# Replace these values with your actual system details
YOUR_EMAIL = "marenahubofficial@gmail.com"       # The inbox where you want to receive messages
SMTP_SERVER = "smtp.gmail.com"             # Using Gmail's outgoing mail server
SMTP_PORT = 587                            # Secure TLS port
SENDER_EMAIL = "your-system-email@gmail.com" # The email account sending the notifications
SENDER_PASSWORD = "beld dwyk wwdc ctau"      # Google App Password (not your normal password)


def send_email_notification(user_name, user_email, subject, message_body):
    """Formats and securely transmits the form contents to your inbox."""
    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = YOUR_EMAIL
        msg['Subject'] = f"[MARENA-HUB Contact] {subject}"

        # Clean readable plain-text formatting for your email reader
        body_content = f"""
        New Contact Form Submission from MARENA-HUB:
        --------------------------------------------------
        From: {user_name}
        User's Email: {user_email}
        Subject: {subject}
        
        Message:
        {message_body}
        --------------------------------------------------
        """
        msg.attach(MIMEText(body_content, 'plain'))

        # Open connection, secure it via TLS, log in, and transmit
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Error executing mail transmission: {e}")
        return False


# ================= BACKEND ROUTES =================

@app.route('/contact')
def contact_page():
    # Renders your static contact page layout
    return render_template('contact.html')

@app.route('/send-message', methods=['POST'])
def handle_contact_form():
    if request.method == 'POST':
        # Safely extract values from the form inputs via their 'name' attributes
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Trigger the mail sender function
        success = send_email_notification(name, email, subject, message)
        
        if success:
            # Simple alert string response. You can replace this with a success.html redirect later!
            return "<h1>Message Sent Successfully!</h1><p>Thank you for reaching out to MARENA-HUB.</p><a href='/contact'>Back to Contact Page</a>"
        else:
            return "<h1>System Error</h1><p>We could not send your message at this time. Please try again later.</p>", 500

if __name__ == '__main__':
    # Starts your development server locally on [http://127.0.0.1:5000](http://127.0.0.1:5000)
    app.run(debug=True)

