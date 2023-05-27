from flask import Flask, render_template, request
from sklearn.preprocessing import MinMaxScaler
import pickle
import numpy as np

model = pickle.load(open('pcos_test.pkl', 'rb'))

app = Flask (__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def home():

   data1 = request.form['follical_r']
   data2 = request.form['follical_l']
   data3 = request.form['weight']
   data4 = request.form['hair']
   data5 = request.form['skin']
   data6 = request.form['cycle_r']
   data7 = request.form['cycle_l']
   data8 = request.form['age']
   arr = np.array([[ data1, data2, data3, data4, data5, data6, data7, data8]])
   pred = model.predict(arr)
   if(pred==0) :
       return render_template('main.html',pred="You are less probable to be disgnosed with PCOS.") 
   
   elif (pred==1) :
       return render_template('main.html',pred="You are highly probable to be diagnosed with PCOS.") 



if __name__ == "__main__":
    app.run(debug=True)