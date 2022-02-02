from bs4 import BeautifulSoup
import requests
import json

BASE_URL = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html"


def get_form_results(product_number):
    """return all forms by product_number"""

    all_results = []

    #start at first page
    index_first_row = 0

    while True:
        search_param = f"{BASE_URL}?indexOfFirstRow={index_first_row}&sortColumn=sortOrder&value={product_number}&criteria=formNumber&resultsPerPage=200&isDescending=false"

        #getting response from url and turn response to soup to start scraping
        response = requests.get(search_param).text
        soup = BeautifulSoup(response, "html.parser")

        #need to check if the response gives an error ***edge case

        #find all the rows with the class name
        all_rows = soup.find_all("tr",  {"class": ["even", "odd"]})
        for row in all_rows:
                #assigning each td of the row to a variable
                form_number = row.find("td", class_="LeftCellSpacer").get_text(strip=True)
                title = row.find("td", class_="MiddleCellSpacer").get_text(strip=True)
                year = row.find("td", class_="EndCellSpacer").get_text(strip=True)
                link = row.find("a")["href"]

                # If product name matches the input product name
                if form_number == product_number:
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



def result_to_form(list_of_dict):
    """turn result to the requested form"""

    #check to see if the list of dict is empty, if so,
    return {"form_number": list_of_dict[0]["form_number"],
            "form_title": list_of_dict[0]["form_title"],
            "min_year": int(list_of_dict[-1]["form_year"]),
            "max_year": int(list_of_dict[0]["form_year"])}



def user_input():
    # form_input = input("Please enter a form name. (If multiple, please separate by comma):\neg: Form W-2 OR Form W-2, FORM W-2 P\n")
    # form_names = form_input.title()
    # list_of_product_numbers = form_names.split(",")
    #check for valid input
    #if one fo the form doesnt work, put form does not exist?
    list_of_product_numbers = "Form W-2, Form W-2 P, Publ 1, Publ 1 (AR)"
    splitted = list_of_product_numbers.split(', ')

    result = []
    for product_number in splitted:
        all_product_result = get_form_results(product_number)
        form = result_to_form(all_product_result)
        result.append(form)

    final_results = json.dumps(result)

    # Write JSON data to file:
    with open("scrape_result.json", "w") as file:
        file.write(json.dumps(json.loads(final_results), indent=4))
        file.close()

user_input()



