from flask import Flask, render_template, request, redirect, url_for, session
from gbmodel.model_sqlite3 import SQLiteModel
from authlib.integrations.flask_client import OAuth
import os
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'super-secret-key')

# Configure OAuth
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={'scope': 'openid email profile'},
)

# Connect to the database
model = SQLiteModel(os.getenv('DATABASE_PATH', 'path_to_your_database.db'))

# Route for the index page
@app.route('/')
def index():
    # Check if user is logged in
    if 'google_token' not in session:
        return render_template('login.html')  # Provide a login template with a login link
    else:
        # The authenticated landing page might show a form to create a new entry
        return render_template('index.html')

# Google login route
@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    print("Redirect URI being used:", redirect_uri)  # This will print to the console where your Flask app is running
    return google.authorize_redirect(redirect_uri)


# Google authorize route
@app.route('/login/callback')
def authorize():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    session['google_token'] = token
    session['user'] = user_info
    return redirect(url_for('index'))

# Route to logout
@app.route('/logout')
def logout():
    session.pop('google_token', None)
    session.pop('user', None)
    return redirect(url_for('index'))

# Existing routes like view_entries and create_entry will require user to be logged in
# For example:
@app.route('/entries', methods=['GET'])
def view_entries():
    if 'google_token' not in session:
        return redirect(url_for('login'))  # Redirect to login if not authenticated
    # Rest of the function ...

# Make sure to secure other routes in a similar way

if __name__ == '__main__':
    # Set the port number to run on a different port if needed
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
