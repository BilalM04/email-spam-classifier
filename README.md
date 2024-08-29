# Email Spam Classifier

This project involves building a machine learning model to classify emails as spam or not spam. The model is trained using a dataset from Kaggle and is implemented in a Jupyter Notebook using Logistic Regression. Additionally, a Flask API is provided for interfacing with the trained model to classify emails. The API can be accessed locally by running the Flask server or through the hosted version [here](https://bilalm14.pythonanywhere.com/predict?message=). 

You can explore the frontend application and test its functionality by visiting the hosted site [here](https://bilalm04.github.io/mail-guard/). The source code for the frontend is available in a separate repository, which can be found [here](https://github.com/BilalM04/mail-guard).

## Dataset 

The dataset used for training the model is sourced from [Kaggle](https://www.kaggle.com/datasets/jackksoncsie/spam-email-dataset?resource=download) and can be found in `datasets/emails.csv`. The model, trained on this dataset, achieves an accuracy of 98.34% on the test data.

<div align="center">

![image](https://github.com/user-attachments/assets/1351fe99-8061-42b8-8ee8-87d4cc907ae5)

</div>

## Technologies Used

- **Python:** The core programming language used to develop the machine learning model and the Flask API.
- **Jupyter Notebook:** Used for implementing and testing the machine learning model.
- **Flask:** A lightweight WSGI web application framework used to create the API.
- **scikit-learn:** The machine learning library used to build and train the logistic regression model.
- **matplotlib**: A plotting library used for visualizing data and model performance.
- **pandas**: A data manipulation and analysis library used for handling datasets, including loading, cleaning, and preprocessing data.
- **numpy**: A library for numerical computations, used for handling arrays and performing mathematical operations.

## Project Structure

- `EmailSpamClassifier.ipynb`: Jupyter Notebook containing the implementation of the spam classifier model.
- `models/`: Directory where the trained model and feature extractor are saved.
- `datasets/`: Directory where the datasets are stored.
- `app.py`: Flask API for interfacing with the trained model.
- `requirements.txt`: Python package dependencies.

## API Interface

1. Access the API at [https://bilalm14.pythonanywhere.com/](https://bilalm14.pythonanywhere.com/).
2. **API Endpoints:**
   - **GET / predict:** Classify an email as spam or not spam.
     - **Request Body:**
       ```json
       {
         "message": "Your email content here."
       }
       ```
     - Response:
       ```json
       {
         "message": "Your email content here.",
         "prediction": "spam or not spam"
       }
       ```
3. Example Request:
   - **Request:** [https://bilalm14.pythonanywhere.com/predict?message=click%20here%20to%20win%20free%20prize](https://bilalm14.pythonanywhere.com/predict?message=click%20here%20to%20win%20free%20prize)
      ```json
      {
        "message": "click here to win free prize"
      }
      ```
   - **Response:**
     ```json
     {
       "message": "click here to win free prize",
       "prediction": "spam"
     }
     ```

## Running Locally

### Dependencies

1. Clone the repository.
   ```
   git clone https://github.com/BilalM04/email-spam-classifier.git
   ```
2. Naviagte to the project directory.
   ```
   cd email-spam-classifier
   ```
3. Ensure you have Python and Jupyter Notebook installed.
4. Install project dependencies.
   ```
   pip install -r requirements.txt
   ```

### Jupyter Notebook

1. Launch the Jupyter Notebook server by running the following command.
   ```
   jupyter notebook
   ```
2. Open `EmailSpamClassifier.ipynb` in the Jupyter Notebook server.
3. Edit `input_mail` to test your own input.
   ```python
   input_mail = [""]
   ```
4. Execute the code to see the result.

### Flask API

1. Start the Flask server.
   ```
   python app.py
   ```
2. Use the same endpoints as described in the API Interface section, but for local use, the URL root will be `http://127.0.0.1:####/`, where `####` is the port number.

## Frontend

The frontend for this project is a web application built using React.js and styled with CSS. It allows users to input email messages and receive a classification of whether the email is spam or not. The frontend communicates with this backend API to utilize the machine learning model for classification. You can explore the frontend application and test its functionality by visiting the hosted site [here](https://bilalm04.github.io/mail-guard/). The source code for the frontend is available in a separate repository, which can be found [here](https://github.com/BilalM04/mail-guard).





