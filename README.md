## End to End Machine Learning Project ##
## Link to website(sometimes takes time to open the link) - https://mlproject-w37k.onrender.com
Here's the complete content for your README that you can directly copy and paste:
Maths Marks Prediction
A web app to predict a student's math score based on gender, race/ethnicity, parental education, lunch type, test preparation, reading score, and writing score. Built with Python, Flask, and machine learning (Scikit-Learn, CatBoost, XGBoost).

Features
- Predict math scores using a trained ML model.
- Simple web interface to input data.
- Supports multiple regression models with tuning.
- Logs errors for debugging.

Project Structure
Maths_marks_prediction/
├── artifacts/ # Model, preprocessor, datasets
├── logs/ # Log files
├── notebooks/ # Dataset (stud.csv)
├── src/ # Code for data processing, training, prediction
├── templates/ # HTML templates (index.html, home.html)
├── app.py # Flask app
├── requirements.txt # Dependencies
├── setup.py # Project setup
└── README.md # This file

## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/abhisheksinha387/Maths_marks_prediction.git
   cd Maths_marks_prediction
2.	Create a virtual environment:
3.	python -m venv venv
4.	source venv/bin/activate  # Windows: venv\Scripts\activate
5.	Install dependencies:
6.	pip install -r requirements.txt
7.	Add dataset:
o	Place stud.csv in the notebooks/ folder (download it from Kaggle).
8.	Run locally:
9.	python app.py
Open http://localhost:5000 in your browser.
Usage
•	Home Page: Click "Go to Prediction Page".
•	Prediction Page: Enter gender, scores, etc., and submit to see the predicted math score.
•	Train Model: Run the following command to train the model:
•	python -m src.pipeline.train_pipeline
Training Pipeline
The train_pipeline.py is initially empty. Copy the following code into src/pipeline/train_pipeline.py:
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()

    def run_pipeline(self):
        try:
            logging.info("Starting data ingestion")
            train_data, test_data = self.data_ingestion.initiate_data_ingestion()
            logging.info("Starting data transformation")
            train_arr, test_arr, _ = self.data_transformation.initiate_data_transformation(train_data, test_data)
            logging.info("Starting model training")
            r2_score = self.model_trainer.initiate_model_trainer(train_arr, test_arr)
            logging.info(f"Model trained with R2 score: {r2_score}")
            return r2_score
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    pipeline = TrainPipeline()
    pipeline.run_pipeline()
Deploy on Render
1.	Push to GitHub:
2.	git add .
3.	git commit -m "Initial commit"
4.	git push origin main
5.	Sign up on Render:
o	Visit Render, sign up, and connect GitHub.
6.	Create Web Service:
o	Select your repo on Render.
o	Configure:
	Runtime: Python
	Build Command: pip install -r requirements.txt
	Start Command: gunicorn --bind 0.0.0.0:$PORT app:app
	Environment Variables:
	PYTHON_VERSION=3.8
	PORT=5000
7.	Pre-train model:
o	Run python -m src.pipeline.train_pipeline locally to create model.pkl and preprocessor.pkl in artifacts/.
o	Commit and push these files:
o	git add artifacts/
o	git commit -m "Add pre-trained model and preprocessor"
o	git push origin main
8.	Deploy:
o	Click Create Web Service. Once the build finishes, you can access your app at the provided URL.
9.	Update README:
o	Replace [Live App](https://your-app.onrender.com) with the actual URL in your README and push the changes.
Notes
•	Ensure stud.csv is in notebooks/ or update data_ingestion.py to fetch it online.
•	Render’s free tier may delay deployment after inactivity.
Contact
•	Author: Abhishek
•	Email: abhisheksinha.7742@gmail.com

### Render Deployment Steps
1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Add README and train_pipeline"
   git push origin main
2.	Sign Up/Login to Render:
o	Visit https://render.com, sign up, and connect your GitHub account.
3.	Create Web Service:
o	Click New > Web Service, choose your Maths_marks_prediction repo.
o	Configure:
	Runtime: Python
	Build Command: pip install -r requirements.txt
	Start Command: gunicorn --bind 0.0.0.0:$PORT app:app
	Environment Variables:
	PYTHON_VERSION: 3.8
	PORT: 5000
4.	Pre-Train Model:
o	Run locally:
o	python -m src.pipeline.train_pipeline
o	Commit artifacts/model.pkl and artifacts/preprocessor.pkl to GitHub:
o	git add artifacts/
o	git commit -m "Add pre-trained model and preprocessor"
o	git push origin main
5.	Deploy:
o	Click Create Web Service. Wait for the build to finish.
o	Access the app at the Render-provided URL.




