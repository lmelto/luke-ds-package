import pandas as pd


def date_splitter(dataframe, date_column_name):
    """
    Takes a df and a column name and converts the date into a datetime
    object, then extracts the day/month/year to new features. Returns new df.
    """
    dataframe[date_column_name] = pd.to_datetime(dataframe[date_column_name],
                                                 infer_datetime_format=True)
    dataframe['Year'] = dataframe[date_column_name].dt.year
    dataframe['Month'] = dataframe[date_column_name].dt.month
    dataframe['Day'] = dataframe[date_column_name].dt.day
    dataframe.drop(date_column_name, axis=1, inplace=True)

    return dataframe

def char_len(dataframe, text_column_name):
    """Takes in a df feature and creates a new feature with an integer length 
    of characters of the passed feature.

    Args:
        dataframe (pandas df)
        text_column_name (df column name)
    """

    return dataframe['text_char_len'] = dataframe[text_column_name].apply(len)