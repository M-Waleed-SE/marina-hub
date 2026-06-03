from flask import Flask, render_template, request

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('forget.html')

# Forgot Password Route
@app.route('/forgot-password', methods=['POST'])
def forgot_password():

    email = request.form.get('email')

    # Check if email entered
    if email:
        return f"""
        <h2>Reset link has been sent to {email}</h2>
        <a href="/">Go Back</a>
        """
    else:
        return """
        <h2>Please enter your email address</h2>
        <a href="/">Go Back</a>
        """

if __name__ == '__main__':
    app.run(debug=True)