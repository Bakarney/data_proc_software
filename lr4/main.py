import pandas as pd
import numpy as np
import os
import re
from tqdm import tqdm


if __name__ == '__main__':
    pd.options.mode.chained_assignment = None

    data = {}
    for set_name in ["test", "train"]:
        data[set_name] = {}
        for root, dirs, files in os.walk(f'./UCI HAR Dataset/{set_name}'):
            for file in files:
                text = open(os.path.join(root, file), "r").read()
                text = re.sub(r" +", " ", text)
                text = re.sub(r"\s*\n\s*", "\n", text)
                text = re.sub(r"(^\s+|\s+$)", "", text)

                column_name = file.replace(f"_{set_name}.txt", "")
                data[set_name][column_name] = text.split("\n")
                data[set_name][column_name] = [q.split(" ") for q in data[set_name][column_name]]
                data[set_name][column_name] = np.transpose(data[set_name][column_name])
                data[set_name][column_name] = {column_name + "_" + str(i): v
                                               for i, v in enumerate(data[set_name][column_name])}

    test_df = [pd.DataFrame(i) for i in data["test"].values()]
    train_df = [pd.DataFrame(i) for i in data["train"].values()]

    for set_name in range(1, len(test_df)):
        test_df[0] = test_df[0].join(test_df[set_name])
    test_df = test_df[0]

    for set_name in range(1, len(train_df)):
        train_df[0] = train_df[0].join(train_df[set_name])
    train_df = train_df[0]

    for i in test_df:
        test_df[i] = pd.to_numeric(test_df[i])
    for i in train_df:
        train_df[i] = pd.to_numeric(train_df[i])

    print("\n\nTest dataset:")
    print(test_df)
    print("\n\nTrain dataset:")
    print(train_df)

    print("\n\n1. Merges the training and the test sets to create one data set.")
    df = pd.concat([test_df, train_df], ignore_index=True)
    print(df)

    print("\n\n2. Extracts only the measurements on the mean and standard deviation for each measurement.")
    for i in df.keys():
        print(i, ":", sep="")
        print("Mean: ", df[i].mean())
        print("Standard deviation:", df[i].std())
        print()

    print("\n\n3. Uses descriptive activity names to name the activities in the data set")
    labels = open("./UCI HAR Dataset/activity_labels.txt").read()
    labels = re.sub(r"(^\s+|\s+$)", "", labels)
    labels = [i.split(" ") for i in labels.split("\n")]
    labels = {int(i[0]): i[1] for i in labels}
    for i in range(len(df["y_0"])):
        df["y_0"][i] = labels[df["y_0"][i]]
    print(df["y_0"])

    print("\n\n4. Appropriately labels the data set with descriptive variable names")
    df = df.rename(columns={"y_0": "activity", "subject_0": "subject"})
    print(df.keys())

    print("\n\n5. From the data set in step 4, creates a second, independent tidy data set with the average "
          "of each variable for each activity and each subject.")
    unique_df = df[["activity", "subject"]].drop_duplicates()
    unique_df.index = range(len(unique_df))
    mean_df = pd.DataFrame(columns=df.keys())
    mean_df = pd.concat([mean_df, unique_df])
    for i in tqdm(mean_df.index):
        for j in [k for k in mean_df.keys() if k != "activity" and k != "subject"]:
            tmp = df[(df["activity"] == mean_df["activity"][i]) & (df["subject"] == mean_df["subject"][i])][j]
            mean_df[j][i] = tmp.mean()
    print(mean_df)
