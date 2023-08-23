# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import pandas as pd
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/date/start_date<br/>"
        f"/api/v1.0/date/start_date/end_date<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return last 12 months of precipitation data"""
    # Query last 12 months of precipitation data
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()
    
    session.close()

    # Create a dictionary from the row data and append to a list of prcp_data
    prcp_data = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict[date] = prcp
        prcp_data.append(prcp_dict)

    return jsonify(prcp_data)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations"""
    # Query all stations
    results = session.query(Station.station).all()
    
    session.close()

    # Convert list of tuples into normal list - flattens results
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of temperature observations from the most active station from the previous year"""
    # Define last year of data
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query date and temps from previous year for most active station
    results = session.query(Measurement.tobs) \
    .filter(Measurement.station == "USC00519281") \
    .filter(Measurement.date >= year_ago) \
    .all()
    
    session.close()

    # Convert list of tuples into normal list - flattens results
    frequent_station_tobs = list(np.ravel(results))

    return jsonify(frequent_station_tobs)

@app.route("/api/v1.0/date/<start_date>")
def get_date(start_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return the min, max, and average temp after a start date"""
    # Query min, max, and average temps after a given start date
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)) \
    .filter(Measurement.date >= start_date) \
    .all()

    session.close()

    # Create a dictionary from the row data and append to a list of temp_info_after_start_date
    temp_info_after_start_date = []
    for min, max, avg in results:
        temp_dict = {}
        temp_dict["min_temp"] = min
        temp_dict["max_temp"] = max
        temp_dict["avg_temp"] = avg
        temp_info_after_start_date.append(temp_dict)

    return jsonify(temp_info_after_start_date)

@app.route("/api/v1.0/date/<start_date>/<end_date>")
def between_date(start_date, end_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return the min, max, and average temp between two dates"""
    # Query min, max, and average temps between a start date and end date
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)) \
    .filter(Measurement.date >= start_date) \
    .filter(Measurement.date <= end_date) \
    .all()

    session.close()

    # Create a dictionary from the row data and append to a list of temp_info_between_dates
    temp_info_between_dates = []
    for min, max, avg in results:
        temp_dict2 = {}
        temp_dict2["min_temp"] = min
        temp_dict2["max_temp"] = max
        temp_dict2["avg_temp"] = avg
        temp_info_between_dates.append(temp_dict2)

    return jsonify(temp_info_between_dates)

if __name__ == '__main__':
    app.run(debug=True)
