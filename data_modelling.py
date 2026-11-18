import pandas as pd

# This is the cleaning function for all research questions.

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Unified data cleaning function for all research questions
    Remove dublicates
    Fill missing values with Unknown
    Standardize column names
    Convert date column to  datetime
    Return the cleaned dataframe
    """
    # remove duplicates
    df = df.drop_duplicates()

    # handle missing values (fill missing values with 'unknown')
    df = df.fillna("unknown")

    # standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
      
    # convert date column to datetime
    if "birth_date" in df.columns:
        df["birth_date"] = pd.to_datetime(df["birth_date"], format = "%Y-%m-%d",errors="coerce")
        df["birth_year"] = df["birth_date"].dt.year #this extract the year from birth_date

    return df
