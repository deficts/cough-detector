from flask import Flask, render_template, request
import os
import hmm1
import hmm

UPLOAD_FOLDER = './static/uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

hmm_models = hmm.main()
print(hmm_models)
hmm1_models = hmm1.main()
print(hmm1_models)
wavRecording = None

@app.route('/audio', methods=['POST'])
def audio():
    with open('static/uploads/audio.wav', 'wb') as f:
        f.write(request.data)
        f.close()
    global wavRecording
    wavRecording = "static/uploads/audio.wav"
    return "Recorded succesfully"

@app.route("/", methods=['GET','POST'])
def index():
    Cough = ""
    #En este if checo la elección de los algoritmos
    if request.method == 'POST':
        #Aqui se obtiene el path del archivo
        path = None
        if(wavRecording is not None):
            path = wavRecording
        else:
            f = request.files['file']
            if f.filename != '':
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
                path = UPLOAD_FOLDER+f.filename
            else:
                return 

        algs = request.form.get('algs')
        

        if(algs == "alg1"):
            print(path)
            Cough = hmm.evaluate(hmm_models,path)
        else:
            print(path)
            Cough = hmm1.evaluate(path,hmm1_models)

    return render_template('index.html', Cough = Cough)



if __name__ == '__main__':
    app.run(debug=True)