import pandas as pd

def calculate_medical_priority():

    df = pd.read_csv(r"E:\PYCHARM\PycharmProjects\Wildlife_Community_Dashboard\data\villages.csv")

    df["medical_score"] = (
        0.4 * df["distance_to_clinic_km"] +
        0.3 * df["malaria_cases"] +
        0.2 * df["population"] -
        0.1 * df["water_access"]
    )

    return df.sort_values("medical_score", ascending=False)