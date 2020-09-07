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

