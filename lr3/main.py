import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv("hike_long.csv")

    # Tidying dataset
    print("1. Convert columns gain, highpoint, rating to numeric values.")
    print("Done by default!")

    print("\n2. Add new column trip with the type of trip from column length (“roundtrip”, “trails”, “one-way”).")
    df["trip"] = df["length"].str.split(" ").str[-1]
    print(df[["length", "trip"]])

    print("\n3. Add new column length_total with the route length from column length, considering that for “one-way” "
          "trip you must double the route length.")
    df["length_total"] = pd.to_numeric(df["length"].str.split(" ").str[0])
    df["length_total"] = df.apply(lambda df: df["length_total"] * 2 if df["trip"] == "one-way" else df["length_total"],
                                  axis=1)
    print(df[["length", "length_total"]])

    print("\n4. Add new column location_general with location from column location (a part before “–”).")
    df["location_general"] = df["location"].str.split(" -- ").str[0]
    print(df[["location", "location_general"]])

    print("\n5. Add column id with row number")
    df["index"] = df.index
    print(df["index"])

    # Questioning dataset
    print("\nQuestion 1. How many routes have rating more than 4.9")
    print(len(df[df["rating"] > 4.9]))

    print("\nQuestion 2. How many routes are “Good for kids”?")
    print(len(df[df["features"].str.contains("Good for kids")]))

    print("\nQuestion 3. Which unique features can routes have?")
    print(df.drop_duplicates("features")["features"].tolist())

    print("\nQuestion 4. What is the most common rating of a route?")
    print(df["rating"].value_counts().head(5))

    print("\nQuestion 5. How many observations (i.e. rows) are in this data frame?")
    print(len(df))
