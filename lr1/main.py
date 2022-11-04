import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv("airquality.csv")

    print("\nQuestion 1. What are the column names of the data frame?")
    print(list(df.keys()))

    print("\nQuestion 2. What are the row names of the data frame?")
    print(list(df.index))

    print("\nQuestion 3. Extract the first 6 rows of the data frame and print them to the console")
    print(df.head(6))

    print("\nQuestion 4. How many observations (i.e. rows) are in this data frame?")
    print(len(df))

    print("\nQuestion 5. Extract the last 6 rows of the data frame and print them to the console")
    print(df.tail(6))

    print("\nQuestion 6. How many missing values are in the “Ozone” column of this data frame?")
    print(len(df[df["Ozone"].isnull()]))

    print("\nQuestion 7. What is the mean of the “Ozone” column in this dataset? "
          "Exclude missing values (coded as NA) from this calculation.")
    print(df[df["Ozone"].notnull()]["Ozone"].mean())

    print("\nQuestion 8. Extract the subset of rows of the data frame where"
          " Ozone values are above 31 and Temp values are above 90.")
    print(df[(df["Ozone"] > 31) & (df["Temp"] > 90)])

    print("\nQuestion 9. Use a for loop to create a vector of length 6 containing"
          " the mean of each column in the data frame (excluding all missing values).")
    print([df[df[key].notnull()][key].mean() for key in df.keys()])
    
    print("\nQuestion 10. Use the apply function to calculate the standard deviation of each column in the data frame "
          "(excluding all missing values).")
    print([df[df[key].notnull()][key].std() for key in df.keys()])

    print("\nQuestion 11. Calculate the mean of “Ozone” for each Month in the data frame and "
          "create a vector containing the monthly means (exclude all missing values).")
    print([df[(df["Ozone"].notnull()) & (df["Month"] == month)]["Ozone"].mean() for month in range(1, 13)])

    print("\nQuestion 12. Draw a random sample of 5 rows from the data frame")
    print(df.sample(5))
