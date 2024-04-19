# poke_berry_stats

This API gathers berry information from https://pokeapi.co/docs/v2#berries-section in order to generate statistics

## INSTALLATION

LANGUAGE

As this API was written in Python, you will need to install Python 3.10

DEPENDENCIES

Also, for correct execution, following dependencies are needed:

- bs4  0.0.2
- pandas  2.2.1
- requests  2.31.0
- numpy  1.26.4
- matplotlib  3.8.3
- pytest  8.1.1

OS

API was developed on Windows 10

## MODULES

data_extraction.py: This module handles the extraction of all needed data from the consumption API "https://pokeapi.co/docs/v2#berries-section" via web scraping technique.
All this data extraction is handled thru 3 functions, which at the end return a Dataframe contaiening raw data from all berries

data_transformation.py: This module uses the berries raw data Dataframe as an input, in order to wrangle the data and generate some statistics from it.
Returning a new dataframe with the wrangled data

data_load.py: This module is in charge of generating two CSV files that reports as follows:
  - all_berries_data.csv: Raw data from all berries found on https://pokeapi.co/docs/v2#berries-section API
  - poke-API_statistics.csv: Statistics generated from the raw data of all berries

log_process.py: Just a module that handles generating an informative log of the complete process.

poke_berry_stats.py: Main script that you need to execute in order to generate CSV reports, an Histogram based on statistics and the log file.

test_all_stages.py: Some unittest just to ensure that functions do what they are supposed to do.

## WORKFLOW

Execute main script poke_berry_stats.py on your favorite IDE, the flow is as follows:

data_extraction -> data_transformation -> data_load


Cheers!
