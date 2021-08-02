import sys
import pandas as pd
import numpy as np
import re
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    '''
    Parameters:
        messages_filepath: csv file containing messages
        categories_filepath: csv file containing categories
        
    Returns:
        df: combined dataframe
    '''
    
    # load messages dataset
    messages = pd.read_csv(messages_filepath)
    # load categories dataset
    categories = pd.read_csv(categories_filepath)
    
    # merge datasets
    df = messages.merge(categories, on='id')
    return df

def clean_data(df):
    '''
    Parameters:
        df: combined dataframe from load_data()
    Returns:
        df:  cleaned dataframe
    '''
    
    # create a dataframe of the 36 individual category columns
    categories = df['categories'].str.split(';', expand=True)
    
    # select the first row of the categories dataframe
    row = categories.iloc[0]
    
    # use slicing to get the characters up to the 2nd to the last character
    category_colnames = [word for word in row.apply(lambda x: x[:-2])]
    
    # rename the columns of `categories`
    categories.columns = category_colnames
    
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str [-1]
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
    
    # drop the original categories column from `df
    df.drop('categories', axis=1, inplace=True)

    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis=1, sort=False)
    
    # drop duplicates
    df = df.drop_duplicates(['id','message'])
    
    # drop child_alone column and any row that has a value of 2
    df.drop('child_alone', axis=1, inplace=True)
    df = df[df['related'] != 2]
    
    return df    
    
def save_data(df, database_filename):
    '''
    Save data for SQLite database as .db file
    '''
    engine = create_engine('sqlite:///DisasterResponse.db')
    df.to_sql('Messages', engine, index=False)
    
    pass


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
