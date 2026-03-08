import pandas as pd

def calculate_conservation_priority():

    df = pd.read_csv(r"E:\PYCHARM\PycharmProjects\Wildlife_Community_Dashboard\data\conservation_areas.csv")

    df["ranger_gap"] = df["area_size_km2"] / df["ranger_count"]

    df["priority_score"] = (
        0.4 * df["poaching_incidents"] +
        0.3 * df["ranger_gap"] +
        0.2 * df["wildlife_population"] -
        0.1 * df["tourism_revenue"]
    )

    return df.sort_values("priority_score", ascending=False)