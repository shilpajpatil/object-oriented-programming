
import pandas as pd 

df = pd.read_csv('infodata.csv')  # Replace with your file path
#print(df.head())  # Display the first 5 rows

#Retrive all thecars built in year 72:
#print(df.loc[df['model_year'] == 72 ].head())

#Problem statement : Retrieve details of all the cars built in Japan having 6 cylinders
#print(df.loc[(df['origin'] == 'japan') & (df['cylinders'] == 6)])


""" Fuel efficient
 MPG > 29, Horsepower < 93.5,
Weight < 2500"""
#print(df.loc[(df['mpg'] > 29) & (df['horsepower'] < 93.5) & (df['weight'] < 2500)])



"""Muscle cars
Displacement >262, Horsepower > 126, Weight in range[2800, 3600]"""
#print(df.loc[(df['displacement'] > 262) & (df['horsepower'] > 126) & (df['weight'] >=2800) & (df['weight'] <= 3600)])


"""SUV
# Horsepower > 140 , Weight > 4500"""
print(df.loc[(df['horsepower'] > 140) & (df['weight'] >=4500)])


"""Racecar
 Weight <2223, acceleration > 17"""
#print(df.loc[(df['acceleration'] > 17) & (df['weight'] < 2223)])


#Problem Statement:
#XYZ Custom cars want the data sorted according to the number of cylinders. 
#print(df.sort_values(by = 'cylinders'))

"""There is a requirement in which the cars that have lowest acceleration must be assessed. It is also to be checked 
that which cars have higher horsepower despite having lower acceleration.
"""
#print(df.sort_values(['acceleration', 'horsepower'], ascending = (1,0)))

#How many cars belong to each year?
#print(df.groupby(['model_year']).count()[['name']])


"""ps:Some senior engineers in XYZ custom cars
want to understand about the effect of model year and number 
of cylinders on horsepower.

soln : checking the mean, minimum and maximum horsepower based on number of cylinders and model year. For such requirement, 
the ‘agg’ function can be combined with groupby function as shown

"""
"""
#Creating a DataFrame grouped on cylinders and model_year and finding mean, min and max of horsepower
grouped_multiple = df.groupby(['cylinders', 'model_year']).agg({'horsepower': ['mean', 'min', 'max']})
#Naming columns in grouped DataFrame
grouped_multiple.columns = ['hp_mean', 'hp_min', 'hp_max']
#Resetting index
grouped_multiple = grouped_multiple.reset_index()
#Viewing head of resulting DataFrame
grouped_multiple.head()
"""


