def transform_data(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing age
    df = df.dropna(subset=["age"])

    # Keep valid ages
    df = df[df["age"] >= 0]

    return df