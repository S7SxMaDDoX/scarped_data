from flask import Flask, render_template, request, redirect
from scraper import get_events

app = Flask(__name__)

@app.route('/')
def home():
    events = get_events()
    return render_template('index.html', events=events)

@app.route('/get-ticket', methods=['POST'])
def get_ticket():
    email = request.form['email']
    event_link = request.form['event_link']
    print(f"Collected email: {email}")  # Later you can save this
    return redirect(event_link)

if __name__ == '__main__':
    app.run(debug=True)
