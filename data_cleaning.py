import pandas as pd 
print("hello python is working.")
df = pd.read_csv("marketing_campaign-selected-columns.csv")
print(df.shape)
print(df.head())
print(df.columns)
print(df.isnull().sum())
df.columns = df.columns.str.lower()
print(df.columns)
df['income'] = df['income'].fillna(df['income'].median())
print(df['income'].isnull().sum())
print("Before removing duplicates:",df.shape)
df = df.drop_duplicates()
print("After removing duplicates:",df.shape)
print(df['marital_status'].unique())
df['marital_status'] = df['marital_status'].replace({
    'Alone':'single',
    'Absurd':'single',
    'Yolo':'single'
})
print(df['marital_status'].unique())

print(df['dt_customer'].dtype)

df['dt_customer'] = pd.to_datetime(df['dt_customer'], format='%d-%m-%Y')

print(df['dt_customer'].dtype)
print(df['dt_customer'].head())

df['year_birth'] = df['year_birth'].astype(int)
df['income'] = df['income'].astype(float)

df['age'] = 2024 - df['year_birth']

print(df[['year_birth', 'age']].head())
print(df.dtypes)

print("Before removing birth year outliers:", df.shape)
df = df[df['year_birth'] > 1940]
print("After removing birth year outliers:", df.shape)

print("Before removing income outliers:", df.shape)
df = df[df['income'] < 200000]
print("After removing income outliers:", df.shape)

print("Final shape:", df.shape)
print(df.isnull().sum())
print(df.dtypes)

df.to_csv("marketing_campaign_cleaned.csv", index=False)
print("Saved cleaned file as marketing_campaign_cleaned.csv")
