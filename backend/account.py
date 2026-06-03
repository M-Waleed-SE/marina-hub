from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__, template_folder='.')
app.secret_key = 'marena_hub_secure_session_key'  # Required by Flask to manage encrypted session cookies

# Temporary volatile dictionary acting as our localized mock student database storage
DATABASE = {}

@app.route('/signup')
def signup_page():
    """Renders the account registration form layout view."""
    return render_template('sign.html') # Pulls your registration template layout file


@app.route('/register', methods=['POST'])
def process_registration():
    """Extracts student data from signup form and registers user."""
    if request.method == 'POST':
        # Safely capture user inputs via form input 'name' fields
        full_name = request.form.get('fullName')
        email = request.form.get('email')
        password = request.form.get('password') # In production environments, hash this securely!
        
        # Strip out email domain details to quickly construct a friendly clean username handle
        generated_username = email.split('@')[0].lower() if email else "student"

        # Bundle structural layout data for storage allocation
        user_account = {
            'name': full_name,
            'email': email,
            'username': generated_username,
            'password': password
        }

        # Store account parameters using unique email address identifiers
        DATABASE[email] = user_account

        # Authorize session explicitly to transition directly into dashboard log context
        session['logged_in_user'] = email

        # Reroute request seamlessly into active dynamic dashboard view loop
        return redirect(url_for('account_dashboard'))


@app.route('/account')
def account_dashboard():
    """Loads authenticated student record information into layout template dynamically."""
    # Enforce standard access validation check logic
    current_user_email = session.get('logged_in_user')

    if not current_user_email or current_user_email not in DATABASE:
        # Halt unauthorized tracking context and bounce safely back to registration checkpoint
        return redirect(url_for('signup_page'))

    # Extract target record dictionary from memory allocation system map 
    active_student = DATABASE[current_user_email]

    # Serve user template structure cleanly populated with functional runtime data context variables
    return render_template('account.html', student=active_student)


@app.route('/update-profile', methods=['POST'])
def handle_profile_updates():
    """Intercepts inline student account modification entries from dashboard inputs."""
    current_user_email = session.get('logged_in_user')

    if not current_user_email or current_user_email not in DATABASE:
        return redirect(url_for('signup_page'))

    if request.method == 'POST':
        new_name = request.form.get('fullName')
        new_email = request.form.get('email')

        # Target entry references directly to update storage records
        DATABASE[current_user_email]['name'] = new_name
        
        # If the student email address updates, re-map our internal references safely
        if new_email != current_user_email:
            DATABASE[new_email] = DATABASE.pop(current_user_email)
            DATABASE[new_email]['email'] = new_email
            session['logged_in_user'] = new_email

        return redirect(url_for('account_dashboard'))


@app.route('/logout')
def terminate_session():
    """Flushes active session states safely out of user tracking pipeline context."""
    session.pop('logged_in_user', None)
    return redirect(url_for('signup_page'))


if __name__ == '__main__':
    # Spins up active development server loop process matching terminal configuration commands
    app.run(debug=True)

