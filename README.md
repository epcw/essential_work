# Center for Equitable Policy in a Changing World
## Essential Workers? Modeling Equity and Human Rights during COVID-19

### Codebase
Graphing: Python-based [Plotly Dash](https://plotly.com/dash/) app.  Network model runs a [NetworkX](https://networkx.github.io/) social networking graph, using [bhargavchippada's Force Atlas 2 for Python algorithm](https://github.com/bhargavchippada/forceatlas2)\
Data crunching: Python [Pandas](https://pandas.pydata.org/) with some pre-work in MySQL to parse text files pulled from the [US Census API](https://www.census.gov/data/developers.html).

### Data sources
BLS - Local Area Unemployment Statistics 2010-2021
BLS - State and Area Employment, Hours, and Earnings 2010-2021
OSHA -  Inspection Reports for Washington State 2010-2021
US Census American Community Survey 5-year survey 2010-2019
US SBA - PPP FOIA 2020-2021
US SBA - COVID-19 Economic Injury Disaster Loans 2020-2021
Washington Employment Security Department – Workforce Supply and Demand Report 2019-2021
Washington Secretary of State – Business starts 2010-2021
City of Seattle Open Data Project – Workplace discrimination complaints 2017-2020

### Principal researchers
Richard W. Sharp\
Patrick W. Zimmerman

### Use guide (first time, run in this order)
##### Build dataframes from new data (WILL NEED TO SUPPLY NEW RAW DATA in CSV format - OUTPUT IS CSVs)
/sandbox-singlepage/data_build.sh
##### Build network graph from above dataframes
/sandbox-singlepage/build_graphs.py
##### Build maps and other graphs
/sandbox-singlepage/build_network.py
##### Launch dashboard server
/sandbox-singlepage/application.py


#### Package requirements (as well as all their dependencies)
dash\
Flask-Caching\
geopandas\
geopy\
matplotlib\
networkx\
numpy\
pandas\
scipy\
sklearn\
fa2\
rtree (usually this needs to be installed with 'sudo apt-get install python3-rtree')

### Repository Structure
.\
|-- main root folder. License and readme.\

TBA
