## 2. Array Comparisons ##

import numpy
third_column = world_alcohol[:, 2]
countries_canada = (third_column == 'Canada')
first_column = world_alcohol[:, 0]
years_1984 = (first_column == '1984')


## 3. Selecting Elements ##

import numpy
country_is_algeria = (world_alcohol[:, 2] == 'Algeria')
country_algeria = world_alcohol[country_is_algeria, ]

## 4. Comparisons with Multiple Conditions ##

import numpy
is_algeria_and_1986 = (world_alcohol[:, 0] == "1986") & (world_alcohol[:, 2] == "Algeria")
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986, ]

## 5. Replacing Values ##

import numpy
a = (world_alcohol[:, 0] == '1986')
world_alcohol[a, 0 ] = '2014'
b = (world_alcohol[:, 3] == 'Wine')
world_alcohol[b, 3] = 'Grog'

world_alcohol[:, 0][world_alcohol[:, 0] == '1986'] = '2014'
world_alcohol[:, 3][world_alcohol[:, 3] == 'Wine'] = 'Grog'

## 6. Replacing Empty Strings ##

import numpy
is_value_empty = world_alcohol[:, 4] == ''
world_alcohol[is_value_empty, 4] = '0'

world_alcohol[:, 4][world_alcohol[:, 4] == ''] ='0'

## 7. Converting Data Types ##

import numpy
alcohol_consumption = world_alcohol[:, 4]
alcohol_consumption = alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

import numpy
alcohol_consumption = world_alcohol[:, 4]
alcohol_consumption = alcohol_consumption.astype(float)
total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

import numpy
is_canada_1986 = (world_alcohol[:, 0] == '1986') & (world_alcohol[:, 2] == 'Canada')
canada_1986 = world_alcohol[is_canada_1986, :]
canada_alcohol = canada_1986[:, 4]
is_empty = canada_alcohol == ''
canada_alcohol[is_empty] = '0'
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()


## 10. Calculating Consumption for Each Country ##

totals = {}
is_year = world_alcohol[:, 0] == '1989'
alcohol_year = world_alcohol[is_year,]

for country in countries:
    is_country = (alcohol_year[:,2] == country)
    country_alcohol = alcohol_year[is_country, :]
    alcohol_column = country_alcohol[:, 4]
    is_empty = alcohol_column == ''
    alcohol_column[is_empty] = '0'
    alcohol_column = alcohol_column.astype(float)
    country_total = alcohol_column.sum()
    totals[country] = country_total
        

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None

'''
for key,value in enumerate(totals):
    if highest_key is None or value > highest_value:
        highest_key = key
        highest_value = value
'''
'''
for country in totals:
    if totals[country] > highest_value:
        highest_value = totals[value]
        highest_key = country
'''        


highest_value = 0
highest_key = None
for country in totals:
    consumption = totals[country]
    if highest_value < consumption:
        highest_value = consumption
        highest_key = country

    