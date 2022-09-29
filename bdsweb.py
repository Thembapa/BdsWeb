from flask import Flask, render_template, session, redirect, request, flash, url_for, send_from_directory

app = Flask(__name__, static_url_path='')
app.secret_key = "bdswebapp"

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(palletBarcode = None):

    return render_template('index.html')

if __name__ == "__main__":
    #serve(app,host='192.168.14.7', port=1407)
    app.run()
