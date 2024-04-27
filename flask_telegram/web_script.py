from flask import Flask, redirect, url_for, request, render_template
import requests
app = Flask(__name__)

#Bot name = @shai444bot
TOKEN = "7146877031:AAF16FIQN3oaGjcYDS4Q7kecGJ0d8XUzUz0"
chat_id = "529919876"

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/success', methods=['GET'])   
def botsend():
        
        message = "hello from your telegram bot"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json()) # this sends the message
        return (requests.get(url).json())


@app.route('/', methods=['POST', 'GET'])
def login():
        cred = request.form.get('nm')


        if not cred:
            error = 'you must fill something man!'
            return render_template('index.html', error=error)
        else:
      	    return redirect(url_for('success', name=cred))

@app.route('/success', methods=['GET'])
def success(name):
         
      	    return f'hello {name}'





if __name__ == '__main__':
    app.run(debug=True)