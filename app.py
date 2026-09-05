import streamlit as st
import pandas as pd

# -----------------------------
# Load Data
# -----------------------------
jobs = pd.read_csv("jobs.csv")


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="JobLens",
    page_icon="🔎",
    layout="wide"
)
# Sidebar
st.sidebar.title("🔎 JobLens")
st.sidebar.write("Job Market Analytics Dashboard")

# -----------------------------
# Title
# -----------------------------
st.title("🔎 JobLens")
st.subheader("Job Market Skills & Salary Analytics")
st.write("Number of selected jobs requiring each skill:")
st.write(
    "Explore job roles, salary trends, skills, and locations "
    "using real data analysis."
)
st.write(
    "An interactive dashboard for exploring job roles, "
    "skills, salaries, and hiring locations."
)

st.divider()

# -----------------------------
# Key Metrics
# -----------------------------
total_jobs = len(jobs)
average_salary = jobs["Salary"].mean()
top_role = jobs["Job Role"].value_counts().idxmax()
highest_salary = jobs["Salary"].max()
top_skill = max(
    ["Python", "SQL", "Excel"],
    key=lambda skill: (jobs[skill] == "Yes").sum()
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("💼 Total Jobs", total_jobs)
col2.metric("💰 Average Salary", f"{average_salary:.1f} LPA")
min_salary = st.slider(
    "Minimum Salary (LPA)",
    min_value=0.0,
    max_value=float(jobs["Salary"].max()),
    value=0.0,
    step=0.5
)
col3.metric("🏆 Top Role", top_role)
col4.metric("🔥 Top Skill", top_skill)
col5.metric("📈 Highest Salary", f"{highest_salary:.1f} LPA")
st.divider()
highest_paid_role = jobs.groupby("Job Role")["Salary"].mean().idxmax()
highest_paid_salary = jobs.groupby("Job Role")["Salary"].mean().max()

st.success(
    f"🏆 Highest Average Salary: {highest_paid_role} — "
    f"{highest_paid_salary:.1f} LPA"
)

# -----------------------------
# Filters
# -----------------------------
st.header("🔎 Explore Jobs")

col1, col2 = st.columns(2)

with col1:
    selected_role = st.selectbox(
        "Select Job Role",
        ["All"] + sorted(jobs["Job Role"].unique().tolist())
    )

with col2:
    selected_location = st.selectbox(
        "Select Location",
        ["All"] + sorted(jobs["Location"].unique().tolist())
    )

filtered_jobs = jobs.copy()

if selected_role != "All":
    filtered_jobs = filtered_jobs[
        filtered_jobs["Job Role"] == selected_role
    ]
    filtered_jobs = filtered_jobs[
    filtered_jobs["Salary"] >= min_salary
]

if selected_location != "All":
    filtered_jobs = filtered_jobs[
        filtered_jobs["Location"] == selected_location
    ]

st.write(f"Showing **{len(filtered_jobs)} jobs**")
st.metric(
    "🔎 Matching Jobs",
    len(filtered_jobs)
)
st.write(
    f"Average salary for these jobs: "
    f"**{filtered_jobs['Salary'].mean():.1f} LPA**"
)

st.dataframe(filtered_jobs, use_container_width=True)
csv = filtered_jobs.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Jobs",
    data=csv,
    file_name="joblens_filtered_jobs.csv",
    mime="text/csv"
)
st.divider()

# -----------------------------
# Job Roles
# -----------------------------
st.header("📊 Job Roles")

role_counts = filtered_jobs["Job Role"].value_counts()

st.bar_chart(role_counts)
salary_by_role = (
    filtered_jobs.groupby("Job Role")["Salary"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(salary_by_role)

# -----------------------------
# Skill Demand
# -----------------------------
st.header("💻 Skill Demand")

python_count = (filtered_jobs["Python"] == "Yes").sum()
sql_count = (filtered_jobs["SQL"] == "Yes").sum()
excel_count = (filtered_jobs["Excel"] == "Yes").sum()
most_demanded_skill = max(
    ["Python", "SQL", "Excel"],
    key=lambda skill: (filtered_jobs[skill] == "Yes").sum()
)

st.info(f"🔥 Most demanded skill in the selected jobs: {most_demanded_skill}")

skill_data = pd.DataFrame({
    "Skill": ["Python", "SQL", "Excel"],
    "Jobs": [python_count, sql_count, excel_count]
})

st.bar_chart(skill_data.set_index("Skill"))

# -----------------------------
# Location Analysis
# -----------------------------
st.header("📍 Jobs by Location")

location_counts = filtered_jobs["Location"].value_counts()

st.bar_chart(location_counts)

# -----------------------------
# Salary Analysis
# -----------------------------
st.header("💰 Salary by Job Role")

st.dataframe(filtered_jobs, width="stretch")

st.bar_chart(salary_by_role)

st.divider()

st.caption("JobLens — Built with Python, Pandas & Streamlit")