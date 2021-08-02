# Disaster Response Pipeline Project
### Project Motivation
The goal of the project is to classify the disaster messages into categories. Disaster data from Figure Eight is used to build a model for an API that classifies disaster messages. Through a web app, the user can input a new message and get classification results in several categories.

### Required Libraries
- Pandas for data manipulation
- Re for regular expressions
- Scikit-Learn for machine learning
- NLTK for natural language processing
- SQLAlchemy to read and write an SQLite database
- Flask which allows user to enter a disaster message and retrieve the associated category for the message

### Execution Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

### Additional Material

In the data and models folder you can find two jupyter notebook that will help you understand how the model works step by step:

    ETL Preparation Notebook: learn everything about the implemented ETL pipeline
    ML Pipeline Preparation Notebook: look at the Machine Learning Pipeline developed with NLTK and Scikit-Learn

You can use ML Pipeline Preparation Notebook to re-train the model or tune it through a dedicated Grid Search section.
