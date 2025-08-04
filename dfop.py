"""Problem Statement:
The teacher does not want to reveal the marks of students who have failed.
The condition is that if a student has scored marks >= 33, 
then they have passed, otherwise failed. 
The marks of failed students has to be replaced with ‘Fail’. 
So, how can the task be performed?."""
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


# we will use simple dataset data is stored in dictionart 
marks = [{'Chemistry': 67, 'Physics': 45, 'Mathematics': 50, 'English' : 19},
        {'Chemistry': 90, 'Physics': 92, 'Mathematics': 87, 'English' : 90}, 
        {'Chemistry': 66, 'Physics': 72, 'Mathematics': 81, 'English' : 72}, 
        {'Chemistry': 32, 'Physics': 40, 'Mathematics': 12, 'English' : 68}]

#-----converting data into pandas dataframe 
marks_df = pd.DataFrame(marks, index = ['Subodh', 'Ram', 'alex', 'John'])

marks_df['student'] = ['Subodh', 'Ram', 'alex', 'John']
#----display data from dictionary 
#print(marks_df)

#-----if you want information about DF 
#print(marks_df.info())


#----how head works
#print(marks_df.head(n=3))   # first 5 values
# print(marks_df.tail())   # las 5 values 


# working on rows and columns 
# select rows only by label  using loc[]
#print(marks_df.loc['Ram'])

#----slice by rows using index position 
#print(marks_df[2:5])

#print(marks_df.iloc[:1])

# select multiple rows and multiple columns with slice method 
#print(marks_df.iloc[2:5,0:2])

# Grouping of Data 
#marks_df['Student'] =['Subodh', 'Ram', 'alex', 'John']
#marks_df['Result'] = marks_df['English'].apply(lambda x: 'Fail' if x < 33 else 'Pass')
#grouped = marks_df.groupby('Result').mean(numeric_only=True)
#print(grouped)






# print statistics 
#print(marks_df.describe())

# ---------------------------------Masking operation 
#----firt try with this 
#f = marks_df < 33
#marks_df.mask(f, 'Fail')

# then this 
#marks_df =marks_df.mask(f, 'Fail') 
#print(marks_df)

#The teacher wants to award five bonus marks to all the students.
#new_marks = marks_df + 5
#print(new_marks)


#----------------------------------------Sorting 
#sorted_df = marks_df.sort_values(by='Physics', ascending=False)
#print(sorted_df)






#The teacher wants to increase the marks of all the students as follows-

#Chemistry: + 5  Physics: + 10 Mathematics: +10  English: + 2
#new_marks = marks_df + [5,10,10,2]
#print(new_marks.head())


# transpose : rows become column and column becomes rows 
#print(marks_df .T)




# Barplot 

"""

marks_df.set_index('student')[['Chemistry', 'Physics', 'Mathematics', 'English']].plot(kind='bar', figsize=(10,6))
plt.title("Subject-wise Marks for Each Student")
plt.ylabel("Marks")
plt.xticks(rotation=0)
plt.legend(title="Subjects")
plt.grid(True)
plt.tight_layout()
plt.show()
"""

#line plot
"""
marks_df.set_index('student', inplace=True)
marks_df.T.plot(kind='line', marker='o', figsize=(10, 6))
plt.title("Subject-wise Trend Across Students")
plt.ylabel("Marks")
plt.xlabel("Subjects")
plt.grid(True)
plt.tight_layout()
plt.show()

"""