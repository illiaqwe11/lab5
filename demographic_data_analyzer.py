import pandas as pd

def race_count(df):
    """Повертає кількість людей кожної раси."""
    return df['race'].value_counts()

def average_age_men(df):
    """Повертає середній вік чоловіків."""
    men = df[df['sex'] == 'Male']
    return round(men['age'].mean(), 1)

def percentage_bachelors(df):
    """Повертає відсоток людей з вищою освітою."""
    bachelors = df[df['education'] == "Bachelors"]
    return round((len(bachelors) / len(df)) * 100, 1)

def higher_education_salary(df):
    """Повертає відсоток людей з вищою освітою, що заробляють більше 50K."""
    higher_ed = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    return round((higher_ed[higher_ed['salary'] == '>50K'].shape[0] / higher_ed.shape[0]) * 100, 1)

def lower_education_salary(df):
    """Повертає відсоток людей без вищої освіти, що заробляють більше 50K."""
    lower_ed = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    return round((lower_ed[lower_ed['salary'] == '>50K'].shape[0] / lower_ed.shape[0]) * 100, 1)

def min_work_hours(df):
    """Повертає мінімальну кількість годин роботи на тиждень."""
    return df['hours-per-week'].min()

def min_hours_salary(df):
    """Повертає відсоток людей, які працюють мінімальну кількість годин і заробляють більше 50K."""
    min_hours = df[df['hours-per-week'] == df['hours-per-week'].min()]
    return round((min_hours[min_hours['salary'] == '>50K'].shape[0] / min_hours.shape[0]) * 100, 1)

def country_max_percentage(df):
    """Повертає країну з найбільшим відсотком людей, що заробляють більше 50K, і цей відсоток."""
    countries = df['native-country'].unique()
    highest_percentage = 0
    country_name = ''
    
    for country in countries:
        country_data = df[df['native-country'] == country]
        percentage = (country_data[country_data['salary'] == '>50K'].shape[0] / country_data.shape[0]) * 100
        if percentage > highest_percentage:
            highest_percentage = percentage
            country_name = country
            
    return country_name, round(highest_percentage, 1)

def popular_occupation_in_india(df):
    """Повертає найбільш популярну професію для людей, які заробляють більше 50K в Індії."""
    india_data = df[df['native-country'] == 'India']
    india_above_50k = india_data[india_data['salary'] == '>50K']
    return india_above_50k['occupation'].mode()[0]
