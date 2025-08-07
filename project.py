import pandas as pd

file_path=r"data_project.csv"
df=pd.read_csv(file_path,low_memory=False)

print(df.head())
print(df.info())
print(df.isnull().sum())

print(df['InvoiceDate'].unique()[:10])

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce', format='%d-%m-%Y %I.%M.%S %p')
print(df['InvoiceDate'].isnull().sum())

print("Before removing duplicates:", df.shape)
df = df.drop_duplicates()
print("After removing duplicates:", df.shape)

df_cleaned = df.dropna()


output_path = r"C:\Users\abhip\OneDrive\Desktop\Project1\cleaned_data_project.csv"
df_cleaned.to_csv(output_path, index=False)

print("Cleaned data saved to:", output_path)
