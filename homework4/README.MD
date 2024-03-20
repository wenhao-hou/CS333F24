# Flask OAuth Authentication with Google Cloud Platform

## Prerequisites

Before beginning, ensure you have a Google Cloud Platform account and the `authlib` library installed in your Flask app's environment.

## Configuration Steps

### Step 1: Set Up Google Cloud Project and OAuth Consent Screen

- Create a new project in the Google Cloud Console.
- Configure the OAuth consent screen with your app details.
- Set up the required scopes for your app.

### Step 2: Create OAuth Client ID and Secret

In the Google Cloud Console:
- Navigate to APIs & Services > Credentials.
- Create a new OAuth client ID.
- Set the Authorized JavaScript origins to `http://127.0.0.1:8080`.
- Set the Authorized redirect URIs to `http://127.0.0.1:8080/login/callback`.

### Step 3: Configure Environment Variables

Set the following environment variables in your development environment:

```sh
export GOOGLE_CLIENT_ID='your-google-client-id'
export GOOGLE_CLIENT_SECRET='your-google-client-secret'
export FLASK_SECRET_KEY='your-random-secret-key'

STEp 4:

from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    # ... additional configuration ...
)

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/login/callback')
def authorize():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    session['google_token'] = token
    session['user'] = user_info
    return redirect('/')
