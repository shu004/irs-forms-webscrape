from bs4 import BeautifulSoup
import requests
import os
from scrape import get_product_results
import sys

def download():

    product_number = sys
    print(product_number)
    year_range = user_input_year_range()
    #check to see if the
    if len(year_range) < 2:
        min_year = int(year_range[0])
        max_year = int(year_range[0])
    else:
        min_year = int(year_range[0])
        max_year = int(year_range[1])

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

    #looping through the all the results with input form
    for result in all_form_results:
        if int(result['form_year']) >= min_year and int(result['form_year']) <= max_year:
            pdf_link = result["form_link"]

            res = requests.get(pdf_link)

            file_name = os.path.join(new_path, f"{result['form_number']} - {result['form_year']}")
            with open(f"{file_name}.pdf", "wb") as file:
                file.write(res.content)


# def user_input_form():
#     """returns user input form name"""
#     form_name = input("Please enter a form you would like to download: \neg: Form W-2\n").title()

#     return form_name

# def user_input_year_range():
#     """returns a range of years inclusive"""
#     year_range = input("Please enter a range of years:\neg: 2018-2022\n").split("-")

#     return year_range



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

    # download()


    #check for invalid year range
#what if year doesn't exist, i want to print something?