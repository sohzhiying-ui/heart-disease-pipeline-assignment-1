import pandas as pd

def remove_duplicates(input_file, output_file):
    df = pd.read_csv(input_file)
    df_clean = df.drop_duplicates()
    df_clean.to_csv(output_file, index=False)

if __name__ == "__main__":
    remove_duplicates("data/dataset.csv", "data/dataset_clean.csv")
