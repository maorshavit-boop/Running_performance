This project classifies runners into performance tiers (Beginner, Intermediate, Advanced) using running metrics and a derived General Running Performance Score (GRPS). It includes feature engineering, unsupervised clustering (KMeans), supervised learning (Logistic Regression, Decision Tree, Random Forest, Gradient Boosting) and model evaluation.

**1. Problem Statement -**  
    - <u>Objective:</u> Classify runners into perforance tiers (Beginner / Intermediate / Advanced) based on running metrics. Compare between Clustering to true labels.  
**2. Data Collection -**  
    - based on friends' running data (Garmin Connect, RunKeeper, Apple Watch, Nike run club, Strava)  
    - Kaggle - "Running Log Insight", "Running races from Strava", "strava-data"  
**3. Method**  
    - Gather the datasets and create a median run for each runner, than use the running metric chosen and run the model.  
    - Using Riegel formula - https://trainasone.com/ufaq/riegels-formula/ to create a custom running metric (named GRPS in the project).   
    - Splitting the data to train and test by using traintestsplit function (splits randomly the data to train split and test split, sizes can be determine by the user) and Cross Validation (divides the data to multiple 'folds', every time using different 'fold' as the test split and running the model than aggregate the model results and returns their average).     
    - Classification models - Decision Tree, Logistic Regression, Random Forest, Gradient Boosting.  
    - Clustering model - K-means  
