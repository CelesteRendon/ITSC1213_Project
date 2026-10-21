"""
Cloud & Cybersecurity Career Analyzer
Initial AI-generated project code.

Uses only Python's built-in csv module.
No Pandas, Polars, or similar data-analysis libraries.
"""

import csv


def average_salary_by_field(
    jobs: list[dict[str, str]], field: str
) -> dict[str, float]:
    """Calculate average salaries grouped by a selected field."""
    salary_totals = {}
    job_counts = {}

    for job in jobs:
        group = job[field]
        salary = int(job["Salary_USD"])

        if group not in salary_totals:
            salary_totals[group] = 0
            job_counts[group] = 0

        salary_totals[group] += salary
        job_counts[group] += 1

    averages = {}

    for group in salary_totals:
        averages[group] = salary_totals[group] / job_counts[group]

    return averages


def load_jobs(filename: str) -> list[dict[str, str]]:
    """Read job records from a CSV file and return a list of dictionaries."""
    jobs = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            jobs.append(row)

    return jobs


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


def print_results(jobs: list[dict[str, str]]) -> None:
    """Display a summary of the career analysis."""
    category_averages = average_salary_by_category(jobs)
    certification_averages = average_salary_by_certification(jobs)
    highest_job = find_highest_paying_job(jobs)

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


def main() -> None:
    """Run the career analysis program."""
    jobs = load_jobs("cloud_cybersecurity_jobs.csv")
    print_results(jobs)


if __name__ == "__main__":
    main()
