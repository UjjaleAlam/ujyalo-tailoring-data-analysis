"""
Performs exploratory data analysis on the cleaned tailoring business dataset.

This script:
- Calculates total revenue
- Analyzes customer distribution
- Creates customer transaction charts
- Summarizes product quantities
- Visualizes product demand
"""

import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "cleaned_ujyalo_tailoring_house.csv"

PRODUCT_COLUMNS = [
    "coat",
    "waistcoat",
    "shirt",
    "pant",
    "other",
]


def main():
    """Load the dataset and perform exploratory data analysis."""

    # Load cleaned dataset
    df = pd.read_csv(DATA_FILE)

    analysis_df = df[
        [
            "customer_name",
            "customer_type",
            "total_npr",
            "initial_payment_npr",
            "remaining_payment_npr",
            "extra_charges_npr",
            *PRODUCT_COLUMNS,
        ]
    ].copy()

    # -------------------------
    # Revenue Analysis
    # -------------------------
    total_revenue = analysis_df["total_npr"].sum()
    print(f"Total Revenue (NPR): {total_revenue}")

    # -------------------------
    # Customer Analysis
    # -------------------------
    customer_counts = analysis_df["customer_type"].value_counts()
    print("\nCustomer Transaction Counts:")
    print(customer_counts)

    customer_ratio = analysis_df["customer_type"].value_counts(
        normalize=True
    )
    print("\nCustomer Transaction Ratio:")
    print(customer_ratio)

    customer_counts.plot(
        kind="bar",
        title="Transaction Distribution: New vs Returning Customers",
    )
    plt.xlabel("Customer Type")
    plt.ylabel("Number of Transactions")
    plt.tight_layout()
    plt.savefig(
        "customer_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()

    # -------------------------
    # Product Analysis
    # -------------------------
    missing_columns = [
        column
        for column in PRODUCT_COLUMNS
        if column not in analysis_df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing product columns: {missing_columns}"
        )

    analysis_df[PRODUCT_COLUMNS] = (
        analysis_df[PRODUCT_COLUMNS]
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0)
    )

    product_totals = analysis_df[PRODUCT_COLUMNS].sum()

    print("\nProduct Totals:")
    print(product_totals)

    product_totals.plot(
        kind="bar",
        title="Product Dominance by Quantity",
    )

    plt.xlabel("Product Type")
    plt.ylabel("Total Quantity")
    plt.tight_layout()
    plt.savefig(
        "product_dominance,png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()


if __name__ == "__main__":
    main()