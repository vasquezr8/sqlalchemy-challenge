# Climate Analysis and Flask API Design

## Background

I decided to treat myself to a long holiday vacation in Honolulu, Hawaii. To help with trip planning, I chose to conduct a climate analysis of the area using Python, SQLAlchemy, and Flask. Here's how I accomplished this task:

### Part 1: Analyzed and Explored the Climate Data

In this section, I used Python and SQLAlchemy to perform a basic climate analysis and data exploration of the climate database. Here are the steps I followed:

1. **Connected to the Database**: I used the provided files (`climate_starter.ipynb` and `hawaii.sqlite`) to connect to the SQLite database using SQLAlchemy's `create_engine()` function.

2. **Reflected Tables into Classes**: Utilizing SQLAlchemy's `automap_base()` function, I reflected the tables into classes and saved references to the classes named `station` and `measurement`.

3. **Created a Session**: I established a SQLAlchemy session to interact with the database.

4. **Precipitation Analysis**: I conducted a precipitation analysis by finding the most recent date in the dataset, obtaining the previous 12 months of precipitation data, and plotting the results.

5. **Station Analysis**: I performed a station analysis to calculate the total number of stations, find the most-active stations, and retrieve temperature observation data for the most-active station.

6. **Closed the Session**: Remembering to close my session at the end of my notebook.

### Part 2: Designed My Climate App

After completing the initial analysis, I designed a Flask API based on the queries developed. Here's how I designed the Flask routes:

1. **Homepage**: I started at the homepage and listed all available routes.

2. **/api/v1.0/precipitation**: I converted the query results from the precipitation analysis to a dictionary and returned the JSON representation.

3. **/api/v1.0/stations**: I returned a JSON list of stations from the dataset.

4. **/api/v1.0/tobs**: I queried temperature observations of the most-active station for the previous year of data and returned a JSON list.

5. **/api/v1.0/<start> and /api/v1.0/<start>/<end>**: I returned a JSON list of the minimum, average, and maximum temperatures for a specified start or start-end range.

## Code Citation

Sort a Pandas data frame using ascending and inplace parameters:
(Found in input cell 10 of climate_starter.ipynb file)

https://python-forum.io/thread-31451.html
