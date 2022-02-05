# IRS Form Information Tool


## Scraper part (should have better name)

### How to use

```console
$ python scrape.py "form w-2"
[
    {
        "form_number": "Form W-2",
        "form_title": "Wage and Tax Statement (Info Copy Only)",
        "min_year": 1954,
        "max_year": 2022
    }
]
```

You can save it to a file!
```console
$ python scrape.py "form w-2" > irs_info.json
```


# IRS Form Informational Tool

## Description:
Write two different uitilies to search IRS tax forms on `https://apps.irs.gov/app/picklist/list/priorFormPublication.html`
1. Take in a list of forms and returns a formatted json.
2. Take in a form name and a range of year, download the PDFs in a folder of the current directory.

## Setup:
1. Clone this repo: `https://github.com/shu004/irs-webscrape.git`
2. Initiate and activate a virtual environment
    * virtualenv venv
    * source ./venv/bin/activate
3. Install dependencies
    * pip3 install -r requirements.txt

### Part 1: Scraping the web:



## Set-Up
1. Clone this repo:
    * `cd <your_desired_directory>`
    * `git clone https://github.com/katalinschmidt/webscraping.git`
2. Set-up the virtual environment:
    * `virtualenv env`
    * `source env/bin/activate`
    * `pip3 install -r requirements.txt`
3. For webscraper 1 / form results as JSON data:
    * `$ python3 scrape_forms.py`
    * Input: as prompted
    * Output: new file '/query_results.json' containing JSON data
4. For webscraper 2 / form results as PDF downloads:
    * `$ python3 scrape_downloads.py`
    * Input: as prompted
    * Output: new subdirectory '/{desired_form_name}' containing PDFs

## Additional Thoughts
There are numerous popular webscraping tools and each tool has its own advantages and disadvantages.

In preparation for this project, I looked into the following webscraping tools:
* BeautifulSoup
    * User-friendly
    * Requires dependencies => difficult to transfer code
    * Inefficient (for scaling / larger projects)
* Selenium
    * Versatile (e.g. automated-testing within the same framework)
    * Works well with Javascript
    * Not user-friendly (i.e. not designed w/webscraping in mind)
* Scrapy
    * Efficient (for scaling / larger projects)
    * Written in Python framework => asynchronous capabilities
    * No dependencies => portable
    * Not user-friendly

Due to my personal time constraints, I decided to use BeautifulSoup for this project.
Selenium and Scrapy are tools that I am still unfamiliar with, but look forward to learning!

There are also many ways I could have designed the input/output of information for this project.
For example, shell commands for redirecting and piping could have been required or, to more closely emulate as REST API,
I could have developed a small Flask web application with 'webscraper 1' in particular as an endpoint.

Another design choice I made was to use logging as my tool for debugging.
Given the nature of the raw HTML being returned by GET requests and then being manipulated with BeautifulSoup,
I needed an easy way to read and assess the large amount of data that was the end result of each of these functions and
felt that exporting that data to a separate log file would be the best way to accomplish that.
Logging is something I had not done before, so I greatly appreciate the practice this project has afforded me with that.