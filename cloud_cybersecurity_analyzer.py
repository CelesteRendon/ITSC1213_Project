"""
Cloud & Cybersecurity Career Analyzer
Initial AI-generated project code.

Uses only Python's built-in csv module.
No Pandas, Polars, or similar data-analysis libraries.
"""

import csv


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
    salary_totals = {}
    job_counts = {}

    for job in jobs:
        category = job["Category"]
        salary = int(job["Salary_USD"])

        if category not in salary_totals:
            salary_totals[category] = 0
            job_counts[category] = 0

        salary_totals[category] += salary
        job_counts[category] += 1

    averages = {}

    for category in salary_totals:
        averages[category] = salary_totals[category] / job_counts[category]

    return averages


def average_salary_by_certification(jobs: list[dict[str, str]]) -> dict[str, float]:
    """Calculate the average salary associated with each certification."""
    salary_totals = {}
    job_counts = {}

    for job in jobs:
        certification = job["Certification"]
        salary = int(job["Salary_USD"])

        if certification not in salary_totals:
            salary_totals[certification] = 0
            job_counts[certification] = 0

        salary_totals[certification] += salary
        job_counts[certification] += 1

    averages = {}

    for certification in salary_totals:
        averages[certification] = salary_totals[certification] / job_counts[certification]

    return averages


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
