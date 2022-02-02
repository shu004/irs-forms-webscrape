from bs4 import BeautifulSoup
import requests
import os
from scrape import get_form_results

from scrape import BASE_URL

BASE_URL = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html"

form_name = "Form W-2"

#user input
#check for user input edge cases

ui_year_range = "2018-2020"
#think about cases where range doesnt exist or "2018-"
#check for valid input?
year_range = ui_year_range.split("-")

#check to see if the
if len(year_range) < 2:
    min_year = int(year_range[0])
    max_year = int(year_range[0])
else:
    min_year = int(year_range[0])
    max_year = int(year_range[1])

search_results = get_form_results(form_name)


current_dir = os.getcwd()

#create new path with current directory and form name
new_path = os.path.join(current_dir, form_name)

#if the directory doesn't already exist, create new one with form name
if not os.path.exists(new_path):
    os.makedirs(new_path)

os.chdir(form_name)

for result in search_results:
    if int(result['form_year']) >= min_year and int(result['form_year']) <= max_year:
        pdf_link = result["form_link"]

        res = requests.get(pdf_link)

        file_name = os.path.join(new_path, f"{result['form_number']} - {result['form_year']}")
        with open(f"{file_name}.pdf", "wb") as file:
            file.write(res.content)

