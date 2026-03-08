import pandas as pd

def calculate_school_priority():

    df = pd.read_csv("data/schools.csv")

    df["student_classroom_ratio"] = df["students"] / df["classrooms"]

    df["need_score"] = (
        df["student_classroom_ratio"] +
        (1 - df["toilets"]) +
        (1 - df["electricity"]) +
        (5 - df["condition_score"])
    )

    return df.sort_values("need_score", ascending=False)