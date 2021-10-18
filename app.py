from flask import Flask, render_template

app = Flask(__name__)

events = [
    {
        'title': 'event1',
        'date': '2021-10-15'
    },
    {
        'title': 'event2',
        'date': '2021-10-20'
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html', events=events)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)