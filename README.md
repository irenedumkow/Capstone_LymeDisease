## Project Definition

### Project Overview
This is the final projec for the Udacity Data Scientist Nanodegree. For all the other projects in the Nanodegree, quite some guidance was provide. The final project is designed to show of what was learned in the course and involved:
- Deciding on a dataset to use
- Finding out and deciding which steps to take to turn a real world dataset into a clean dataset
- Deciding if a machine learning pipeline or a web application will be handed it
- If needed, taking refinement steps

I decided to look at health data, in particular data for cases of Lyme disease in the US between 2008 and 2021 (Source: [Lyme Disease Cases in the US between 2008 and 2021](https://healthdata.gov/CDC/Lyme-disease-public-use-aggregated-data-with-geogr/n9dr-4pe8/about_data)). This is the kind of data where it is most helpful if the public can play around with the data and derive conclusions themself, therefore I decided to develop a web application

### Problem Statements
The web application can help people explore the data for themself and answer questions like
- How does the number of cases change over the course of the year in my county or in all of the US?
- Are there difference in the case numbers between women and men?
- ...

#### Installation

This project was developed using the following Python version and Python libraries
- dash 2.14.2
- dash bootstrap-components 1.7.1
- flask 3.0.3
- jason
- numpy 1.26.4
- pandas 2.3.1
- plotly 6.0.1


#### Files in this repository
- Lyme_Disease.ipynb: Jupyter notebook representing the ETL pipeline to read in the data, transform it and load (save) it in three files which can be loaded into the web application
- Lyme_disease_public_use_aggregated_data_with_geography__2008-2021.csv downloaded from https://healthdata.gov/CDC/Lyme-disease-public-use-aggregated-data-with-geogr/n9dr-4pe8/about_data
- geojson-counties-fips.json: Needed for correlating FIPS and counties in visualization
- fips2county.tsv: Helper file, currently not needed
- app.py: Webapplication for visualizing the number of cases of Lyme disease between 2008 and 2021, broken down to counties
- The assets/data folder contains three csv.files
    - df_age_cat_yrs.csv: Contains the year, FIPS and columns for the different age categories
    - df_case_status.csv: Contains the year, FIPS and columns for the case status
    - df_sex.csv: Contains the year, FIPS and columns for the sex

#### Running the app

Starting the app by typing:
`python app.py`
Then open a browser and type in: `http://127.0.0.1:8050/`

It will first start with empty maps of the US. By selecting a year the maps with by filled with the data und one can use the radio buttons to look at different segments of the data.

## Analysis

In this project for it is actually more important to learn how to deal with real world data than to actually draw conclusions.

This project clearly shows for me that it is always important to know where the data comes from and how it was processed before it is visualized in any way.

During the dataprocessing I realized that not every data point was split down to the county level, but was giving them on the state level. For my analysis I decided to drop these lines, but for a real world analysis a more thorough investigation would be needed, which would answer questions like: 
- If only the state is given, is it just a summary of the data for the state, then dropping would be fine, because otherwise data would be counted twice.
- Or are we loosing data by dropping these lines?
- As real people are involved, maybe they understood the questions differently and the answer depends on the state/clerk entering the data?

For the Suppressed and the Unknown values in the Age, Cases Status and Sex category a closer look could also be worthwile. Here I decided not to drop these lines but also add a Total column because otherwise too much information would be lost.

As real world data never is perfect it is always important to keep in the back of the head that in cleaning the data some information will always be lost.

It is also important to note that using modules and libraries it is relatively easy to draw this visualization, things still can go wrong and one would also need to think about plausibilty checks. I realized that Conneticut including Lyme is not represented on the visualization, even though it is in the data set. And given the high numbers there, it would completely change the visual impression.

What can be said about the data, with the caveats given above:
- Over time more and more counties have cases of Lyme disease, but mostly on the East Coast, around the Great Lakes and in the West.
- In the East a larger area is involved, but the number in the counties are lower. From this analysis one can not deduct if the total of cases have risen or fallen between 2008 and 2021.
- Especially in the East one need to be careful if talking about Confirmed, Probable or the sum of both.
- The gender does not make much of a difference.
- Lyme disease is more of a disease of grown-up (20+) than of children (0-19).

## Conclusion

The app is a good start to visualize the development of the number of Lyme disease cases in the US and especially to show the spread over the country over the years. And looking at a picture is a lot easier than looking at the bare numbers in a table.

On the other end I learned again that a lot of things can go wrong in a visualization like what happened to Conneticut and even though a visualization can be very suggestive, one also needs to question them.

Also there is still a lot to do to turn it into a really good visualization.
- Finding a better color scale
- Giving the option of changing the maximum number, at the moment it is fixed and is the maximum number of cases for the whole table.
- Centering everything.
- Different font.
- ...

#### Reference for the code development
[Develop Data Visualization Interfaces in Python with Dash](https://realpython.com/python-dash/)

[Writing a simple plotly dash app](https://medium.com/@jandegener/writing-a-simple-plotly-dash-app-f5d83b738fd7)

[Dash Python User Guide](https://dash.plotly.com/), especially the Dash Fundamentals


