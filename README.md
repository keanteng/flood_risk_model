# Flood Risk Regression Model <!-- omit in toc -->

![Static Badge](https://img.shields.io/badge/license-MIT-blue)
![Static Badge](https://img.shields.io/badge/python-3.11-blue)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://floodriskmodel-wdvqe2xfvx6rrusmkrprrr.streamlit.app/)

A univariate flood risk model using logistic regression trained with about 4500 labelled random geo-coordinates in Malaysia. 

A multivariate example is given [here](https://github.com/keanteng/flood_risk_model_2).

**Table of Contents:**

- [Objective](#objective)
- [Methodology](#methodology)
  - [Data Preparation](#data-preparation)
- [Limitation](#limitation)

## Objective
- To predict flood risk in any location in Malaysia
- To determine the best model describing flood risk in Malaysia

## Methodology
1. Ordinary Least Square (OLS)
    ```latex
    Y = b_0 + b_1X + e
    ``````
2. Explanation For Variables
    - `Y` is the flood risk, it can be in the form of risk score or a binary outcome if using logistic regression
    - `X` is the distance from historical flood location
    - `\beta_*` can be computed and estimated. Generally:
        - The slope should be negative as greater distance (from historical location) would reduce the flood risks
        - One unit change in distance will correspond to the change in flood risk based on the magnitude of slope
3. Some alternative to the linear regression/logistic regression approach:
    - [XGBoost](https://xgboost.readthedocs.io/en/stable/)
    - [Decision Tree](https://scikit-learn.org/stable/modules/tree.html)


### Data Preparation
To create a regression model for flood risk, we require both predictor, `x` and the response, `y` variable. 
1. The predictor variable is collected as follows:
    - Random address throughout Malaysia were scrapped and cleaned from [random address generator](https://www.bestrandoms.com/random-address-in-my) using Python `Selenium` package.
    - The addresses were then geocoded to obtain their corresponding longitude and latitude.
    - To compute for the distance from historical flood location, the following formula is applied: `distance = | npoint - point |` where `npoint` represents the nearest historical flood points and `point` represent the random address point input.
2. The response variable is collected as follows:
    - The response variable is denoted in binary form of 0 and 1 which means either it is not being flooded until now or it is flooded before. 
    - A radius of about `500m` will be drawn around each historical flood points and check for intersection, for intersected point, a value of 1 will be assigned, otherwise, 0 will be assigned. 

## Limitation
This is only a simple model with one feature: "distance to historical flood site", it might not be 100% reliable. The high accuracy from the model is perhaps due to the data labelling process where the flood coverage for all historical flood events were assumed to be the same. 

More features and a more robust data collection plan are needed to make the prediction more sound and trustable.

Internship Project © 2023
