import pandas as pd
import gzip

# Step 1: Load the dataset
df = pd.read_csv("AIML_Dataset.csv")
print("Original dataset size (rows, columns):", df.shape)

# Step 2: Select important columns (you can remove any column you don't need)
columns_to_keep = ["step", "type", "amount", "oldbalanceOrg", "newbalanceOrig","oldbalanceDest", "newbalanceDest", "isFraud"]
df = df[columns_to_keep]
print("After column selection (rows, columns):", df.shape)

# Step 3: Row sampling to reduce size (adjust frac as needed)
df = df.sample(frac=0.2, random_state=42)  # 20% rows
print("After row sampling (rows, columns):", df.shape)

# Step 4: Data type optimization to reduce memory
for col in df.select_dtypes(include='float64').columns:
    df[col] = df[col].astype('float32')
for col in df.select_dtypes(include='int64').columns:
    df[col] = df[col].astype('int32')
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype('category')

# Step 5: Convert to JSON and compress with gzip
output_file = "dataset_compressed.json.gz"
with gzip.open(output_file, "wt", encoding="utf-8") as f:
    df.to_json(f, orient="records")

print(f"Compressed dataset saved as {output_file}")