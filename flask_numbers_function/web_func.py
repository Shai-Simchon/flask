from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index2.html')
    
    
    else:
        
        if request.method == 'POST':
            num1 = int(request.form.get('num1'))
            num2 = int(request.form.get('num2'))
            result = num1 + num2
        
            return render_template('index2.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
