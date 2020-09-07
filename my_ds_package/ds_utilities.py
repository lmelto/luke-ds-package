import pandas as pd


def char_len(dataframe, text_column_name):
    """Takes in a df feature and creates a new feature with an integer length
    of characters of the passed feature.

    Args:
        dataframe (pandas df)
        text_column_name (df column name)
    """

    dataframe['text_char_len'] = dataframe[text_column_name].apply(len)

    return dataframe


def split_dates(dataframe, date_column):
    """Converts date features into pandas datetime objects.

    Args:
        dataframe (pandas dataframe)
        date_column (dataframe column)
    """

    copy_of_df = dataframe.copy()
    copy_of_df["Year"] = pd.DatetimeIndex(copy_of_df[date_column]).year
    copy_of_df["Month"] = pd.DatetimeIndex(copy_of_df[date_column]).month
    copy_of_df["Day"] = pd.DatetimeIndex(copy_of_df[date_column]).day

    return copy_of_df
