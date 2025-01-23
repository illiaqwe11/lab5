import pandas as pd
from demographic_data_analyzer import *

df = pd.read_csv('data.csv')

print("Кількість людей по расі:\n", race_count(df))
print("Середній вік чоловіків:", average_age_men(df))
print("Відсоток людей з вищою освітою (Bachelor's):", percentage_bachelors(df))
print("Відсоток людей з вищою освітою, що заробляють більше 50K:", higher_education_salary(df))
print("Відсоток людей без вищої освіти, що заробляють більше 50K:", lower_education_salary(df))
print("Мінімальні години роботи на тиждень:", min_work_hours(df))
print("Відсоток людей, які працюють мінімальні години і заробляють більше 50K:", min_hours_salary(df))
print("Країна з найбільшим відсотком людей, що заробляють більше 50K:", country_max_percentage(df))
print("Найбільш популярна професія для тих, хто заробляє більше 50K в Індії:", popular_occupation_in_india(df))
