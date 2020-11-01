from flask import Flask, render_template, request, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=['POST'])
def form():
    name = request.form.get('name')
    return render_template('form.html', name=name)


@app.route('/dojima')
def dojima():
    return render_template('dojima.html')
    

@app.route('/choice', methods=['POST'])
def choice():
    options = []
    op1 = request.form.get('op1')
    op2 = request.form.get('op2')
    op3 = request.form.get('op3')
    if op1 != None:
        options.append(op1)
    elif op2 != None:
        options.append(op2)
    elif op3 != None:
        options.append(op3)  
    return render_template('choice.html', options=options)


if __name__ == "__main__":
    app.run(debug=True)