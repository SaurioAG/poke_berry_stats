import requests
import pandas as pd
import re
import json
from bs4 import BeautifulSoup

def url_request(url: str):
    """
    This function will do a request to the given url and return a response object
    """
    request = requests.get(url)
    return request

def web_scraping(request):
    """
    This function receives a response object and parses the text on it to gather specific data
    Returns the berry url template and a list of tupples with attribute names and descriptions
    """
    soup = BeautifulSoup(request.text, features = "html.parser")
    list_url_templates = []
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        if "GET https://" in paragraph.text:
            pattern = r" .*"
            url_template = re.search(pattern, paragraph.text)[0].strip()
            list_url_templates.append(url_template)
            if "/berry/{" in url_template:
                pattern = r"\{[\w ]+\}\/"
                berry_url_template = re.sub(pattern, r"", url_template)
    tables = soup.find_all('tbody')
    rows = tables[2].find_all('tr')
    list_name_desc = [(row.find_all('td')[0].text.strip(), row.find_all('td')[1].text.strip()) for row in rows]
    return (berry_url_template, list_name_desc)

def extracting_json(url, headers):
    """
    This function receives an url template that serves as base to construct the complete url
    for each existing berry on the pokeAPI. Then gets all the json data as a string and casts
    it to pyhton dict. Then creates each berry data dict is stored in a list to later populate
    a dataframe which is returned.
    """
    berry_id = 1
    json_request = url_request(f'{url}{berry_id}')
    code = json_request.status_code
    berry_dict = {}
    list_berries = []
    while code == 200:
        json_request = url_request(f'{url}{berry_id}')
        berry_data = json.loads(json_request.text)
        for header in headers:
            key = header[0]
            if key in ["firmness", "item", "natural_gift_type"]:
                berry_dict[key] = berry_data[key]["name"]
            elif key == "flavors":
                berry_dict[key] = str(berry_data[key])
            else:
                berry_dict[key] = berry_data[key]
        list_berries.append(berry_dict.copy())
        berry_id += 1
        json_request = url_request(f'{url}{berry_id}')
        code = json_request.status_code
    berry_df = pd.DataFrame.from_dict(list_berries)
    return berry_df
