import pandas as pd

def handle_missing_income(df):
    """
    Handles missing values in the 'income' column.
    - Uses median if data is normally distributed (|skew| <= 0.5)
    - Uses mode if data is skewed (|skew| > 0.5)
    """

    skewness = df["income"].skew()

    if abs(skewness) <= 0.5:
        fill_value = df["income"].median()
        method = "median"
    else:
        fill_value = df["income"].mode()[0]
        method = "mode"

    df["income"] = df["income"].fillna(fill_value)

    print(f"Missing values filled using {method} (skewness = {skewness:.3f})")
    return df


# Sample test case
if __name__ == "__main__":
    data = {
        "income": [45000, 52000, None, 48000, None, 1000000]
    }

    df = pd.DataFrame(data)
    df = handle_missing_income(df)
    print(df)
