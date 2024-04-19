# filters.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

def load_dataset(dataset_file):
    # Load dataset from CSV file
    dataset = pd.read_csv('C:/Users/karun/OneDrive/Desktop/CBDA-main/Dataset/text-data.csv')
    return dataset

def train_cyberbullying_model(dataset):
    # Prepare data
    X = dataset['text']
    y = dataset['label']
        
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer(max_features=1000)  # Limit to top 1000 features
    X_transformed = vectorizer.fit_transform(X)
    
    # Create Random Forest classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)  # Adjust parameters as needed
    
    # Train the model
    model.fit(X_transformed, y)
    
    return vectorizer, model
