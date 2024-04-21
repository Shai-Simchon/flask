from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')




@app.route('/', methods=['POST', 'GET'])
def login():
        cred = request.form.get('nm')


        if not cred:
            error = 'you must fill something man!'
            return render_template('index.html', error=error)
        else:
      	    return redirect(url_for('success', name=cred))

@app.route('/success/<name>', methods=['GET'])
def success(name):
         
      	     return f'hello {name}'



if __name__ == '__main__':
	app.run(debug=True)
