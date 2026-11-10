# User Stories - to be completed

## User Story 1: Change in Literacy Rates Over Time

As an educational researcher, I want to see how literacy rates for the United States have changed for the recent years.

**Acceptance Criteria**
- Given a country name, the program returns the country's first recorded literacy rate, most recent recorded literacy rate, and the percent change between the two.
- If no data exists for the selected country, the program returns a message indicating that there is no data.
- If only one data point exists for the selected country, the program returns a message indicating that there is not enough data to calculate growth. 

**Acceptance Tests**
- `python3 ProductionCode/command_line.py --country "Mexico" --growth`
  prints out first data point for literacy in Mexico, most recent data point, and percent growth for Mexico
- `python3 ProductionCode/command_line.py --country "bob" --growth`
  prints out a message indicating that there is no data for the given country.
- `python3 ProductionCode/command_line.py --country "Netherlands" --growth`
  (with our mock dataset) prints that there are not enough data points for the country. 

## User Story 2: Average Years of Schooling by Country

As a student interested in global education trends, I want to look up the percentage of average years of schooling in my country (France) for a given start and end year.

**Acceptance Criteria**
- Given a specific country name and a 5 year time range, the program returns the average schooling data for that country for those years, sorted by year in chronological order on a chart and table
- Given two country names and a year range, the program displays their schooling data side by side for comparison and the chart updates to show trends for both countries over the selected years
- If no data exists for the selected filters, the chart and table are empty

**Acceptance Tests**
- `python3 ProductionCode/command_line.py --country "France" --stat schooling --start 2000 --end 2005`
  prints schooling data (table and graph) for France sorted by year for that range
- `python3 ProductionCode/command_line.py --country "France" --stat schooling --start 2000 --end 2005`
  and `python3 ProductionCode/command_line.py --country "Germany" --stat schooling --start 2000 --end 2005`
  prints schooling data (table and graph) for Germany and France for the same range, allowing comparison
- `python3 ProductionCode/command_line.py --country "Hi" --stat schooling --start 2000 --end 2005`
  prints "No schooling data found for 'Hi'."


## User Story 3: Recent Data About Women in Government

As a politican interested in women representation, I would like to know the percentage of women in my local government (France).

**Acceptance Criteria**
- Given a category ("Literacy rate", "women in gov", "years of schooling") the program should return the five countries with the highest and lowest of the corresponding statistics
- Countries did not provide data from corresponding years, the program should factor in the most recent data of its catagory in each country

**Acceptance Tests**
- `python3 ProductionCode/command_line.py --category "years of schooling"`
   Prints out the top and lowest five countries by average years of schooling, checks country that we know should be at the top is included
- `python3 ProductionCode/command_line.py --category "women in gov"`
   Prints out the top and lowest five countries by percentage of women in local gov, checks country that we know should be at the top is included
- `python3 ProductionCode/command_line.py --category "literacy rate"`
   Prints out the top and lowest five countries by literacy rate, checks country that we know should be at the top is included
- `python3 ProductionCode/command_line.py --category "Snowman stats"`
   Checks random categories are safely dealt with.
  
