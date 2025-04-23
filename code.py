# Air Pollution and Innovation Opportunity Report
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("/Users/shikharagrawal/Desktop/pyton/pollution.csv")

#Displaying some data 
print(df.head())
print(df.info())            #Give Dataset information
print(df.describe())        #Give Statistics Summary of numerical columns

# Step 1: Clean column names (remove extra spaces)
df.columns = df.columns.str.strip()

# Step 2: Handle missing values
print("\nMissing Values: \n", df.isnull().sum())                #Summing missing values columns wise
print("\nMissing Values: \n", df.isnull().sum().sum())          #Summing all the columns missing values 

# Filling missing value with mean
for col in ['pollutant_min', 'pollutant_max', 'pollutant_avg']:
    df[col] = df[col].fillna(df[col].mean())

#again checking for null values
print(df.isnull().sum())

# 3. Check for duplicates rows and remove them
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

# 4. Convert 'last_update' to datetime
df['last_update'] = pd.to_datetime(df['last_update'], dayfirst=True, errors='coerce')

#Handle missing datetimes
print(df['last_update'].isnull().sum())

#Step 6: check for misspelled data/Fix categorical data noise
columns_to_check = ['country', 'state', 'city', 'station', 'pollutant_id']

for col in columns_to_check:
    print(f"\n Unique values in '{col}' (total: {df[col].nunique()}):")
    print(df[col].value_counts().sort_values(ascending=True))

#Misllaneous cleaning of dataset
print(df['city'].str.lower().value_counts().head(20))
df['pollutant_id'] = df['pollutant_id'].str.upper()

# Standardize state names for consistency
df['state'] = df['state'].str.replace('_', ' ', regex=False)
#data cleaning completed 

#Data Visualization
# Objective 1. Sorted Graph showing Pollutant Type Frequency 
pollutant_counts = df['pollutant_id'].value_counts().sort_values(ascending=False)
sns.barplot(x=pollutant_counts.index,y=pollutant_counts.values, palette='viridis')

for i, count in enumerate(pollutant_counts.values):
    plt.text(i, count + 1, str(count), ha='center', va='bottom', fontsize=10)
plt.title("Pollutant Type Frequency (Sorted)", fontsize=14)
plt.xlabel("Pollutant ID")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Objective 2.Top 10 cities with the highest average pollutant levels
plt.style.use('dark_background')
top_cities = df.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_cities.values, y=top_cities.index, palette="magma")
plt.title("Top 10 Polluted Cities (Avg)", fontsize=16, color='white')
plt.xlabel("Average Pollution Level",color='white')
plt.ylabel("City",color='white')
plt.grid(False)
plt.show()

# Objective 3. Distribution of Average Pollution Levels Across Indian States
plt.style.use('dark_background')
plt.figure(figsize=(14, 6))
flierprops = dict(marker='o', markerfacecolor='white', markersize=5, linestyle='none')
sns.boxplot(data=df, x='state', y='pollutant_avg', palette="flare", flierprops=flierprops)
plt.xticks(rotation=90, color='white')
plt.yticks(color='white')
plt.title("Pollution Levels Across States", fontsize=16, color='white')
plt.grid(False)
plt.tight_layout()
plt.show()

# Objective 4. Correlation Between Pollution Values
plt.figure(figsize=(6,4))
sns.heatmap(df[['pollutant_min', 'pollutant_max', 'pollutant_avg']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Between Pollution Values")
plt.show()

# Objective 5. Box Plot - Distribution of pollutant_avg by pollutant type
sns.set_style("dark")
top_cities = df['city'].value_counts().nlargest(5).index
df_top_cities = df[df['city'].isin(top_cities)]
top_pollutants = df['pollutant_id'].value_counts().nlargest(5).index
df_top_pollutants = df[df['pollutant_id'].isin(top_pollutants)]
sns.boxplot(data=df_top_pollutants, x='pollutant_id', y='pollutant_avg')
plt.title('Outlier Detection by Pollutant Type')
plt.tight_layout()
plt.show()

# Objective 6. Geographical Scatter Plot
sns.set_style("dark")
sns.scatterplot(data=df, x='longitude', y='latitude', hue='pollutant_avg', palette='magma', 
                size='pollutant_avg', sizes=(50, 300),alpha=0.5,edgecolor=None)
plt.title('Pollution Levels by Location')
plt.tight_layout()
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# Objective 7. Grouped Bar Chart - Pollutant comparison in top cities
grouped = df_top_cities.groupby(['city', 'pollutant_id'])['pollutant_avg'].mean().reset_index()
sns.barplot(data=grouped, x='city', y='pollutant_avg', hue='pollutant_id')
plt.title('Pollutant Comparison Across Top Cities')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Objective 8. Histogram - Distribution of pollutant_avg
sns.histplot(data=df, x='pollutant_avg', bins=30, kde=True, color='skyblue')
plt.style.use('dark_background')
plt.title('Distribution of Average Pollutant Levels')
plt.tight_layout()
plt.show()

# Objective 9. Scatter Plot Matrix
sns.set_style("dark")
df_plot = df[['pollutant_min', 'pollutant_max', 'pollutant_avg']].dropna().copy()
df_plot['category'] = pd.cut(df_plot['pollutant_avg'], bins=3, labels=["Low", "Medium", "High"])
sns.pairplot( df_plot, hue='category',palette='coolwarm',diag_kind='kde')
plt.suptitle('Scatter Plot Matrix for Pollutant Measures', y=1.02)
plt.tight_layout()
plt.show()

#Model Training
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

#Normalization
scaler = MinMaxScaler()
df[['pollutant_max', 'pollutant_avg']] = scaler.fit_transform(df[['pollutant_max', 'pollutant_avg']])

print("After Normalization:")
print(df[['pollutant_max', 'pollutant_avg']].describe())

# Scatter Plot: pollutant_max vs pollutant_avg
plt.scatter(df['pollutant_max'], df['pollutant_avg'])
plt.xlabel('Pollutant Max (Normalized)')
plt.ylabel('Pollutant Avg (Normalized)')
plt.title('Scatterplot: Max vs Avg Pollution Level')
plt.grid(True)
plt.show()

# Linear Regression Model
X = df[['pollutant_max']]
y = df[['pollutant_avg']]
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, Y_train)

# Prediction for a custom max pollution input
check_pollution = pd.DataFrame({'pollutant_max': [0.8]})  # normalized value
predicted_avg = model.predict(check_pollution)
print("Predicted pollutant_avg for normalized pollutant_max = 0.8:", predicted_avg)

# Plot regression line
plt.scatter(X, y, color='skyblue')
plt.plot(X, model.predict(X), color='red', linewidth=3)
plt.xlabel('Pollutant Max')
plt.ylabel('Pollutant Avg')
plt.title('Linear Regression Fit')
plt.show()

# Mean Squared Error
y_pred = model.predict(X_test)
mse = mean_squared_error(Y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse:.6f}")
print(f"R² Score: {r2_score(Y_test, y_pred):.4f}")
