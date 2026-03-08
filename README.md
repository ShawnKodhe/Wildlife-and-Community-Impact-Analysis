# Wildlife & Community Impact Analytics Dashboard

## Overview

The **Wildlife & Community Impact Analytics Dashboard** is a data-driven tool designed to help conservation organizations prioritize community development and wildlife protection initiatives.

The dashboard analyzes community and conservation data to answer four important operational questions:

* Which villages need **medical camps next**
* Which areas have **high human–elephant conflict risk**
* Which schools most need **infrastructure support**
* Which conservation areas require **additional protection funding**

The platform provides **priority rankings and interactive maps** to help organizations allocate resources effectively.

This type of analytics system can support conservation initiatives operating near protected ecosystems such as **Maasai Mara National Reserve** and **Amboseli National Park**, where community welfare and wildlife conservation intersect.

---

# Features

The dashboard includes four analytical modules:

### Medical Camp Planning

Ranks villages based on healthcare needs using factors such as:

* distance to clinics
* disease incidence
* population size
* water access

---

### Human–Elephant Conflict Risk Analysis

Identifies areas with high conflict risk using:

* number of elephant incidents
* crop damage reports
* proximity to wildlife areas

---

### School Infrastructure Prioritization

Highlights schools needing infrastructure investment based on:

* student-to-classroom ratios
* electricity availability
* sanitation facilities
* building condition

---

### Conservation Funding Priorities

Identifies conservation areas requiring additional protection by analyzing:

* poaching incidents
* ranger shortages
* wildlife population
* tourism revenue

---

# Technology Stack

This project is built using:

* **Python**
* **Streamlit** – interactive dashboard
* **Pandas** – data processing
* **NumPy** – numerical analysis
* **Plotly** – interactive maps and visualizations

---

# Project Structure

```
wildlife_community_dashboard/

data/
    villages.csv
    elephant_conflicts.csv
    schools.csv
    conservation_areas.csv

src/
    medical_priority.py
    conflict_risk.py
    school_priority.py
    conservation_priority.py

dashboard/
    app.py

requirements.txt
README.md
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/wildlife-community-dashboard.git
cd wildlife-community-dashboard
```

---

## 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## 3. Run the Dashboard

Start the Streamlit application:

```bash
streamlit run dashboard/app.py
```

Once the app starts, the dashboard will open in your browser.

---

# Usage

After launching the dashboard, users can navigate through the tabs to explore different analyses:

* **Medical Camps** – identify villages needing healthcare outreach
* **Elephant Conflict** – view areas with high human–wildlife conflict risk
* **School Infrastructure** – identify schools requiring upgrades
* **Conservation Funding** – prioritize conservation zones needing support

Interactive maps allow users to visually explore priority locations.

---

# Future Improvements

Potential enhancements for this project include:

* machine learning models for conflict prediction
* satellite data integration for environmental monitoring
* wildlife migration analysis
* mobile data collection for field teams
* GIS integration with protected area boundaries

---

# License

This project is released under the **MIT License**.

---

