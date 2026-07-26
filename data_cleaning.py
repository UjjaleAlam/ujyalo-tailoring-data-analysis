"""
Cleans the tailoring business dataset by standardizing column names,
checking for missing values, validating payment totals,
and exporting a cleaned CSV file.
"""

import pandas as pd

INPUT_FILE = "Ujyalo Tailoring House.csv"
OUTPUT_FILE = "cleaned_ujyalo_tailoring_house.csv"


def main():
    """Load, clean, validate, and export the dataset."""

    # Load dataset
    data_cleaning_df = pd.read_csv(INPUT_FILE)

    # Standardize column names
    data_cleaning_df.columns = (
        data_cleaning_df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace(".", "", regex=False)
    )

    # Rename important columns
    data_cleaning_df = data_cleaning_df.rename(
        columns={
            "total_(npr)": "total_npr",
            "initial_payment_(npr)": "initial_payment_npr",
            "remaining_payment_(npr)": "remaining_payment_npr",
            "extra_charges_(npr)": "extra_charges_npr",
        }
    )

    # Check for missing values
    missing_values = data_cleaning_df.isnull().sum()

    print("Missing values per column:")
    print(missing_values)

    # Validate payment totals
    data_cleaning_df["calculated_total"] = (
        data_cleaning_df["initial_payment_npr"]
        + data_cleaning_df["remaining_payment_npr"]
    )

    payment_mismatch = data_cleaning_df[
        data_cleaning_df["calculated_total"]
        != data_cleaning_df["total_npr"]
    ]

    print(f"\nPayment mismatches found: {len(payment_mismatch)}")

    # Export cleaned dataset
    data_cleaning_df.to_csv(OUTPUT_FILE, index=False)

    print(f"\nCleaned dataset saved as '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()