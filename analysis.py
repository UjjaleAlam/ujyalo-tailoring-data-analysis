import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("cleaned_ujyalo_tailoring_house.csv")

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(".", "")

)
#print(df.columns.tolist())

analysis_df = df[
  [  
    "customer_name",
    "customer_type",
    "total_npr",
    "initial_payment_npr",
    "remaining_payment_npr",
    "extra_charges_npr",
    "coat",
    "wasscoat",
    "shirt",
    "pant",
    "other"
  ]
]

total_revenue = analysis_df["total_npr"].sum()
print("Total Revenue (NPR):", total_revenue)

customer_counts = analysis_df["customer_type"].value_counts()
print(customer_counts)

customer_ratio = analysis_df["customer_type"].value_counts(normalize=True)
print(customer_ratio)

customer_counts.plot(
    kind="bar",
    title="Transaction Distribution: New vs Returning Customers"
    )
plt.ylabel("Number of Transcations")
plt.xlabel("Customer Type")
plt.tight_layout()
plt.show()

product_columns = ["coat", "wasscoat", "shirt", "pant", "other"]

analysis_df[product_columns] = analysis_df[product_columns].apply(pd.to_numeric, errors="coerce").fillna(0)

product_totals = analysis_df[product_columns].sum()

analysis_df[product_columns] = analysis_df[product_columns].apply(pd.to_numeric, errors="coerce").fillna(0)

product_totals.plot(
    kind="bar",
    title="Product Dominance by Quantity"
)
plt.xlabel("Product Type")
plt.ylabel("Total Quantity")
plt.tight_layout()
plt.show()