# IRS Form Informational Tool

## Description:
Write two different uitilies to search IRS tax forms on `https://apps.irs.gov/app/picklist/list/priorFormPublication.html`
1. Take in a list of forms and returns a formatted json.
2. Take in a form name and a range of year, download the PDFs in a folder of the current directory.

## Setup:
1. Clone this repo: `https://github.com/shu004/irs-webscrape.git`
2. Initiate and activate a virtual environment
    * `virtualenv venv`
    * `source ./venv/bin/activate`
3. Install dependencies
    * `pip3 install -r requirements.txt`

## Part 1: Scraping the Site
Use command line arguments to interact. If multiple forms, put in as multiple argument.
run below command to see examples.
```console
$ python scrape.py
```

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

or

```console
$ python scrape.py "form w-2" "publ 1"
[
    {
        "form_number": "Form W-2",
        "form_title": "Wage and Tax Statement (Info Copy Only)",
        "min_year": 1954,
        "max_year": 2022
    },
    {
        "form_number": "Publ 1",
        "form_title": "Your Rights As A Taxpayer",
        "min_year": 1996,
        "max_year": 2017
    }
]
```

You can save it to a file!
```console
$ python scrape.py "form w-2" > irs_info.json
```

## Part 2: Downloading the PDFs
Use command line arguments to interact. Input form name as an argument, a range of years as another argument.
run below command to see examples.
```console
$ python download.py
```

```console
$ python scrape.py "form w-2" "2018-2019"
```
