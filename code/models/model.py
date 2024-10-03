import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import mean_squared_error
from catboost import CatBoostRegressor
import joblib
import os
from sklearn.preprocessing import LabelEncoder
from scipy.stats import randint

# Define the path to the dataset folder
dataset_path = os.path.join(os.path.dirname(__file__), '../datasets/StudentPerformanceFactors.csv')

# Load dataset
df = pd.read_csv(dataset_path)

# Handle missing values separately for numeric and categorical columns
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Combine all object columns for encoding
object_columns = df.select_dtypes(include=['object']).columns

# Apply LabelEncoder to all object-type columns
label_encoders = {}
for col in object_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le  # Store the encoder for later use in the API

# Define features (X) and target (y)
X = df.drop(columns=['Previous_Scores'])
y = df['Previous_Scores']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the CatBoostRegressor
catboost_model = CatBoostRegressor(verbose=0, random_state=42)

# Define the hyperparameter grid for CatBoost
param_dist = {
    'iterations': randint(100, 500),
    'depth': randint(4, 10),
    'learning_rate': [0.01, 0.05, 0.1, 0.2],
    'l2_leaf_reg': randint(1, 10)
}

# Perform RandomizedSearchCV
random_search = RandomizedSearchCV(
    estimator=catboost_model,
    param_distributions=param_dist,
    n_iter=20,  # Number of random combinations to try
    scoring='neg_mean_squared_error',
    cv=5,  # 5-fold cross-validation
    random_state=42,
    n_jobs=-1  # Use all available cores
)

# Fit the RandomizedSearchCV
random_search.fit(X_train, y_train)

# Print the best parameters and best score
print(f"Best Hyperparameters: {random_search.best_params_}")
print(f"Best Cross-Validated MSE: {-random_search.best_score_}")

# Evaluate the best model on the test set
best_catboost = random_search.best_estimator_
y_pred = best_catboost.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Test Set Mean Squared Error: {mse}")

# Save the trained model and label encoders
model_save_path = os.path.join(os.path.dirname(__file__), '../models')
joblib.dump(best_catboost, os.path.join(model_save_path, 'catboost_student_performance_model.pkl'))
joblib.dump(label_encoders, os.path.join(model_save_path, 'label_encoders.pkl'))

