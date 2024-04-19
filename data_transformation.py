import pandas as pd
import numpy as np

def transforming_data(dataframe):
    """
    This function receives a dataframe in order to calculate the required statistics.
    Then a new dataframe is generated and returned for the new calculations
    """

    headers = ["berries_names",
               "growth_times",
               "min_growth_time",
               "median_growth_time",
               "max_growth_time",
               "variance_growth_time",
               "mean_growth_time",
               "frequency_growth_time"]
    
    growth_time_list = dataframe["growth_time"].to_list()
    berry_names = dataframe["name"].to_list()
    min_growth_time = np.min(growth_time_list)
    median_growth_time = np.median(growth_time_list)
    max_growth_time = np.max(growth_time_list)
    variance_growth_time = np.var(growth_time_list)
    mean_growth_time = np.mean(growth_time_list)

    frequency_growth_time = {}
    for growth_time in growth_time_list:
        frequency_growth_time[growth_time] = growth_time_list.count(growth_time)

    calculations = [berry_names,
                    growth_time_list,
                    min_growth_time,
                    median_growth_time, max_growth_time,
                    variance_growth_time, mean_growth_time,
                    frequency_growth_time]
    
    records = dict(zip(headers, calculations))
    transformed_df = pd.DataFrame.from_dict([records])
    return transformed_df
