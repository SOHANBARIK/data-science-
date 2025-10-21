import pandas as pd

def read_csv_file(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and returns its contents as a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.
    
    Returns:
        pd.DataFrame: The contents of the CSV file as a pandas DataFrame.
    """        
    return pd.read_csv(file_path)