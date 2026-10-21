
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