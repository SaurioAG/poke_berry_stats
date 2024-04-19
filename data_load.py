
def load_to_csv(dataframe, csv_file):
    """
    This function receives a dataframe and generates a CSV file from it for reporting purposes.
    """
    dataframe.to_csv(csv_file, index = False)
