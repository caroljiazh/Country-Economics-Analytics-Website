import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask
from ProductionCode.datasource import *
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def homepage():
    """default page"""
            # "This is the home page. See below for URL formatting: <br><br>"
            # "http://127.0.0.1/literacy_rate/&lt;country&gt;<br>"
            #  "To see average literacy rate in a country, or <br>"
            #  "http://127.0.0.1/avg_schooling/&lt;country&gt;/&lt;start_year&gt;/&lt;end_year&gt; <br>"	
            #  "To see the average schooling in a country between two years, or <br>" 
            #  "http://127.0.0.1/women_in_gov/&lt;country&gt;<br>"
            #  "To see the percentage of women in government of a country <br>"
    return render_template('home_page.html')

@app.route('/literacy_rate')
def flask_get_countries_literacy_rate():
    """displays literacy rate for a given country
    Args: 
        country (str): the name of the country to look at. Retrieved from the route
    Returns: 
        the result of the call to function get_countries_literacy_rate
    """
    country = request.args.get('country')
    connection = connect()
    result = get_countries_literacy_rate(connection, country)
    connection.close()
    if not result:
        return render_template('invalid_country.html')
    percentage = round(result[-1][2], 1) if result else 0
    return render_template('results_literacy.html', country=country, percentage=percentage)
 
@app.route('/avg_schooling')
def flask_country_avg_schooling():
    """displays average years of schooling for a country in a certain time period
    Args: 
        country (str): the name of the country to look at. Retrieved from the route
        start_year(int): the start year (retrieved from second variable in the route)
        end_year(int): the end year (retrieved from final part of route)
    Returns: 
        the result of the call to function country_avg_schooling
    """
    country = request.args.get('country')
    start_year = request.args.get('start_year')
    end_year = request.args.get('end_year') 
    try:
        start_year = int(start_year)
        end_year = int(end_year)
    except (TypeError, ValueError):
        return render_template('invalid_year.html')
    if (start_year > end_year) or (start_year % 5 != 0) or (end_year % 5 != 0):
        return render_template('invalid_year.html')

    connection = connect()
    result = country_avg_schooling(connection, country, start_year, end_year)
    connection.close()
    if not result:
        return render_template('invalid_country.html')
    return render_template('results_schooling.html', years=result)

@app.route('/women_in_gov')
def flask_get_women_gov_by_country():
    """displays percentage of women in government in a given country"""
    country = request.args.get('country')
    connection = connect()
    result = get_women_gov_by_country(connection, country)
    connection.close()
    if not result:
        return render_template('invalid_country.html')
    percentage = round(result[-1][2], 1) if result else 0
    return render_template('results_women.html', country=country, percentage=percentage)

@app.route('/about')
def about():
    """displays about page"""
    return render_template('about_page.html')

@app.errorhandler(404)
def page_not_found(e):
     """
     Handles not found errors, returns a guide for valid url."""
     return render_template('404_page.html')

@app.errorhandler(500)
def python_bug(e):
     """Handles Errors caused by unhandled exceptions in the app."""
     return render_template('500_page.html')

if __name__ == '__main__': 
   # Uses one command-line argument: the port number to run on
   if len(sys.argv) != 2:
       print("Usage: python3 app.py <port>")
       sys.exit(1)
    
   app.run(port=int(sys.argv[1]), host = "stearns.mathcs.carleton.edu")