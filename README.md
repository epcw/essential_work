# Center for Equitable Policy in a Changing World
## Essential Workers? Modeling Equity and Human Rights during COVID-19

### Codebase
Graphing: Python-based [Plotly Dash](https://plotly.com/dash/) app.  Network model runs a [NetworkX](https://networkx.github.io/) social networking graph, using [bhargavchippada's Force Atlas 2 for Python algorithm](https://github.com/bhargavchippada/forceatlas2)\
Data crunching: Python [Pandas](https://pandas.pydata.org/) with some pre-work in MySQL to parse text files pulled from the [US Census API](https://www.census.gov/data/developers.html).

### Data source
TBA

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
