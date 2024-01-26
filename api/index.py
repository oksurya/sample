from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    url = None
    cookies = None

    if request.method == 'POST':
        url = request.form['url']

        try:
            response = requests.get(url)
            cookies = response.cookies
        except requests.RequestException as e:
            error_message = f"Error fetching URL: {e}"
            return render_template('index.html', error_message=error_message)

    return render_template('index.html', url=url, cookies=cookies)

if __name__ == '__main__':
    app.run(debug=True)
