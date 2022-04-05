from flask import Flask
from flask import render_template
app = Flask(__name__)
from nyt import get_pdf
from datetime import datetime
from datetime import timedelta

@app.route('/')
def main():
    today = datetime.now()
    today_str = f'{today.year}-{today.month:02}-{today.day:02}'
    print('today',today_str)
    yesterday = today - timedelta(days=1)
    yesterday_str = f'{yesterday.year}-{yesterday.month:02}-{yesterday.day:02}'
    try:
        open(f'images/{today_str}.jpg','r')
    except:
        print('[W] Generating PDF')
        get_pdf()
    return render_template(
        '_main.html',
        today=today_str,
        yesterday=yesterday_str,
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002)
