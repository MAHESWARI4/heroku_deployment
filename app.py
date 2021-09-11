from flask import Flask, render_template, request
import joblib

#initialize the app
app = Flask(__name__)
model = joblib.load('dib_79.pkl')
print('[INFO] model loaded')

#@app.route('/')
#def hello_world():
#   return 'hello world'

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/hello')
def hello():
    return 'hello'

#welcome
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

#contact
@app.route('/contact')
def contact():
    return render_template('contact.html')
#blog
@app.route('/blog')
def blog():
    return render_template('blog.html')

#gallery
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/predict', methods = ['post'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    print(preg, plas,pres,skin,test,mass,pedi,age)
    output = model.predict([[preg, plas,pres,skin,test,mass,pedi,age]])
    if output[0]==1:
        # print('diabetic')
        ans = 'diabetic'
    else:
        # print('not diabetic')
        ans = 'non diabetic'
    # return 'Form Submitted'
    return render_template('predict.html', predict= f'the person is {ans}')
#run the app
if __name__ == '__main__':
    app.run()
# app.run(debug=True)
