import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(layout="wide")

st.sidebar.title("Resources:")
st.sidebar.info(
    """
    - GitHub repository: [Flood Risk Model](https://github.com/keanteng/flood_risk_model)
    - Data sources: [Flood Data](https://www.water.gov.my/)
    """
)

st.sidebar.title("Created By:")
st.sidebar.info(
    """
  Khor Kean Teng | Intern, DGA, JPS, Bank Negara Malaysia | [GitHub](https://github.com/keanteng) | [LinkedIn](https://www.linkedin.com/in/khorkeanteng/)
    """
)

# Customize page title
st.title("Analysis of Results")

st.markdown(
    """
    This page contains the analysis of the results of the flood risk prediction service that is powered by the logistic regression model.
    
    ### 1. Model Evaluation
    The model achieve a accuracy score of 0.9880, training set accuracy of 0.9928. Furthermore, the training set score and the test set score are very close to each other,
    which means that the model is not overfitting. Generally, training score measures how to model fit in the training data. If model fits so well in a data with lots of variance it results 
    in overfitting. This will result in poor test score. The mode curved a lot to fit the training data and generalized very poorly. For test score, since we implement train-test split
    before fitting model, it represents real life scenario. Thus, the higher the the test score, the better.
    
    ### 2. Confusion Matrix
    From the confusion matrix below, it can be observed that the true positive is 251, true negative is 575 while the false negative is 8 and the false positive is 2. These results show
    that our model perform very well in predicting the flood risk of a location in Malaysia. Furthermore, we compute the accuracy (0.9880), classification error (0.0120).
    precision (0.9921) and sensitivity (0.9691).
    
    Precision can be defined as the percentage of correctly predicted positive outcomes out of all the predicted positive outcomes. 
    It can be given as the ratio of true positives (TP) to the sum of true and false positives (TP + FP). Precision identifies the proportion of correctly predicted positive outcome. 
    It is more concerned with the positive class than the negative class. Recall can be defined as the percentage of correctly predicted positive outcomes out of all the actual 
    positive outcomes. It can be given as the ratio of true positives (TP) to the sum of true positives and false negatives (TP + FN). Recall is also called Sensitivity.
    """
)

image = Image.open('images/confusion_matrix.png')
st.image(image, caption='Confusion Matrix', use_column_width=True)

st.markdown(
    """
    ### 3. ROC Curve
    ROC curver stands for receiver operating characteristic curve. It shows the performance of classification model at various classification threshold levels. 
    The curve also shows the performance of a classification model at various classification threshold levels. From the image below, we can see that the area under the curve
    is closed to one. Perfect classifier will have AOC equal to 1 whereas a random classifier will have a ROC AUC equal to 0.5. Since our model ROC-AUC approximate to 1, 
    we can conclude that our classifier does a good job in predicting whether a location has a flood risk or no flood risk.
    """
)

image = Image.open('images/Log_ROC.png')
st.image(image, caption='ROC Curve', use_column_width=True)

st.markdown(
    """
    ### 4. Models Comparison
    In the above section, we have shown that logistic regression model is a good model to predict whether a location has a flood risk or no flood risk. In this section, we will compare
    several models such as XGBoost, Decision Tree Classifier, Naive Bayes, Support Vector Machine and so on. We will then evaluate all the models based on their accuracy score, area
    under curve, recall and precision. From the table below, we can see that there are several models able to attain  100% accuracy score, area under curve, recall and precision. 
    """
)

col1, col2 = st.columns(2)

with col1: 
    image = Image.open('images/MLA_train_accuracy.png')
    st.image(image, caption='Train Accuracy Score', use_column_width=True)
    
    image = Image.open('images/MLA_compare.png')
    st.image(image, caption='Test Accuracy Score', use_column_width=True)

with col2:
    image = Image.open('images/MLA Recall Comparison.png')
    st.image(image, caption='Recall', use_column_width=True)
    
    image = Image.open('images/MLA_AUC_Comparison.png')
    st.image(image, caption='Area Under Curve', use_column_width=True)
    
image = Image.open('images/ROC Curve comparison.png')
st.image(image, caption='ROC Curve Comparison', width = None)