import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.utils import resample
import pickle

class ChurnPredictionModel:
    def __init__(self, data, target_column, drop_columns=None):
        # Initialize the model with default hyperparameters
        self.data = data
        self.target_column = target_column.lower()
        self.drop_columns = drop_columns
        self.model = RandomForestClassifier()
    
    def preprocess_data(self):
        # Preprocess the data
        list_columns = []

        for i in self.data.columns:
            col = i.lower()
            list_columns.append(col)

        self.data.columns = list_columns
        self.data = self.data.drop(columns=self.drop_columns)

        data_preprocess = self.data.copy()
        # Identify and preprocess categorical columns
        categorical_columns = [col for col in data_preprocess.select_dtypes(include=['object']) if col not in [self.target_column]]
        
        for col in categorical_columns:
            if data_preprocess[col].nunique() == 2:  # Binary values
                le = LabelEncoder()
                data_preprocess[col] = le.fit_transform(data_preprocess[col])
            else:  # More than two unique values
                ohe = OneHotEncoder(sparse=False)
                encoded_cols = pd.DataFrame(ohe.fit_transform(self.data[[col]]))
                data_preprocess = pd.concat([data_preprocess, encoded_cols], axis=1)
                data_preprocess = data_preprocess.drop(columns=[col])


        return data_preprocess

    def train(self, data):
        # Split the data into features (X) and target (y)
        X = data.drop(columns=[self.target_column])
        y = data[self.target_column]

        # Handle class imbalance using resampling
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Upsample the minority class (churned customers)
        data_train = pd.concat([X_train, y_train], axis=1)
        churned = data_train[data_train[self.target_column] == 1]
        not_churned = data_train[data_train[self.target_column] == 0]
        
        # Handle imbalance using undersample
        proportion_target = churned.shape[0]*100/(churned.shape[0] + not_churned.shape[0])
        print(churned.shape[0], not_churned.shape[0])
        print("Propoortion Target Churn is {}".format(proportion_target))
        
        if proportion_target < 30: 
            #undersampling
            not_churned_sample = resample(not_churned, replace=True, n_samples=len(churned), random_state=42)
            data_train_all = pd.concat([not_churned_sample, churned])
            print(not_churned_sample.shape[0])
        else:
            data_train_all = pd.concat([not_churned, churned])
        
        
        X_train_process = data_train_all.drop(columns=[self.target_column])
        y_train_process = data_train_all[self.target_column]

        # Train the model
        self.model.fit(X_train_process, y_train_process)
        
        # Make predictions on the test set
        y_pred = self.model.predict(X_test)

        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)

        return accuracy, report

    def export_model(self, model_filename):
        # Export the trained model to a pickle file
        with open(model_filename, 'wb') as model_file:
            pickle.dump(self.model, model_file)
    
    def load_model(self, model_filename):
        # Load a trained model from a pickle file
        with open(model_filename, 'rb') as model_file:
            self.model = pickle.load(model_file)

    def eda_visualization(self, data):
        # Perform EDA and visualize data
        sns.set(style="whitegrid")
        plt.figure(figsize=(12, 6))
        sns.countplot(data=data, x=self.target_column, palette='Set1')
        plt.title("Churn Distribution")
        plt.show()