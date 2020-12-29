from csv import DictReader
import pandas as pd
import numpy as np

employee_info = []
with open("LinuxAcademy/employees.csv", newline="") as f:
    reader = DictReader(f)
    for row in reader:
        row["age"] = int(row["age"])
        row["salary"] = float(row["salary"])
        employee_info.append(row)

# Example dictionary in employee_info
# {
#     "id": "10",
#     "first_name": "Marie-ann",
#     "last_name": "Cargo",
#     "email": "Marie-ann.Cargo@example.com",
#     "gender": "Female",
#     "age": 68,
#     "salary": 54000.0,
#     "job_title": "Human Resources Manager",
# }


employees = pd.DataFrame.from_records(employee_info)
# employees_arch == employees     # save copy

print('Nber of unique job titles: ', employees.job_title.value_counts().count())

job_title_unique_gender_count = employees.groupby('job_title')['gender'].nunique()
job_title_with_2_genders = job_title_unique_gender_count.where(job_title_unique_gender_count==2).dropna().index
job_title_gender_frame = employees[employees.job_title.isin(job_title_with_2_genders)]

average_mf = pd.pivot_table(job_title_gender_frame, values=['salary'], index=['job_title'], columns=['gender'])
average_mf[('salary', 'difference')] = average_mf[('salary', 'Female')] - average_mf[('salary', 'Male')]
print(average_mf)