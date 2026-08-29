# Import pandas for data manipulation 
import pandas as pd

#Import the plotly graph objects for creating the grouped bar chart
import plotly.graph_objects as go

#Import datetime for checking the current time
from datetime import datetime
from zoneinfo import ZoneInfo

#Load the google play store dataset 
df = pd.read_csv('googleplaystoredata.csv')
print(df.head())

#Check the number of rows and columns
print(df.shape)

#Display all column names
print(df.columns.tolist())
print(df.dtypes)

#check missing values in each column
print(df.isnull().sum())

#Remove rows where rating is missing 
df = df.dropna(subset = ["Rating"])

#Check the remaining missing values in rating 
print(df["Rating"].isnull().sum())
print(df.shape)

#Convert rating and reviews columns into numeric values
df["Rating"] = pd.to_numeric(df["Rating"], errors='coerce')
df["Reviews"] = pd.to_numeric(df["Reviews"], errors='coerce')

#Create a function to convert Installs into numeric values
def convert_installs(value):
    #convert the value to string
    value = str(value)
    #Remove commas and plus signs
    value = value.replace(',', '').replace('+', '')

    #convert the cleaned value into a number
    return pd.to_numeric(value, errors='coerce')

#Apply the function to the Installs column
df["Installs"] = df["Installs"].apply(convert_installs)
print(df["Installs"].head())

#create a function to convert app size into MB
def convert_size(value):

    #return missing value if the value is not available
    if pd.isna(value):
        return None
    #convert the value to string and remuve extra spaces
    value = str(value).strip()

    #return missing value for "varies with device"
    if value == "Varies with device":
        return None

    #convert values given in MB
    if "M" in value:
        return float(value.replace("M", ""))
    #convert values given in KB into MB
    elif "k" in value:
        return float(value.replace("k", "")) / 1024
    else:
        return None
    #create a new column containing size in MB
df["size_MB"] = df["Size"].apply(convert_size)
print(df[["Size", "size_MB"]].head())

#convert the last updated column into datetime format
df["Last Updated"] = pd.to_datetime(df["Last Updated"], errors='coerce')
print(df["Last Updated"].head())

#Filter the dataset according to the task requirements
filtered_df = df[
    (df["Rating"] >= 4.0) &
    (df["size_MB"] >= 10) &
    (df["Last Updated"].dt.month == 1)
].copy()

#display the number of rows remaining after filtering
print(len(filtered_df))

#Group the filtered data by app category 
category_data = filtered_df.groupby("Category").agg(

    #calculate total installs for each category
    Total_installs = ("Installs", "sum"),

    #calculate average rating for each category
    Average_rating = ("Rating", "mean"),

    #calculate total review count for each category
    Total_reviews = ("Reviews", "sum")

).reset_index()

#Display the category_wise results
print(category_data.head())

# Sort categoory by total installs in descending order
top10 = category_data.sort_values(by="Total_installs", ascending=False).head(10)

print(top10)



#Get the current time according to india standard time
current_time = datetime.now(ZoneInfo("Asia/Kolkata"))

#Display the current time
current_hour = current_time.hour

#Check whether the current time is between 3 pm and 5 pm
if 15 <= current_hour < 17:
    #create an empty plotly figure 
    fig = go.Figure()

    #Total Rating
    fig.add_trace(go.Bar(
        x = top10["Category"],
        y = top10["Average_Rating"],
        name = "Average Rating",
        yaxis = "y1"
    )
    )

    #Total Reviews Count
    fig.add_trace(go.Bar(
        x = top10["Category"],
        y = top10["Total_reviews"],
        name = "Total Reviews",
        yaxis = "y2"
    )
    )

    #Update the layout of the figure
    fig.update_layout(
        barmode = "group",
        title = "Top 10 App Categories:Average Rating vs Total Reviews Count",

        # configure the primary y-axis
        yaxis1 = dict(
            title = "Average Rating",
        ),

        # secondary y-axis
        yaxis2 = dict(
            title = "Total Reviews Count",
            overlaying = "y",
            side = "right"
        ),

        #Label the x-axis
        xaxis = dict(
            title = "App Category"
        ),

        template = "plotly_white"
    )
    fig.show()

    #Save the interative chart as an html file
    fig.write_html("Task_1_Grouped_Bar_Chart.html")

else:
    print("Chart is available only between 3 PM to 5 PM IST")






