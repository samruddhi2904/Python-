import pandas as pd
import re

def clean_text_column(df, column_name):
    """
    Cleans a text column by:
    1. Converting text to lowercase
    2. Removing special characters
    3. Tokenizing the text
    """

    df[column_name] = df[column_name].str.lower()
    df[column_name] = df[column_name].apply(
        lambda text: re.sub(r'[^a-z0-9\s]', '', text)
    )
    df[column_name] = df[column_name].apply(lambda text: text.split())

    return df


# Sample test case
if __name__ == "__main__":
    data = {
        "text": [
            "Hello World!",
            "Data@Science is #Awesome",
            "Clean THIS text!!!"
        ]
    }

    df = pd.DataFrame(data)
    df = clean_text_column(df, "text")
    print(df)
