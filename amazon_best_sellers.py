import pandas as pd

df = pd.read_csv('bestsellers.csv')

# EXPLORE: get the shape of the spreadsheet
print(df.shape)

# EXPLORE: get the column names
print(df.columns)

# EXPLORE: print the first 5 rows
print(df.head)

# EXPLORE: get summary statistics
print(df.describe())

# CLEAN: eliminate duplicates
df.drop_duplicates(inplace=True)

# CLEAN: rename some of the columns
df.rename(columns={'Name': 'Title', 'User Rating': 'Rating'}, inplace=True)

# CLEAN: convert prices to float data types
df['Price'] = df['Price'].astype(float)


