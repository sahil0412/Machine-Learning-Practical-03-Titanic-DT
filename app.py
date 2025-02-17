from flask import Flask,request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            Pclass=float(request.form.get('Pclass')),
            Age = float(request.form.get('Age')),
            SibSp = float(request.form.get('SibSp')),
            Parch = float(request.form.get('Parch')),
            Fare = float(request.form.get('Fare')),
            Cabin = request.form.get('Cabin'),
            Sex = request.form.get('Sex'),
            Embarked= request.form.get('Embarked')
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)
        if results == 0:
            survive = "NOT"
        else:
            survive = ""
        return render_template('results.html',final_result=survive)






if __name__=="__main__":
    app.run(host='0.0.0.0', port = 8080,debug=True)