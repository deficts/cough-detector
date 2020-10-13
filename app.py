from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    #En este if checo la elección de los algoritmos
    if request.method == 'POST':
        #Al presionar el botón de testear se obtiene el valor elegido de los algortimos
        print(request.form.get('algs'))
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)