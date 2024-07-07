# Titanic Survival 

## Installation Guide
1. Clone or Fork the Project
2. Create a Virtual Enviroment
3. go to same virtual enviroment and write below cmd
4. pip install -r requirements.txt


### 1. Project Description
#### A. Problem Statement
We will be using a decision tree to make predictions about the Titanic data set from Kaggle. This data set provides information on the Titanic passengers and can be used to predict whether a passenger survived or not.

#### B. Tools and Libraries
Tools<br><br>
a.Python<br>
b.Jupyter Notebook<br>
c. Flask<br>
d. HTML<br>
e. Render<br>
f. GitHub

Libraries<br><br>
a.Pandas<br>
b.Scikit Learn<br>
c.Numpy<br>
d.Seaborn<br>
e.Matpoltlib<br>

### 2. Data Collection

The dataset contains 891 observations of 12 variables:<br>


PassengerId: Unique Id of a passenger<br> 
survived:    Person survived or not<br> 
pclass:    Ticket class<br>
Name: Name of the passanger<br>
sex:    Sex<br>
Age:    Age in years<br>
sibsp:    # of siblings / spouses aboard the Titanic <br>   
parch:    # of parents / children aboard the Titanic <br> 
ticket:    Ticket number<br>
fare:    Passenger fare<br> 
cabin:    Cabin number<br> 
embarked:    Port of Embarkation<br>



### 3. EDA
#### A.Data Cleaning
There is no need of three columns such as passengerId, Name and Ticket Number, so those columns can be dropped<br>
We can add SibSp and Parch column as well since both represent no of persons aboarded more and drop those 2 columns as well<br>
Now We have 8 columns and null values are present, so null values should be handled<br>
Null values for numerical columns can be handled via median stargegy and for categorical columns mode can be applied<br>
Dependent Variable is survived

#### B. Feature Engineering
No outliers are present in the data

#### C. Data Normalization
Normalization (min-max Normalization)<br>
In this approach we scale down the feature in between 0 to 1<br>
There are different ways by which we can convert categorical cols to numerical cols such as ->
1. Label Encoding -> Label Encoding converts categorical values to numerical values by assigning a unique integer to each category. This is useful for ordinal categorical variables.
2. One-Hot Encoding -> One-Hot Encoding creates binary columns for each category. This is useful for nominal categorical variables.
3. Ordinal Encoding -> Ordinal Encoding is used when the categorical variable has a natural order but no fixed spacing between the categories.
4. Frequency Encoding -> Frequency Encoding replaces categories with their frequency in the dataset.
5. Target Encoding -> Target Encoding replaces categories with the mean of the target variable for each category. This is more advanced and should be used carefully to avoid data leakage.

We use ordinal encoding to convert categorical cols to numerical cols in our use-case

We have numerical column where we can apply min-max Normalization.<br>

### 4. Choosing Best ML Model
List of the model that we can use for our problem<br>
a. Decision Tree<br>

### 5. Model Creation
So,using a Decision Tree we got good accuracy of 83%, we can Hyperparameter tuning for best accuracy.

Algorithm that can be used for Hyperparameter tuning are :-

a. GridSearchCV<br>
b. RandomizedSearchCV<br>

Main parameters used by Decision Tree Algorithm are :-
a. criterion -> For classification: 'gini' (default) or 'entropy'.
b. max_depth -> The maximum depth of the tree. If None, nodes are expanded until all leaves are pure or contain fewer than min_samples_split samples.
c. min_samples_split -> The minimum number of samples required to split an internal node. Default is 2.
d. min_samples_leaf -> The minimum number of samples required to be at a leaf node. Default is 1.
e. max_leaf_nodes -> Grow a tree with max_leaf_nodes in best-first fashion. Best nodes are defined as relative reduction in impurity. If None (default), then unlimited number of leaf nodes.
f. max_features -> The number of features to consider when looking for the best split. <br>
`None` (default): Consider all features.

### 6. Model Deployment
After creating model ,we integrate that model with beautiful UI. for the UI part we used HTML and Flask. We have added extra validation check also so that user doesn't enter Incorrect data. Then the model is deployed on render

### 7. Model Conclusion

Model predict 83% accurately on test data.

### 8. Project Innovation
a. Easy to use<br>
b. Open source<br>
c. Best accuracy<br>
d. GUI Based Application

### 9. Limitation And Next Step
Limitation are :-<br>
a. Mobile Application<br>
b. Accuracy can be improved more<br>
d. Feature is limited

Next Step are :-<br>
a. we can work on mobile application<br>

## Deployable Link
https://machine-learning-practical-03-titanic-dt.onrender.com/predict