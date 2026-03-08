import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import plotly.express as px

from src.medical_priority import calculate_medical_priority
from src.conflict_risk import calculate_conflict_risk
from src.school_priority import calculate_school_priority
from src.conservation_priority import calculate_conservation_priority

st.set_page_config(
    page_title="Conservation Impact Dashboard",
    layout="wide"
)

st.title("Wildlife & Community Impact Analytics")

st.markdown(
"""
This platform helps conservation organizations decide:

• Which villages need **medical camps**  
• Where **human–elephant conflict** is highest  
• Which schools need **infrastructure support**  
• Which conservation areas need **more protection funding**
"""
)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overview",
    "Medical Camps",
    "Elephant Conflict",
    "School Infrastructure",
    "Conservation Funding"
])

# -------------------
# OVERVIEW
# -------------------

with tab1:

    st.header("Program Overview")

    medical = calculate_medical_priority()
    conflict = calculate_conflict_risk()
    schools = calculate_school_priority()
    conservation = calculate_conservation_priority()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Villages Assessed", len(medical))
    col2.metric("Conflict Areas", len(conflict))
    col3.metric("Schools Evaluated", len(schools))
    col4.metric("Conservation Zones", len(conservation))

    st.subheader("Top Priority Villages for Medical Camps")
    st.dataframe(medical.head(5)[["village","medical_score","population"]])

    st.subheader("Highest Human–Elephant Conflict Areas")
    st.dataframe(conflict.head(5)[["village","risk_score","elephant_incidents"]])


# -------------------
# MEDICAL CAMPS
# -------------------

with tab2:

    st.header("Villages Needing Medical Camps")

    df = calculate_medical_priority()

    st.subheader("Priority Ranking")
    st.dataframe(df)

    st.subheader("Top 5 Villages")

    st.table(df.head(5)[["village","population","medical_score"]])

    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        color="medical_score",
        size="population",
        hover_name="village",
        zoom=6,
        mapbox_style="open-street-map",
        title="Medical Need Map"
    )

    st.plotly_chart(fig, use_container_width=True)


# -------------------
# ELEPHANT CONFLICT
# -------------------

with tab3:

    st.header("Human–Elephant Conflict Risk")

    df = calculate_conflict_risk()

    st.subheader("Conflict Ranking")
    st.dataframe(df)

    st.subheader("Top Risk Areas")

    st.table(df.head(5)[["village","elephant_incidents","risk_score"]])

    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        color="risk_score",
        size="elephant_incidents",
        hover_name="village",
        zoom=6,
        mapbox_style="open-street-map",
        title="Elephant Conflict Risk Map"
    )

    st.plotly_chart(fig, use_container_width=True)


# -------------------
# SCHOOL INFRASTRUCTURE
# -------------------

with tab4:

    st.header("Schools Needing Infrastructure Support")

    df = calculate_school_priority()

    st.subheader("Priority Ranking")
    st.dataframe(df)

    st.subheader("Top Schools Needing Support")

    st.table(df.head(5)[["school","students","need_score"]])

    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        color="need_score",
        size="students",
        hover_name="school",
        zoom=6,
        mapbox_style="open-street-map",
        title="School Infrastructure Needs"
    )

    st.plotly_chart(fig, use_container_width=True)


# -------------------
# CONSERVATION FUNDING
# -------------------

with tab5:

    st.header("Conservation Areas Needing Funding")

    df = calculate_conservation_priority()

    st.subheader("Priority Ranking")
    st.dataframe(df)

    st.subheader("Top Conservation Funding Priorities")

    st.table(df.head(5)[["area","priority_score","poaching_incidents"]])

    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        color="priority_score",
        size="wildlife_population",
        hover_name="area",
        zoom=6,
        mapbox_style="open-street-map",
        title="Conservation Funding Priority Map"
    )

    st.plotly_chart(fig, use_container_width=True)