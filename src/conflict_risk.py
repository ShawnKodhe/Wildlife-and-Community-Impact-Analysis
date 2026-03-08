import pandas as pd

def calculate_conflict_risk():

    df = pd.read_csv(r"E:\PYCHARM\PycharmProjects\Wildlife_Community_Dashboard\data\elephant_conflicts.csv")

    df["risk_score"] = (
        0.5 * df["elephant_incidents"] +
        0.3 * df["crop_damage_usd"] +
        0.2 * (1 / df["distance_to_park"])
    )

    return df.sort_values("risk_score", ascending=False)