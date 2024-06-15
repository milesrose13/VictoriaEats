# UberEats Data Scraper
After a failed attempt in gathering Victoria restaurant data via the UberEats API, we've created a script under `ubereats_scraper.py` that scrapes the UberEats webpage to gather data on available restaurants in Victoria. 

The script created gathers data about each restaurant (80 in total) with the restaurant name, restaurant url, and dishes offered by each restaurant.

The reason we weren't able to list the stores via the UberEats API, despite the endpoint existing, is due to the following message that appears in [UberEats' API documentation page for listing stores](https://developer.uber.com/docs/eats/references/api/v1/get-eats-stores):

```
Access to These APIs May Require Written Approval From Uber

Uber’s APIs are always under development and as such are subject to changes according to our Versioning & Upgrade policy. As part of Uber’s ongoing privacy improvements, we’ve updated our Developer API program with new scope access policies for third party applications. For further information, please refer to our Getting Started guides.
```

# How to run
## Python version
Ensure that you have the correct python version to run the script.

The python version used to construct the script was: `3.9`.

## Create a Python virtual environment (optional)
You are encouraged to create a virtual environment to run this, but it is not required.

To create a virtual environment, head to `csc370project > mock data` and run the following commands in a terminal of your choice:

1. `virtualenv --python=python3.9 .`
2. `source ./Scripts/activate`

Note: you may need to run a different `activate` file (found under `Scripts` after creating the Python virtual environment) depending on the terminal that you are using.

## Download required dependencies
After activating your virtual environment (see above), run `pip install -r requirements.txt` to download the required dependencies to run this script. 

## Run the script
You should now be ready to run the script by simply running `python ubereats_scraper.py`. 

## Deactivate your python virtual environment
To deactivate your python virtual environment, simply run `deactivate`.
