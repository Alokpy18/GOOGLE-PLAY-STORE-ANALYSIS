# GOOGLE-PLAY-STORE-ANALYSIS USING PYTHON

## TASK-1 - Grouped Bar Chart 

## Description 

This task analyzes the top 10 app categories based on total installs.

The dataset was cleaned and filtered using:
- Rating >= 4.0
- Size >= 10 MB
- Last Updated in January

Category-Wise total installs, average rating, and total reviews were calculated.

A Plotly grouped bar chart was created to compare average rating and total review count. The chart is configured to be available only between 3 PM to 5 PM.

## Output

## INSIGHTS
- The Family category has the highest total review count indicating strong user engagement.
- The Personalization category has one of the highest average ratings among the top 10 categories.
- Most of the selected app categories have an average rating above 4.0, showing positive user satisfaction.
- The number of reviews varies significantly across categories, with Family and Game having much higher review counts than several other categories.

# Task-2 - Interactive Choropleth Map 

### Objective
Created an interactive Choropleth Map using Plotly to visualize country-wise app installs.

### Work Done 
- Applied 6 pm to 8 pm time restriction.
- Converted 2-letter country codes to 3-letter country code.
- Create an interactive plotly Choropleth Map.
- Saved the map as an HTML file.

### Tools used 
python, pandas, plotly

### Output


### Insight

- The map helps compare app installations across different countries interactively.
- The USA has one of the highest app install volumes shown on the map.
- Countries like India, Brazil, and the UK also show high app installations compared to many other countries.



# Task 3 - Dual Axis Chart

## Objective
Compare the average installs and revenue of Free vs Paid apps within the Top 3 app categories.

## Filters Applied
- Installs >= 10000
- Paid Revenue >= $10000
- Android Version > 4.0
- Size > 15 MB
- Content Rating = Everyone
- App Name <= 30 characters
- Time restriction: 1 PM - 2 PM

## Tools Used 
- Python
- pandas
- NumPy
- plotly

## Insights
- Game-Free has the highest average installs among the categories shown.
- Tools-Paid has the highest average revenue in the chart.
- Paid apps have lower installs but can generate much higher revenue than Free apps.

## Output

## Task 4 - Time Series Line Chart 

## Objective
Analyze the monthly install trends by app category and identify significant growth.

## Work done
- Calculate monthly category-wise total installs.
- Calculate MoM Growth.
- Highlighted growth above 20%.
- Time Restriction 6 PM - 9PM.

## Insights
- Communication has the highest install trend.
- Some categories show significant growth above 20%.
- Installs increase sharply in the later months.
