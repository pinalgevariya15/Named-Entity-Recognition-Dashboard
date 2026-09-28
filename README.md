# 📰 Named Entity Recognition (NER) Dashboard

An end-to-end NLP analytics application that extracts, aggregates, and visualizes named entities across articles using spaCy's pre-trained language models and Streamlit.

### 🌟 Key Features
- **Automated Entity Extraction**: Extracts key named entities (`PERSON`, `ORG`, and `LOCATION`) across multiple text files using spaCy's `en_core_web_sm`.
- **Interactive Analytics Dashboard**: Filter entities dynamically by type and view aggregate metrics (total articles, total entity mentions, unique entities, entity types).
- **Visual Insights**: Interactive horizontal bar charts powered by Plotly showing the top entities by frequency.
- **Batch Processing**: Normalization and frequency aggregation of entities across multi-document datasets.

### 🛠️ Tech Stack
- **NLP Engine**: [spaCy](https://spacy.io/)
- **Dashboard UI**: [Streamlit](https://streamlit.io/)
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/)
- **Visualizations**: [Plotly Express](https://plotly.com/python/)
