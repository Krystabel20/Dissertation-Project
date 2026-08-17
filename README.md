# A Data-Driven Analysis of Physical Activity and Obesity in England: Investigating the Gap Between Activity Levels and Health Outcomes Using Machine Learning

MSc Data Science Individual Research Project (7005SCN), Coventry University.

This repository contains the code and artefacts for a dissertation investigating why physical activity does not translate into lower obesity outcomes across demographic and socioeconomic groups in England, and translating the findings into practical tools.

## Overview

The project uses national data derived from the Sport England Active Lives Survey, accessed through the OHID Fingertips platform, to analyse the relationship between physical activity and obesity across demographic subgroups. It applies two interpretable machine learning models and delivers an interactive decision-support tool and a dashboard.

## Live decision-support tool

The deployed tool is available at: https://weight-management-support-tool.streamlit.app/ 

## Contents

- `app.py` — the Streamlit decision-support tool
- `data_preparation.py` — the data preparation pipeline that reshapes the raw indicator extract into the analytical dataset
- `test_routing.py` — the test suite validating the tool's routing logic
- `gantt_chart.py` — generates the project timeline chart
- `Analysis.ipynb` — exploratory data analysis and machine learning models
- `processed` — the processed analytical dataset
- `raw` - the raw data taken from OHID website
- `requirements.txt` — Python dependencies

## Methods

Two interpretable classifiers, Logistic Regression and Decision Tree, were trained to predict whether a demographic subgroup exhibits above-average obesity, achieving stable cross-validated accuracies of 0.807 and 0.784 respectively. Physical inactivity, socioeconomic class and ethnicity were identified as the strongest predictors.

## Running locally

​```
pip install -r requirements.txt
streamlit run app.py
​```

## Data source

Data was obtained from the OHID Fingertips platform, with indicators derived from the Sport England Active Lives Adult Survey. The data comprises publicly available population-level aggregates and contains no personal data.

## Author

Christabel Muolokwu
