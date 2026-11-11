"""
Cloud & Cybersecurity Career Analyzer
Phase 4: Pandas Data Analysis and Visualization
"""


import csv
import json
import pandas as pd
import matplotlib.pyplot as plt

from career_analysis import average_salary_by_field, sort_jobs_by_salary


def average_salary_by_field(
    jobs: list[dict[str, str]], field: str
) -> dict[str, float]:
    """Calculate average salaries grouped by a selected field."""
    salary_data = {}

    for job in jobs:
        group = job[field]
        salary = int(job["Salary_USD"])

        if group not in salary_data:
            salary_data[group] = {"total": 0, "count": 0}

        salary_data[group]["total"] += salary
        salary_data[group]["count"] += 1

    averages = {}

    for group in salary_data:
        total = salary_data[group]["total"]
        count = salary_data[group]["count"]
        averages[group] = total / count

    return averages



def load_jobs(filename: str) -> list[dict[str, str]]:
    """Read job records from a CSV file and return a list of dictionaries."""
    jobs = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            jobs.append(row)

    return jobs


def load_jobs_dataframe(filename: str) -> pd.DataFrame:
    """Load job data from a CSV file into a pandas DataFrame."""
    df = pd.read_csv(filename)
    return df

def average_salary_by_category(jobs: list[dict[str, str]]) -> dict[str, float]:
    """Calculate the average salary for each job category."""
    return average_salary_by_field(jobs, "Category")


def average_salary_by_certification(jobs: list[dict[str, str]]) -> dict[str, float]:
    """Calculate the average salary associated with each certification."""
    return average_salary_by_field(jobs, "Certification")


def find_highest_paying_job(jobs: list[dict[str, str]]) -> dict[str, str]:
    """Return the job record with the highest salary."""
    if len(jobs) == 0:
        return {}

    highest_job = jobs[0]

    for job in jobs:
        if int(job["Salary_USD"]) > int(highest_job["Salary_USD"]):
            highest_job = job

    return highest_job


def analyze_jobs(jobs: list[dict[str, str]]) -> dict:
    """
    Analyze cloud and cybersecurity job records.

    Args:
        jobs: A list of dictionaries containing job information.

    Returns:
        A dictionary containing category salary averages,
        certification salary averages, and the highest-paying job.
    """
    return {
        "category_averages": average_salary_by_category(jobs),
        "certification_averages": average_salary_by_certification(jobs),
        "highest_job": find_highest_paying_job(jobs)
    }




def print_results(results: dict, jobs: list[dict[str, str]]) -> None:

    """Display the career analysis results."""
    category_averages = results["category_averages"]
    certification_averages = results["certification_averages"]
    highest_job = results["highest_job"]

    print("CLOUD & CYBERSECURITY CAREER ANALYSIS")
    print("-------------------------------------")

    print("\nAverage salary by category:")
    for category in category_averages:
        print(f"{category}: ${category_averages[category]:,.2f}")

    print("\nAverage salary by certification:")
    for certification in certification_averages:
        print(f"{certification}: ${certification_averages[certification]:,.2f}")

    if highest_job:
        print("\nHighest-paying role:")
        print(f"{highest_job['Job_Title']}: ${int(highest_job['Salary_USD']):,}")
        print(f"Certification: {highest_job['Certification']}")
        print(f"Cloud platform: {highest_job['Cloud_Platform']}")

   
    print("\nTop 5 Highest-Paying Jobs:")

    sorted_jobs = sort_jobs_by_salary(jobs)

    for job in sorted_jobs[:5]:
    
        print(f"{job['Job_Title']}: ${int(job['Salary_USD']):,}") 
def save_results(results: dict) -> None:
    """Save the career analysis results to a JSON file."""
    with open("results.json", "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

def plot_salary_by_category(df: pd.DataFrame) -> None:
    """Create a bar chart of average salaries by job category."""

    average_salaries = df.groupby("Category")["Salary_USD"].mean()

    average_salaries.plot(kind="bar")

    plt.title("Average Salary by Career Category")
    plt.xlabel("Career Category")
    plt.ylabel("Average Salary (USD)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("average_salary_by_category.png")
    plt.show()        

def main() -> None:
    """Run the career analysis program."""
    jobs = load_jobs("cloud_cybersecurity_jobs.csv")

    df = load_jobs_dataframe("cloud_cybersecurity_jobs.csv")
    print("\nPANDAS DATAFRAME PREVIEW")
    print(df.head())

    results = analyze_jobs(jobs)
    print_results(results, jobs)
    save_results(results)
    plot_salary_by_category(df)


if __name__ == "__main__":
    main()
