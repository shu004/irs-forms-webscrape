from bs4 import BeautifulSoup
import requests
import json
import sys

BASE_URL = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html"

def get_product_results(product_number):
    """return all products by product_number"""

    all_results = []

    #start at first page
    index_first_row = 0

    while True:
        search_param = f"{BASE_URL}?indexOfFirstRow={index_first_row}&sortColumn=sortOrder&value={product_number}&criteria=formNumber&resultsPerPage=200&isDescending=false"

        #getting response from url and turn response to soup to start scraping
        response = requests.get(search_param).text
        soup = BeautifulSoup(response, "html.parser")

        #find all the rows with the class name
        all_rows = soup.find_all("tr",  {"class": ["even", "odd"]})

        # invalid input, did not find any search result on page with user's input
        if not all_rows:
            return []

        # valid input, start looping through row
        for row in all_rows:
                #assigning each td of the row to a variable
                form_number = row.find("td", class_="LeftCellSpacer").get_text(strip=True)
                title = row.find("td", class_="MiddleCellSpacer").get_text(strip=True)
                year = row.find("td", class_="EndCellSpacer").get_text(strip=True)
                link = row.find("a")["href"]

                # If product name matches the input product name
                if form_number.lower() == product_number.lower():

                    #add result to all results list
                    all_results.append({
                        "form_number": form_number,
                        "form_title": title,
                        "form_year": year,
                        "form_link": link
                    })

        # continue looping through rest of the pages
        # ex: results: 201 - 400 of 440 files
        num_of_files_section = soup.find(class_="ShowByColumn").get_text(strip=True).split()
        num_of_files_total = int(num_of_files_section[-2])
        num_of_files_on_page = int(num_of_files_section[-4])

        # when we've searched through all results
        if num_of_files_total == num_of_files_on_page:
            break

        # if we still have more to search, then move on to next page
        index_first_row += 200

    return all_results #a list of dictionaries



def result_to_form(search_results):
    """turn result to the requested form"""

    return {"form_number": search_results[0]["form_number"],
            "form_title": search_results[0]["form_title"],
            "min_year": int(search_results[-1]["form_year"]),
            "max_year": int(search_results[0]["form_year"])}




def search_for_irs_forms(product_numbers):
    """return search result to json file"""

    result = []
    for product_number in product_numbers:
        search_results = get_product_results(product_number)
        if not search_results:
            print(f"No search results for {product_number}, please check that it's a valid IRS form")
            quit()
        form = result_to_form(search_results)
        result.append(form)

    return result



#call user_input function when this file runs
if __name__ == '__main__':

    form_names_to_search_for = sys.argv[1:]

    #if they did not put any arguements in command line
    if not form_names_to_search_for:
        print("Welcome to IRS Form Scraper!")
        print('Usage: python scrape.py "<form_name>" "<form_name>" ...')
        print()
        print('For example: python scrape.py "Form W-2" "Form W-2 P"')
        # Return with non-zero exit code to indicate failure
        exit(1)
        
    print(json.dumps(search_for_irs_forms(form_names_to_search_for), indent=4))

