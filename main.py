import pandas as pd
import matplotlib.pyplot as plt
import os

jobs = pd.read_csv("jobs.csv")

roles = jobs["Job Role"].value_counts()

roles.plot(kind="bar")

plt.title("Job Roles in JobLens")
plt.xlabel("Job Role")
plt.ylabel("Number of Jobs")

os.makedirs("charts", exist_ok=True)

plt.savefig("charts/job_roles.png")




python_demand = jobs["Python"].value_counts()

python_demand.plot(kind="bar")

plt.title("Python Demand in JobLens")
plt.xlabel("Python Required")
plt.ylabel("Number of Jobs")

plt.savefig("charts/python_demand.png")

sql_demand = jobs["SQL"].value_counts()

sql_demand.plot(kind="bar")

plt.title("SQL Demand in JobLens")
plt.xlabel("SQL Required")
plt.ylabel("Number of Jobs")

plt.savefig("charts/sql_demand.png")
excel_demand = jobs["Excel"].value_counts()

excel_demand.plot(kind="bar")

plt.title("Excel Demand in JobLens")
plt.xlabel("Excel Required")
plt.ylabel("Number of Jobs")

plt.savefig("charts/excel_demand.png")
locations = jobs["Location"].value_counts()

locations.plot(kind="bar")

plt.title("Jobs by Location")
plt.xlabel("Location")
plt.ylabel("Number of Jobs")

plt.savefig("charts/jobs_by_location.png")
