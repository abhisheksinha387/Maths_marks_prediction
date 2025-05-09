from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.logger import logging
import os

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),  # Fixed
                writing_score=float(request.form.get('writing_score'))   # Fixed
            )
            pred_df = data.get_data_as_data_frame()
            logging.info(f"Prediction dataframe: {pred_df}")
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            logging.info(f"Prediction results: {results}")
            return render_template('home.html', results=results[0])
        except ValueError as ve:
            logging.error(f"ValueError in predict_datapoint: {str(ve)}")
            return render_template('home.html', error="Invalid input. Please enter valid numbers for scores.")
        except Exception as e:
            logging.error(f"Error in predict_datapoint: {str(e)}")
            return render_template('home.html', error=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)