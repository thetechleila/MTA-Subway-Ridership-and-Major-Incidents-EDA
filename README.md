# The Effects of Major Incidents on MTA Subway Ridership from 2020 to 2024
## *An Exploratory Data Analysis*
___

## Project Description 

Utilizing the *MTA Daily Ridership Data: 2020-2025* dataset and the *MTA Subway Major Incidents: Beginning 2020 dataset* available through both [NY Open Data](https://opendata.cityofnewyork.us/) and [data.ny.gov](https://data.ny.gov/), four independent exploratory data analyses were conducted to generate relevant hypotheses and identify possible hidden patterns after measuring any changes in MTA Subway Ridership for 2020-2024 when taking major incidents into consideration.
___

### _What are Major Incidents?_ 
Major Incidents are occurrences that delay 50 or more trains. These are the most likely to cause the highest about of disruption for MTA Subway Riders.
___
### _The Types of Major Incidents tracked by the MTA include:_ 
- __Track:__ Track incidents have a variety of root causes including low quality maintenance (especially when trains are moving at high speed), mistakes and confusion from train operators (this includes ignoring signals, incorrect breaking, and even speeding)
- __Persons on Trackbed/Police/Medical__
- __Signals:__ The various types Signals in the MTA Subway System are manually operated by human operators in signal towers, not automatically by the trains themselves. They are meant to prevent track divergences, control train speed, maintain safe train operation around curves, detect issues with wheels and more. The infrastructure of the MTA Subway system is severely in need of 21st century upgrades and lags behind most comparable subway infrastructures globally
- __Stations and Structure__
- __Subway Car__
- __Other__

___

## Dataset Details

* [*MTA Daily Ridership Data: 2020-2025*](https://data.ny.gov/Transportation/MTA-Daily-Ridership-Data-2020-2025/vxuj-8kew/data_preview)
    * 1776 rows, 15 Columns (*as of April 4, 2025*)

* [*MTA Subway Major Incidents: Beginning 2020*](https://data.ny.gov/Transportation/MTA-Subway-Major-Incidents-Beginning-2020/j6d2-s8m2/about_data)


___
## Execution

**Phase I: Web-Scraping**
* The *MTA Daily Ridership Data: 2020-2025* and the *MTA Subway Major Incidents: Beginning 2020* 
datasets were scraped from the source's public API using:
    * BeautifulSoup
    * Importing Requests
    * JSON

(*Please note that both datasets are still actively recording and storing data about MTA Subway Ridership & Major Incidents as of April 3, 2025.*)

**Phase II: Data Cleaning and Wrangling**
* Scraped data from *MTA Daily Ridership Data: 2020-2025* and *MTA Subway Major Incidents: Beginning 2020* were converted into CSV files.
* The *MTA Daily Ridership Data: 2020-2025* dataset was split into 2 separate CSV files due to its immense size


The _MTA Daily Ridership Data: 2020-2025_ dataset and the _MTA Subway Major Incidents: Beginning 20202_ dataset were either combined or filtered into 5 separate CSV files in order to more easily analyze the large amount of data. The data was pulled from both APIs with code detailed in three .py files = incidents.py, daily_ridership.py, and merge.py.


___

## Repository Story

* This repository is a clone of the first exploratory data analysis I've ever conducted at The Knowledge House Technology Fellowship during late January 2025-early February 2025 with a team of 3 other fellows.
* It contains updates, spelling and grammatical fixes, more contextual information, and an "images" folder containing all visualizations