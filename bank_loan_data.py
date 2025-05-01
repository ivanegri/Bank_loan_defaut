import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
np.random.seed(42)

# Generate synthetic data
data = {
    "applicant_id": [f"A{1000 + i}" for i in range(10000)],
    "age": np.random.randint(18, 70, 10000),
    "mothly_income": np.round(np.random.uniform(1500, 20000, 10000), 2),
    'investment_income': np.round(np.random.uniform(0, 5000, 10000), 2),
    'savings_account_balance': np.round(np.random.uniform(0, 100000, 10000), 2),
    'checking_account_balance': np.round(np.random.uniform(0, 50000, 10000), 2),
    'credit_card_balance': np.round(np.random.uniform(0, 20000, 10000), 2),
    'other_loans_balance': np.round(np.random.uniform(0, 50000, 10000), 2),
    "loan_amount_requested": np.round(np.random.uniform(1000, 100000, 10000), 2),
    "installment": np.round(np.random.uniform(100, 5000, 10000), 2),
    "loan_date": pd.date_range(start="2020-01-01", periods=10000, freq='D'),
    "loan_purpose": np.random.choice(["Home", "Car", "Education", "Personal"], 10000), 
    "state": np.random.choice(["CA", "TX", "NY", "FL", "IL"], 10000),
    "city": [fake.city() for _ in range(10000)],
    "credit_score": np.random.randint(300, 1000, 10000),
    "loan_amount": np.round(np.random.uniform(5000, 500000, 10000), 2),
    "interest_rate": np.round(np.random.uniform(0.03, 0.2, 10000), 4),
    "loan_term": np.random.choice([12, 24, 36, 48 , 60], 10000),
    "employment_status": np.random.choice(["Employed", "Self-Employed", "Unemployed"], 10000, p=[0.7, 0.2, 0.1]),
    "employment_duration": np.random.randint(0, 20, 10000),  # in years
    "marital_status": np.random.choice(["Single", "Married", "Divorced"], 10000, p=[0.4, 0.5, 0.1]),
    "dependents": np.random.randint(0, 5, 10000),
    "education_level": np.random.choice(["High School", "Bachelors", "Masters", "PhD"], 10000, p=[0.3, 0.4, 0.2, 0.1]),
    "residential_status": np.random.choice(["Owned", "Rented", "Mortgaged"], 10000, p=[0.5, 0.4, 0.1]),
    "years_at_residence": np.random.randint(0, 30, 10000),
    "bank_account_age": np.random.randint(0, 20, 10000),  # in years
    "previous_defaults": np.random.randint(0, 3, 10000),
    "default": np.random.choice([0, 1], 10000, p=[0.85, 0.15])  # Target (1 = default)
}

df = pd.DataFrame(data)

# Add missing values (5% random)
df.loc[df.sample(frac=0.01).index, "credit_score"] = np.nan

# Save to CSV
df.to_csv("loan_data.csv", index=False)