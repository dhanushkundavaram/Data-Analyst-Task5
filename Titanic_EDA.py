# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 17:34:19 2025

@author: User
"""

import pandas as pd


# Load dataset
df = pd.read_csv(r"C:\Users\User\Downloads\train.csv")

print(df.info())
print(df.describe())
print(df.head())
print("Initial shape:", df.shape)

# Check for nulls and duplicates
print("Missing values:\n", df.isnull().sum())
print("Duplicate records:", df.duplicated().sum())


print(df['Sex'].value_counts())
print(df['Pclass'].value_counts())
print(df['Embarked'].value_counts())


import seaborn as sns
import matplotlib.pyplot as plt

# Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Pairplot (optional: drop NaNs or limit columns to avoid clutter)
sns.pairplot(df[['Survived', 'Age', 'Fare', 'Pclass', 'SibSp', 'Parch']].dropna(), hue='Survived')
plt.show()



# Survival by Sex
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.show()

# Survival by Class
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Passenger Class")
plt.show()


# Age Distribution
sns.histplot(df['Age'].dropna(), kde=True, bins=30)
plt.title("Age Distribution")
plt.show()

# Fare Distribution
sns.histplot(df['Fare'], kde=True, bins=30)
plt.title("Fare Distribution")
plt.show()

# Boxplot: Age vs Survived
sns.boxplot(x='Survived', y='Age', data=df)
plt.title("Age vs Survival")
plt.show()

# Boxplot: Fare vs Survived
sns.boxplot(x='Survived', y='Fare', data=df)
plt.title("Fare vs Survival")
plt.show()

# Scatterplot: Age vs Fare
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
plt.title("Age vs Fare (Colored by Survival)")
plt.show()

