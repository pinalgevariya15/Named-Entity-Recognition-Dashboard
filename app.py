import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path
from ner_processor import extract_entities

st.set_page_config(
    page_title="NER Analytics Dashboard",
    page_icon="📰",
    layout="wide"
)


st.title("📰 Named Entity Recognition Dashboard")

st.markdown(
    """
    **Analyze named entities across multiple articles using spaCy NER.**

    This dashboard identifies and analyzes:
    - 👤 **PERSON**
    - 🏢 **ORGANIZATION**
    - 📍 **LOCATION**
    """
)

st.divider()

# PROCESS ARTICLES

data_folder = Path("data")

all_entities = []
article_count = 0


for file in data_folder.glob("*.txt"):

    article_count += 1

    text = file.read_text(encoding="utf-8")

    entities = extract_entities(text)

    for entity in entities:

        entity["article"] = file.name

        all_entities.append(entity)

# CHECK DATA

if not all_entities:

    st.warning("No entities were found in the articles.")
    st.stop()

# CREATE DATAFRAME

df = pd.DataFrame(all_entities)

# ENTITY FREQUENCY

frequency_df = (
    df.groupby(["entity", "type"])
    .size()
    .reset_index(name="frequency")
)

frequency_df = frequency_df.sort_values(
    "frequency",
    ascending=False
)

# SIDEBAR

st.sidebar.title("🔎 Dashboard Controls")

entity_filter = st.sidebar.selectbox(
    "Select Entity Type",
    ["ALL", "PERSON", "ORG", "LOCATION"]
)

# FILTER DATA

if entity_filter == "ALL":

    filtered_df = frequency_df

else:

    filtered_df = frequency_df[
        frequency_df["type"] == entity_filter
    ]
    
# METRICS

col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "📄 Articles",
    df["article"].nunique()
)

col2.metric(
    "🔤 Total Entities",
    len(df)
)

col3.metric(
    "🎯 Unique Entities",
    frequency_df["entity"].nunique()
)

col4.metric(
    "📊 Entity Types",
    frequency_df["type"].nunique()
)


st.divider()

# ENTITY FREQUENCY TABLE

st.subheader("📊 Entity Frequency")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)


st.divider()


# TOP ENTITY CHART

st.subheader("📈 Top Entities by Frequency")


chart_df = (
    filtered_df
    .sort_values("frequency", ascending=False)
    .head(15)
)


fig = px.bar(
    chart_df,
    x="frequency",
    y="entity",
    color="type",
    orientation="h",
    title="Top Entities by Frequency"
)


fig.update_layout(
    yaxis={"categoryorder": "total ascending"},
    xaxis_title="Frequency",
    yaxis_title="Entity",
    height=500
)


st.plotly_chart(
    fig,
    use_container_width=True,
    key="entity_frequency_chart"
)


# FOOTER

st.divider()

st.caption(
    "Built using Python • spaCy • Pandas • Streamlit • Plotly"
)