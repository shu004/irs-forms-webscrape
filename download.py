from bs4 import BeautifulSoup
import requests
import os
from scrape import get_product_results
import sys

def download_irs_forms():

    product_number = sys.argv[1].title()
    year_range = sys.argv[2]
    years = year_range.split("-")

    # check if user put in a range or just a year
    if len(years) < 2:
        min_year = int(years[0])
        max_year = int(years[0])
    else:
        min_year = int(years[0])
        max_year = int(years[1])

    #get all product by product_number
    all_form_results = get_product_results(product_number)

    #get the current directory
    current_dir = os.getcwd()

    #create new path with current directory and form name
    new_path = os.path.join(current_dir, product_number)

    #if the directory doesn't already exist, create new one with form name
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    os.chdir(product_number)

    #get a filtered results with the desired years
    filtered_results = {}

    # check to see the year exists in all of the results, if so, add to dictionary
    for result in all_form_results:
        form_year = int(result["form_year"])
        if form_year in range(min_year, max_year + 1):
            filtered_results[form_year] = result

    # if the year is inside of filtered results, download the file
    for year in range(min_year, max_year + 1):
        if year in filtered_results:
            download_form(filtered_results[year], new_path)
        else:
            print(f"Sorry, we cannot find any forms for {year}.")



def download_form(form, new_path):
    """downloading file to directory"""
    res = requests.get(form["form_link"])

    file_name = os.path.join(new_path, f"{form['form_number']} - {form['form_year']}")
    with open(f"{file_name}.pdf", "wb") as file:
        file.write(res.content)



if __name__ == '__main__':

    form_name_and_years_to_download = sys.argv[1:]
    #if they didn't put any arguement:
    if not form_name_and_years_to_download:
        print()
        print("Welcome to IRS Form Downloading Tool!")
        print('Usage: python download.py "<form_name>" "<year range (inclusive)>"')
        print()
        print('For example: python download.py "Form W-2" "2018-2020"')
        # Return with non-zero exit code to indicate failure
        exit(1)

    download_irs_forms()
