import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# import the pickle files
linear_model = pickle.load(open('models/linear.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        area = float(request.form['Area'])
        bhk = int(request.form['BHK'])
        bathroom = float(request.form['Bathroom'])
        furnishing = int(request.form['Furnishing'])
        parking = float(request.form['Parking'])    
        status = int(request.form['Status'])
        transaction = int(request.form['Transaction'])
        type = int(request.form['Type'])

        data = [[area, bhk, bathroom, furnishing, parking, status, transaction, type]]
        prediction = linear_model.predict(data)
        return render_template('index.html', prediction = prediction)
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
