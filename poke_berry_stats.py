from data_extraction import url_request, web_scraping, extracting_json
from data_transformation import transforming_data
from data_load import load_to_csv
from log_process import log_progress
import matplotlib.pyplot as plt

poke_url = "https://pokeapi.co/docs/v2#berries-section"
stats_output_file = "poke-API_statistics.csv"
raw_output_file = "all_berries_data.csv"
log_file = "log_file.txt"

log_progress("Requesting data to pokeAPI", log_file)
api_request = url_request(poke_url)

log_progress("Performing some web scraping to gather data...", log_file)
berry_url_template = web_scraping(api_request)[0]
headers = web_scraping(api_request)[1]

log_progress("Extracting juice from berries...", log_file)
berry_df = extracting_json(berry_url_template, headers)

log_progress("Transforming berries data", log_file)
transfromed_berry_df = transforming_data(berry_df)

log_progress("Generating CSV file", log_file)
load_to_csv(transfromed_berry_df, stats_output_file)
load_to_csv(berry_df, raw_output_file)

log_progress("Ploting Histogram", log_file)
plt.figure(figsize=(8, 6))
plt.hist(transfromed_berry_df['frequency_growth_time'].values[0].keys(), weights=transfromed_berry_df['frequency_growth_time'].values[0].values(), bins=len(transfromed_berry_df['frequency_growth_time'].values[0]))
plt.title('Frequency of Growth Time')
plt.xlabel('Growth Time')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()