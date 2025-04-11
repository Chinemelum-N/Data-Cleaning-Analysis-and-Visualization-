import pandas as pd

df1 = pd.read_csv(r"C:\Users\Chinemelum\MyAruDatabases\customers.csv")

df1.info()
# this provide insights on the datatypes and requirement for the dataset

df1.describe()
#provides summary statistics of the dataset before any cleaning exercise is carried out.

df1.isnull().sum()

df1.columns[df1.isnull().any()]

df1[df1.isnull().any(axis = 1)]

df1.head()
#provides an overview of the dataset

#### From the above, there is the need to fill in missing values in email and age column, convert the datatype of the age column and use a consistent sentence casing for the location column 

## Data Cleaning Activities

### Customer_Data

#### For Missing Values

df1['email'].fillna('Unknown@example.com', inplace = True)
df1

# this replaces missing values with unknown@example.com

# For the missing age, we use the mean to interpolate 

mean_age = df1['age'].mean()
df1['age'].fillna(mean_age, inplace = True)
df1

#### For converting datatype

df1['age'].dtype

df1['age'] = df1['age'].astype(int)
df1['age'].dtype

#### For consistent sentence casing

df1['location'] = df1['location'].str.title()
df1

df1.describe()

#### This dataset is now ready for advanced analysis, it has been cleaned by inputing missing values, ensuring consistent sentence and appropriate data types. It is now to be saved and used for further analysis


#### To save the cleaned dataset:

df1.to_csv(r"C:\Users\Chinemelum\MyAruDatabases\cleaned_customerdata.csv")

## Summary of customer demographics

df1['age'].value_counts().sort_index()

df1['gender'].value_counts()

df1['location'].value_counts()

import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned customers dataset
customers = pd.read_csv('/mnt/data/cleaned_customers.csv')

# Age Distribution
age_distribution = customers['age'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
age_distribution.plot(kind='bar', color='skyblue')
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.show()

# Gender Distribution
gender_distribution = customers['gender'].value_counts()
plt.figure(figsize=(6, 6))
gender_distribution.plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Gender Distribution of Customers')
plt.show()

# Location Breakdown
location_distribution = customers['location'].value_counts().head(10)
plt.figure(figsize=(10, 5))
location_distribution.plot(kind='bar', color='mediumpurple')
plt.title('Top 10 Locations of Customers')
plt.xlabel('Location')
plt.ylabel('Number of Customers')
plt.show()

# Displaying statistics
total_customers = customers['customer_id'].nunique()
average_age = customers['age'].mean()

print(f"Total Number of Customers: {total_customers}")
print(f"Average Age of Customers: {average_age:.2f}")
print("Gender Distribution:")
print(gender_distribution)
print("Top 10 Locations:")
print(location_distribution)


### Transaction Dataset

df2 = pd.read_csv(r"C:\Users\Chinemelum\MyAruDatabases\transactions.csv")

df2.info()

df2.describe()

df2.isnull().sum()

df2[df2.isnull().any(axis =1)]

df2.head()

df2.duplicated().sum()

df2[df2.duplicated()]

### Data Cleaning

#### Drop Duplicates

df2 = df2.drop_duplicates()
df2.duplicated().sum()

#### Data Formating

#### standardizing date format

df2['transaction_date'] = pd.to_datetime(df2['transaction_date'], errors='coerce')
# the conversion to datetime resulted in some records not being recognised as datetime, thus the missing values are interpolated
df2['transaction_date'] = df2['transaction_date'].interpolate(method = 'linear')
# the above code introduces a timestamp to the column which is not needed for our analysis
df2['transaction_date'] = df2['transaction_date'].dt.date
df2

#### Missing Values

####  the price and qantity columns have missing values in them, mean and median were used to fill them up

mean_qty = df2['quantity'].mean()

df2['quantity'].fillna(mean_qty, inplace = True)

median_price = df2['price'].median()
df2['price'].fillna(median_price, inplace = True)

#### Converting Data type

#### The quantity datatype needs to be converted to an interger datatype given the dataset

df2['quantity'] = df2['quantity'].astype(int)

print(df2)

#### The transaction dataset is cleaned and ready to be saved for further data analysis.

df2.describe()

df2.to_csv(r"C:\Users\Chinemelum\MyAruDatabases\transactionsdata.csv")

