# Disaster Response Pipeline Project
### Project Motivation
The goal of the project is to classify the disaster messages into categories. Disaster data from Figure Eight is used to build a model for an API that classifies disaster messages. Through a web app, the user can input a new message and get classification results in several categories. The data provided by Figure Eight contains real messages that were sent during disaster events.

### Required Libraries
- Pandas for data manipulation
- Re for regular expressions
- Scikit-Learn for machine learning
- NLTK for natural language processing
- SQLAlchemy to read and write a SQLite database
- Flask which allows user to enter a disaster message and retrieve its associated category

### Project Overview
The project contains three components:
1. **ETL Pipeline:**  `process_date.py` file containing the script to create the ETL pipeline.
2. **ML Pipeline:**  `train_classifier.py` file containing the script to create the ML pipeline.
3. **Flask Web App:**  web app which enables the user to enter a disaster message and then view the categories of the message.

### ETL Pipeline
The ETL pipeline cleans and processes the raw data for messages and categories datasets and writes the data to an SQLite database.

### Machine Learning Pipeline
The machine learning pipeline processes cleaned data from the ETL pipeline to predict classifications across **36 categories** using **multi-output classification**. The key steps include:

1. **Data Splitting**: The dataset is divided into a **training set** and a **test set**.
2. **Pipeline Construction**: A machine learning pipeline is built using:
   - **NLTK** for text processing,
   - **Scikit-learn's `Pipeline`** to streamline preprocessing and model training,
   - **`GridSearchCV`** for hyperparameter tuning.
3. **Model Training & Evaluation**: The pipeline trains on the message column and optimizes performance using cross-validation.
4. **Model Export**: The final trained model is saved as a **pickle file (`.pkl`)** for deployment.
5. **Script Integration**: The final model implementation is included in `train_classifier.py`.

### File Structure
    app
    | - template
    | |- master.html # main page of web app
    | |- go.html # classification result page of web app
    |- run.py # Flask file that runs app
    data
    |- disaster_categories.csv # data to process
    |- disaster_messages.csv # data to process
    |- process_data.py
    |- InsertDatabaseName.db # database to save clean data to
    models
    |- train_classifier.py
    |- classifier.pkl # saved model
    README.md


### Execution Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

--------------
### Screenshots
1. This is an example of the input screen where you can type in a message which will then be classified by the machine learning model. In the example below the message states "hello I see the fire from my neighbour house, I think they are in danger!"
![alt text](https://github.com/emoreno-hub/Disaster-Response-Pipelines/blob/main/Screenshots/sample_input.png)

2. After clicking on Classify Message, the classified categories associated with the message will be highlighted in green.
![alt text](https://github.com/emoreno-hub/Disaster-Response-Pipelines/blob/main/Screenshots/sample_output.png)


3. The main page shows several graphs associated with the training set.
![alt text](https://github.com/emoreno-hub/Disaster-Response-Pipelines/blob/main/Screenshots/main_page.png)

### Acknowledgements
- Figure Eight for providing the data

### Author
- Eric Moreno
