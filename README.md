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