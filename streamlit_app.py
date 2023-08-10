import streamlit as st

st.set_page_config(layout="wide")
st.markdown('''
<style>
.katex-html {
    text-align: left;
}
</style>''',
unsafe_allow_html=True
)

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
st.title("👋Welcome")

st.markdown(
    """
    This is a simple web app to predict the flood risk for any location in Malaysia. By keying in your location, the state that you currently living, 
    the app will return whether the place that you are living in is prone to flood or not.
    """
)

st.info("👈 Check out the flood predictor page on the left sidebar!")

st.header("How is this app created?")
st.markdown("""
            ### 0. Model Used
            """)

st.latex(r"""
         \text{Logistic Regression: } y = \beta_0 + \beta_1x_1 + \epsilon \text{, where }
         """)

st.latex(r"""
         \bullet { y} \text{ is the flood risk, as a binary outcome of 0 or 1} \\
            \bullet { \beta_0} \text{ is the intercept} \\
                \bullet { x_1} \text{ is the minimum distance between the random location and the historical flood data points} \\
         """)

st.markdown(
    """
    ### 1. Data Collection
    The flood data points are collected from the annual report published by the Department of Irrigation and Drainage Malaysia (JPS) from 2015 to 2021. Subsequently, the locations
    are geocoded using open-source geo-coding API, Nominatim. The geocoded data is then stored in a `.csv` file. Subsequently, random address is generated using [Random Address Generator](https://www.bestrandoms.com/random-address-in-my?quantity=20)
    and scrapped using Selenium. The scrapped data is then geocoded using Nominatim and stored in a separate `.csv` file. 
    
    The minimum distance between the random location and the historical flood data points are then calculated. This minimum distance represents the predictor variable in this study. For the
    response variable, the flood risk will be labelled as 1 if the minimum distance is less than 500 m and 0 otherwise.
    
    ### 2. One Hot Encoding
    Since during model fitting, logistic regression requires at least 2 columns of independent variable, the categorical variable, state, is encoded using one hot encoding. 
    This is to ensure that the model is able to interpret the categorical variable.
    
    ### 3. Model Fitting
    The model is fitted using the `LogisticRegression` function from `sklearn.linear_model`.
    
    ### 4. Model Evaluation
    The model is evaluated using the `accuracy_score` function from `sklearn.metrics`. The model is able to achieve an accuracy of 0.9880. The model is then further evaluated with 
    confusion matrix, training and test set score, receiver operating curve (ROC) as well as cross-validation. Of course, comparisons were made with other models such as KNN, SVM,
    XGB and more. However, logistic regression is chosen as it is able to achieve a high accuracy score with only slightly poor performance compare to XGB classifier (less than 0.05 difference).
    
    ### 5. Conclusion
    1. The logistic regression model accuracy score stood at 0.988. The model does a very good job in predicting whether a location in Malaysia has or has no risk of flooding.
    2. From the validation set, we can see that there are several locations with flood risk and several with no flood risk
    3. There's no sign of overfitting of the model
    4. We have also checked that by changing the threshold we can improve the model's performance
    5. We also have a high ROC AUC which approx to `1`. This means that this classifier does a very good job in flood risk prediction
    6. From the model confusion matrix, we can see that there are only a few false positives and false negatives
    7. We also found that cross validation as well as grid search cross validation tend to improve slightly the model performance.
    
    > Results and analysis can be found on the **Documentation page** on the left sidebar.
       
    ### 6. Limitation of the Model
    The model is only able to predict the flood risk for the location that is within the range of the historical flood data points. This is because the model is trained using the historical flood data points.
    Of course the model is also limited by the flood data points itself as the data is not completed due to unsuccessful geocoding and a lot of flood points are lost. Furthermore, the 
    random location generated are not evenly distributed throoughout the states in Malaysia with a high concentration in some states but not the other. This can also affect the model
    as most of the location are determined by the success of the geocoding process.
    
    Moreover, the distance is calculated by assuming that there is a flood risk within 500 m radius of any historical flood data points. This is not always true and could not be very 
    reliable. Based on the distance data collected, the mean is about 1000 m and the 25% percentiels is about 413 m. 
    
    ### 7. References
    1. [Logistic Regression](https://en.wikipedia.org/wiki/Logistic_regression)
    2. [Stack Overflow - XGBoost Model Consistently Obtaining 100% Accuracy](https://stackoverflow.com/questions/48697770/xgboost-model-consistently-obtaining-100-accuracy)
    3. [Scikit-learn: Machine Learning in Python](https://scikit-learn.org/stable/index.html)
    4. [Comparing Performance of Different ML Algorithms](https://dibyendudeb.com/comparing-machine-learning-algorithms/)
    5. [Kaggle: Logistic Regression Classifier Tutorial](https://www.kaggle.com/code/prashant111/logistic-regression-classifier-tutorial/notebook)
    
    """
)