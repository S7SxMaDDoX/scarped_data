# Create a directory structure and generate the necessary files for the assignment
import os

base_path = "/mnt/data/sydney_events_site"
templates_path = os.path.join(base_path, "templates")

# Create directories
os.makedirs(templates_path, exist_ok=True)

# Content for scraper.py
scraper_py = """
import requests
from bs4 import BeautifulSoup

def get_events():
    url = 'https://www.timeout.com/sydney/events'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    events = []
    for event in soup.select('.card-content'):  # Selector might need update based on inspection
        title = event.select_one('.card-title')
        link = event.select_one('a')
        if title and link:
            events.append({
                'title': title.text.strip(),
                'link': link['href']
            })
    return events
"""

# Content for app.py
app_py = """
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
    print(f"Collected email: {email}")  # This could be saved to a file or database
    return redirect(event_link)

if __name__ == '__main__':
    app.run(debug=True)
"""

# Content for index.html
index_html = """
<!DOCTYPE html>
<html>
<head>
  <title>Sydney Events</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="container mt-4">
  <h1>Sydney Events</h1>
  {% for event in events %}
    <div class="card my-3">
      <div class="card-body">
        <h5 class="card-title">{{ event.title }}</h5>
        <form method="POST" action="/get-ticket">
          <input type="hidden" name="event_link" value="{{ event.link }}">
          <input type="email" name="email" placeholder="Enter your email" required class="form-control mb-2">
          <button type="submit" class="btn btn-primary">Get Tickets</button>
        </form>
      </div>
    </div>
  {% endfor %}
</body>
</html>
"""

# Write files
with open(os.path.join(base_path, "scraper.py"), "w") as f:
    f.write(scraper_py)

with open(os.path.join(base_path, "app.py"), "w") as f:
    f.write(app_py)

with open(os.path.join(templates_path, "index.html"), "w") as f:
    f.write(index_html)

base_path
