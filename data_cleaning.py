import pandas as pd

data_cleaning_df = pd.read_csv("Ujyalo Tailoring House.csv")

data_cleaning_df.columns = (
    data_cleaning_df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(".", "")

)
#print(data_cleaning_df.columns.tolist())


data_cleaning_df = data_cleaning_df.rename(columns={"total_(npr)": "total_npr", "initial_payment_(npr)": "initial_payment_npr", "remaining_payment_(npr)": "remaining_payment_npr", "extra_charges_(npr)": "extra_charges_npr"})

missing_values = data_cleaning_df.isnull().sum()
print("Missing values per column:")
print(missing_values)

data_cleaning_df["calculated_total"] = data_cleaning_df["initial_payment_npr"] + data_cleaning_df["remaining_payment_npr"]
payment_mismatch = data_cleaning_df[data_cleaning_df["calculated_total"] != data_cleaning_df["total_npr"]]

data_cleaning_df.to_csv("cleaned_ujyalo_tailoring_house.csv", index=False)