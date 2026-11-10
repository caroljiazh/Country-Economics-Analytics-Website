# CS 257 Website 
Group B members: Caroline Zhang, Lola Feurer, Gray Driscoll

## Summary of our App and Intended Audience
This app allows a user to search through datasets to find information about women in government in various countries, average literacy rate in a country, or average education during a time period in a certian country. Upon opening the app, the user is greeted with a pleasant and intuitive website, and the easy-to-understand visualization of data makes it user-friendly to a vast audience. Although a vast audience may use it, this app is geared towards individuals who have a desire to learn  about the various pieces of data. The easy visualization makes this a readily available tool in the classroom for any teachers hoping to get their students interested in global education &equality affairs.

## How to Run the App
1. Run:
```bash
python3 app.py <port>
```
2. In a browser, navigate to `http://127.0.0.1:<port>/`

## Summary of our Datasets
We used three datasets for this project. Our data covers the years of education, percentage of women in local government, and literacy rate across various countries. Our data for education and literacy rate begins in 1870, or whenever countries began reporting after that. Data for women in local governments begins in 2007, but not every country reports during the same years. This is the biggest limitation of our datasets: there is no pattern for the years in which a country has data or not. We worked around this limitation in our functions that search for most recent data, but it causes issues with our `Averge years of education` search function. If the user enters a "dead year", they will be lead to a 500 error page, and even if the start and end years have data, there may be "dead points" where the graph drops to zero because data was not reported.

Citations:
Our World in Data —  Average years of education for 15-64 years olds (July 17, 2023)
Date of Download April 9, 2026
Liscence Creative Commons BY Barro and Lee (2015), Lee and Lee (2016), with major processing by Our World in Data

Our World in Data — Literacy rate (June 11, 2025)
Date of Download April 9, 2026
Liscence: Creative Commons BY UNESCO (1957), UNESCO (1953), Buringh and van Zanden (2009), van Zanden, J. et al., UNESCO Institute for Statistics (2025), with major processing by Our World in Data

Out World in Data - Inter-Parliamentary Union and UN Women (October 29, 2025)
Date of Download April 9, 2026
Liscence Creative Commons BY Inter-Parliamentary Union and UN Women via UN SDG Indicators (https://unstats.un.org/sdgs/dataportal), UN Department of Economic and Social Affairs (accessed 2025). 

## Team Member Implementations
Disclaimer! Caroline and Gray talked this over and we realized we do not remember who implemented what exactly, this is a best estimate but is likely imprecise. Most of our functions we wrote when meeting as a group so we all contributed to every part of the project.

Caroline:
- Women in gov
- About the page
- Proposed Literacy Rate function

Gray:
- Women in gov (we each made different versions of the same function)
- Data cleaning
- Proposed Homepage design

Lola:
- Years of schooling
- Style.css
- Proposed the Graph and progress bars

Everything else we worked on together and it is not possible to attribute to only one person.

## Important Information
The port range should be between 5000 and 5150.
Some countries may use alternate spellings than the user is accustomed to.
