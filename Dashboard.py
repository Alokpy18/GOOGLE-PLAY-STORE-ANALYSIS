import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
#page configuration
st.set_page_config(
    page_title="Google Play Store Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

#title
st.title("📊 Google Play Store Analysis Dashboard")

st.markdown(
    """
    ### Google Play Store Data Analysis
    This dashboard presents the visual outputs from Task 1 to Task 6.
    """
)

st.divider()

#dashboard summary output
st.subheader("📌 Dashboard Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Tasks", "6")

with col2:
    st.metric("Charts", "6")

with col3:
    st.metric("Analysis Type", "Google Play Store")


st.divider()

#Task 1
st.header("1️⃣ Task 1 — Grouped Bar Chart")

st.write(
    "Shows category-wise Google Play Store analysis "
    "using the Task 1 visualization."
)

task1_file = Path("Task_1_Grouped_Bar_Chart.html")

if task1_file.exists():

    html_code = task1_file.read_text(encoding="utf-8")

    components.html(
        html_code,
        height=600,
        scrolling=True
    )

else:
    st.error("Task 1 HTML file not found.")


st.success(
    "Output: Category-wise comparison is displayed using a Grouped Bar Chart."
)


st.divider()

#Task 2
st.header("2️⃣ Task 2 — Choropleth Map")

st.write(
    "Shows the geographical distribution of Google Play Store data."
)

task2_file = Path("task_2_choropleth_map.html")

if task2_file.exists():

    html_code = task2_file.read_text(encoding="utf-8")

    components.html(
        html_code,
        height=650,
        scrolling=True
    )

else:
    st.error("Task 2 HTML file not found.")


st.success(
    "Output: Country-wise distribution is displayed using a Choropleth Map."
)


st.divider()

#Task 3
st.header("3️⃣ Task 3 — Dual Axis Chart")

st.write(
    "Compares two different measures using a Dual Axis Chart."
)

task3_file = Path("Task_3_Dual_Axis_Chart.html")

if task3_file.exists():

    html_code = task3_file.read_text(encoding="utf-8")

    components.html(
        html_code,
        height=650,
        scrolling=True
    )

else:
    st.error("Task 3 HTML file not found.")


st.success(
    "Output: Two measures are compared together using a Dual Axis Chart."
)


st.divider()

#Task 4
st.header("4️⃣ Task 4 — Time Series Line Chart")

st.write(
    "Shows changes in Google Play Store data over time."
)

task4_file = Path("Task_4_Time_Series_Line_Chart.html")

if task4_file.exists():

    html_code = task4_file.read_text(encoding="utf-8")

    components.html(
        html_code,
        height=650,
        scrolling=True
    )

else:
    st.error("Task 4 HTML file not found.")


st.success(
    "Output: Time-based trends are displayed using a Time Series Line Chart."
)


st.divider()

#Task 5
st.header("5️⃣ Task 5 — Bubble Chart")

st.write(
    "Shows the relationship between different variables "
    "using bubble size and position."
)

task5_file = Path("Task_5_Bubble_Chart.html")

if task5_file.exists():

    html_code = task5_file.read_text(encoding="utf-8")

    components.html(
        html_code,
        height=650,
        scrolling=True
    )

else:
    st.error("Task 5 HTML file not found.")


st.success(
    "Output: Relationship between variables is displayed using a Bubble Chart."
)


st.divider()

#Task 6
st.header("6️⃣ Task 6 — Stacked Area Chart")

st.write(
    "Shows category-wise changes and cumulative trends over time."
)

task6_file = Path("Task_6_Stacked_Area_Chart.html")

if task6_file.exists():

    html_code = task6_file.read_text(encoding="utf-8")

    components.html(
        html_code,
        height=700,
        scrolling=True
    )

else:
    st.error("Task 6 HTML file not found.")


st.success(
    "Output: Category-wise trends over time are displayed using a Stacked Area Chart."
)


st.divider()

#final output
st.header("🎯 Final Dashboard Output")

st.info(
    """
    This dashboard combines the visual outputs of all six tasks
    into one place.

    Task 1 → Grouped Bar Chart
    Task 2 → Choropleth Map
    Task 3 → Dual Axis Chart
    Task 4 → Time Series Line Chart
    Task 5 → Bubble Chart
    Task 6 → Stacked Area Chart
    """
)


st.caption(
    "Google Play Store Data Analysis"
)


