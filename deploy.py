from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('savedmodel.sav','rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict',methods=['POST','GET'])
def predict():
    cgpa = float(request.form['cgpa'])
    internships = request.form['internships']
    projects = request.form['projects']
    workshops = request.form['workshops']
    aptitude = request.form['aptitude']
    softskills = float(request.form['softskills'])
    eca = request.form['eca']
    pt = request.form['pt']
    ssc = request.form['ssc']
    hsc = request.form['hsc']

    result = model.predict([[cgpa,internships,projects,workshops,aptitude,softskills,eca,pt,ssc,hsc]])[0]
    if result==1:
        out = 'You have chance of getting placed!!!'
    else:
        out = 'You have low chances of getting placed. All the best.'
    return render_template('out.html', output = out)

if __name__ == '__main__':
    app.run(debug=True)