# %% [markdown]
# Data Set: Employee Attrition Report 
# 
# Resource: https://www.kaggle.com/datasets/whenamancodes/hr-employee-attrition?resource=download 
# 
#  
# 
# Employee attrition, meaning employees leaving the company, is a challenge that plagues many companies across various industries. High employee attrition rates can disrupt workflow, hurt productivity, and incur unneeded training and recruitment costs. Understanding factors that contribute to these rates assists employers in increasing employee retention and overall organizational performance. This data mining project aims to explore employee data to gain knowledge and insights surrounding the reasons that employees leave a company. By analyzing historical data, such as demographics, position characteristics, and compensation, this analysis will be able to uncover patterns and relationships that will show what drives attrition. The findings of this analysis will assist companies to proactively address issues that lead to not being able to retain their employees. By identifying key predictors of attrition, organizations can develop targeted interventions, such as adjusting compensation structures or offering career development. Ultimately, the goal of this project is to provide companies with a data-driven answer to the question involving why they may be losing valued employees. By leveraging data mining techniques, we can empower companies to create a more stable and engaged workplace. Leading us to increase productivity, reduce costs, and a healthier workforce culture.  

# %%
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# set directory
os.chdir(r"C:\Users\headc\Documents\Bellevue\DSC550\Final")

# read the csv data from the files paths into datasets
data1 = pd.read_csv('HR Employee Attrition.csv')

# display dataset
data1.head(10)

# %%
# box chart for attrition by department
# group data by department
attrition_dept = data1.groupby(['Department', 'Attrition']).size().unstack()

# calculate percent attrition
total = attrition_dept.sum(axis = 1)
percent = attrition_dept['Yes'] / total * 100

# plot bar chart
ad = percent.plot(kind = 'bar')
plt.xlabel('Department')
plt.ylabel('Count')
plt.title('Attrition by Department')

# add percentages to the top for attrition
def labels(rects):
    for a in rects: 
        w = a.get_width()
        h = a.get_height()
        x, y = a.get_xy()
        ad.annotate(f'{h:.1f}%', (x + w/2, y + h), ha = 'center', va = 'bottom')
labels(ad.patches)
plt.show()

# %% [markdown]
# The bar graph above reveals the attition rates across different departments. The Sales department ehibits the highest attrition rate, followed by the Human Resources department, and the Research and Development department coming in last. This visualizations shows a comparision between departs and allows us to see at a quick glance where each department stands. This shows that the Sales department should be the one focused on in this analysis. 

# %%
# attrition seperation
att_data = data1[data1['Attrition'] == 'Yes']
no_att_data = data1[data1['Attrition'] == 'No']

# years at the company for each
years_att = att_data['YearsAtCompany']
years_no_att = no_att_data['YearsAtCompany']

# plot
plt.hist(years_no_att, bins = 10, alpha = 0.5, label = 'No Attrition', edgecolor = 'black')
plt.hist(years_att, bins = 10, alpha = 0.5, label = 'Attrition', color = 'red', edgecolor = 'black')
plt.xlabel('Years at Company')
plt.ylabel('Frequency of Attrition')
plt.title('Distribution of Years at Company by Attrition')
plt.legend()
plt.show()

# %% [markdown]
# The histrogram above shows a distribution of years at the company by attrition. It visually represents the frequency of attrition for each bin shown, providing helpful insights into the attrition patterns within the company. If you were to compare the attrition distribution beteen employees with and without attrition, you would notice clear differences. The easiest to notice is that most employee attritions happen within being employed for the first 12 years at a company. Once an employee is at a company for 12 years, it drops dramatically. However, the highest amount of employee attrition happens before an employee is with a company for 5 years. This would mean that retention efforts should be focused on employees who have spent fewer years with the company due to the potential higher turnover rate they pose. 

# %%
# select monthly income and attrition columns
income = data1['MonthlyIncome']
attrition = data1['Attrition']

# Combine data
data2 = pd.DataFrame({'Income Monthly': income, 'Attrition': attrition})

# Calculate the average income of each Attrition
avg_att = data2[data2['Attrition'] == 'Yes']['Income Monthly'].mean()
avg_no_att = data2[data2['Attrition'] == 'No']['Income Monthly'].mean()

# Plot a Box plot
sns.boxplot(x = 'Attrition', y ='Income Monthly', data = data2)
plt.xlabel('Attrition')
plt.ylabel('Income: Monthly')
plt.title('Monthly Income by Attrition')

# Add Average to plot
plt.text(0, avg_att, f'Avg Income: ${avg_att: .2f}', ha = 'center', va = 'bottom')
plt.text(1, avg_no_att, f'Avg Income: ${avg_no_att: .2f}', ha = 'center', va = 'bottom')
plt.show()

# %% [markdown]
# The boxplot shown above is a visual representation of the monthly income for each employee grouped by if they have experienced attrition. It reveals that employees who have experience attrition tend to have a lower monthly income that those who have not. This graph showcases the middle 50% of the income distribution with whiskers that extend to the minimum and maximum non-outlier values. Outliers are identified in the monthly incomes. Out of the employees who have experienced attrition, there are a few outliers. These could be representative of employees who left the company despite their income ranges, which would mean more analysis is needed to find the influencing factors. Because there is a difference in the incomes between the non-effected and effected groups, there may be some work that can be done involving employee salary ranges to prevent attrition. 

# %%
# Map 'Yes' and 'No' to numeric value
data1['Attrition'] = data1['Attrition'].map({'Yes': 1, 'No': 0})

# Groupby Year at the Company and Age, then calculate the count of attrition
attrition_counts = data1.groupby(['Age', 'YearsAtCompany'])['Attrition'].value_counts().unstack()

# Create two subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Plotting the stacked bar chart for the first subplot
axes[0].bar(range(len(attrition_counts)), attrition_counts[0].fillna(0), label='No')
axes[0].bar(range(len(attrition_counts)), attrition_counts[1].fillna(0), bottom=attrition_counts[0].fillna(0), label='Yes')
axes[0].set_xlabel('Age and Years at the Company')
axes[0].set_ylabel('Count')
axes[0].set_title('Distribution of Attrition by Age and Years at the Company - No')
axes[0].set_xticks(range(len(attrition_counts)))
axes[0].set_xticklabels(attrition_counts.index, rotation=45)
axes[0].legend()

# Plotting the stacked bar chart for the second subplot
axes[1].bar(range(len(attrition_counts)), attrition_counts[0].fillna(0), label='No')
axes[1].bar(range(len(attrition_counts)), attrition_counts[1].fillna(0), bottom=attrition_counts[0].fillna(0), label='Yes')
axes[1].set_xlabel('Age and Years at the Company')
axes[1].set_ylabel('Count')
axes[1].set_title('Distribution of Attrition by Age and Years at the Company - Yes')
axes[1].set_xticks(range(len(attrition_counts)))
axes[1].set_xticklabels(attrition_counts.index, rotation=45)
axes[1].legend()
plt.tight_layout()
plt.show()

# %% [markdown]
# The graph above shows the distribution of attrition across different age groups and years at the company. The data is split between the 'No' and 'Yes' answers in employee attrition. The analysis reveals that the highest count of attrition occurs in the age range of 25 to 35 years old. Additionally, the stacking of the bar charts shows the gradual decline in employee attrition as employees stay with the company longer. Age does not seem to have any impact on that number. So, it would show us that keeping employees long would decrease employee attrition no matter the age of the employee. 

# %% [markdown]
# While this data set is large, breaking it down into multiple charts have helped us to identify some key criteria. The bar graph that display the employee attrtion by different departments revealed that the Sales department had the highest attrition rate, while the lowest was held by the Development and Human Resources department. The histogram depicts the distribution of employee attrition based on years of employment at the company. This showed indications that a significant portion of employee attrition happens within the first 5 years of working for a company. With a large decrease in attrition once an employee is employed for more than 12 years. Monthly income also plays a factor in keeping employees happy; however, the income difference between the ones that leave and stay was slight. Lastly, looking at attention rate by age and years with the company showed that the highest count of attrition occurs in the age range of 25 to 35 years old.

# %% [markdown]
# Milestone 2: Assignment 7.2
# Due: July 23, 2023

# %%
# Drop any features that will not assist the model
data1_drop = data1.copy()
features_drop = ['EmployeeCount', 'EmployeeNumber', 'StandardHours', 'Over18']
data1_drop = data1_drop.drop(features_drop, axis = 1)

# Print new dataset
data1_drop.head(10)

# %% [markdown]
# The above features were dropped because:
# 
# EmployeeCount: This feature has a constant value for all employees. It will not provide any useful information in trying to understand attrition. 
# 
# EmployeeNumber: This feature is just an identifier for employees and is unlikely to have any predictive power for attrition. 
# 
# StandardHours: Since the standard work hours are the same for all employees, this feature does not contribute to understanding why there is employee attrition. 
# 
# Over18: This is standard for all employees, since they must all be over 18 to work for the company. 

# %%
# select target variable
target = data1_drop['Attrition']

# handle categorical variables 
data1_drop = pd.get_dummies(data1_drop, drop_first=True)

# deal with missing values, if there are any
data1_drop = data1_drop.fillna(data1_drop.mean())

# print dataset
data1_drop.head(10)

# %%
# handle missing values
imputer = SimpleImputer(strategy='mean') # this step was added after trying to run the model and an 'NaN' value errors was encountered
data1_drop = pd.DataFrame(imputer.fit_transform(data1_drop), columns=data1_drop.columns)


# %%
# Calculate optimal number of bins using data points n 
n_age = data1['Age'].shape[0]
n_years = data1['TotalWorkingYears'].shape[0]
SR_bin_age = int(np.sqrt(n_age))
SR_bin_years = int(np.sqrt(n_years))

# print
print('Age: ', SR_bin_age)
print('Total Working Years: ', SR_bin_years)

# %% [markdown]
# Although the found optimal bin using the sqaure root is 38 for both, that seems unlikely. I will try with 6 bins, and work my way through some. Once I find a number of bins that fits, I will continue with the evaluation. 

# %%
# Normalize/Scale the numerical features of Age and TotalWorkingYears
numerical_features = ['Age', 'TotalWorkingYears']
scaler = MinMaxScaler()
data1_drop[numerical_features] = scaler.fit_transform(data1_drop[numerical_features])

# Select binned features
features_to_bin = ['Age', 'TotalWorkingYears']

# Bin loop
for feature in features_to_bin:
    data1_drop[f'{feature}_bin'] = pd.cut(data1_drop[feature], bins=5, labels=False)

# Drop the original numerical features
data1_drop.drop(features_to_bin, axis=1, inplace=True)

# Print transformed data
data1_drop.head(10)

# %% [markdown]
# The step above uses equal-width binning to normalize the features 'Age' and 'TotalWorkingHours'. The numerical features were done first with Min-Max scaling to ensure consistent range before binning. Binning these features will allow the model to be more robust to outliers. It will also increase the model's performance because it is limiting the complexity. Like Age being binned into 5 bins will decrease how many different ages there are. This could help the decision tree perform better. 

# %%
# create histogram to check binning
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(data1_drop['Age_bin'], bins=5, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Age - Binned')

# edit xticks to be age ranges
age_range = ['20-29', '30-39', '40-49', '50-59', '60-69']
plt.xticks(range(5), age_range)

# print
plt.tight_layout
plt.show()

# %%
# Histogram to check bins for TotalWorkingYears
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 2)
plt.hist(data1_drop['TotalWorkingYears_bin'], bins=5, edgecolor='black')
plt.xlabel('Total Working Years')
plt.ylabel('Frequency')
plt.title('Histogram of Total Working Years- Binned')

# set working years ranges
year_range = [f'{int(data1["TotalWorkingYears"].min() + i * (data1["TotalWorkingYears"].max() - data1["TotalWorkingYears"].min()) / 5)}-{int(data1["TotalWorkingYears"].min() + (i + 1) * (data1["TotalWorkingYears"].max() - data1["TotalWorkingYears"].min()) / 5)}' for i in range(5)]
plt.xticks(range(5), year_range)

# print
plt.tight_layout
plt.show()

# %% [markdown]
# The histograms for Age and TotalWorkingYears were created using 5 bins. The calculation from the Square Root Rule seemed incorrect for the optimal amount. These visualizations depict the frequency of employee attrition for each range. The chosen bin number of 5 seems to be reasonable given that is provides a clear overview of both the age and total working years distributions without excessive granularity or loss of important patterns. This result was also tested with 10. Although the ranges were smaller, I think that 10 bins could also have worked out well. 

# %%
# Engineering new features
data1_drop['YearsSinceLastPromotionRatio'] = data1_drop['YearsSinceLastPromotion']/data1_drop['TotalWorkingYears_bin']
hours_per_month = 160  # 160 hrs/month based on the drop column StandardHours

# new feature for HourlyRate to show each employee earns per hour
data1_drop['HourlyRate'] = data1_drop['MonthlyIncome']/hours_per_month

# JobHopper column to see if they transfer jobs or have stayed. Set to be above 2 moves. 
data1_drop['JobHopper'] = (data1_drop['NumCompaniesWorked'] > 2).astype(int)

# Promotion within the last year to see if employees with a recent promotion tend to stay
data1_drop['PromotionInLastYear'] = (data1_drop['YearsSinceLastPromotion'] == 0).astype(int)

# Define income brackets for the IncomeCategory feature
income_brackets = [0, 4000, 8000, float('inf')]
income_labels = ['Low', 'Medium', 'High']
data1_drop['IncomeCategory'] = pd.cut(data1_drop['MonthlyIncome'], bins=income_brackets, labels=income_labels)

# print data
data1_drop.head(10)

# %% [markdown]
# There were several feaetures added in the above dataset. 
# 
#     1. YearsSinceLastPromotionRatio is the ratio of 'YearsSinceLastPromotion' to 'TotalWorkingYears'. This feature captures the rate of promotions relative to how long an employee stays with the company. This could potential indicate whether the company assists in career growth which would be appealing to employees.
# 
#     2. HourlyRate is the income per hour earned calculated using the 'MonthlyIncome' divided by the standard hours worked for a month. The StandardHours feature was earlier removed since all employees had the same result. This would assist in identifying employees that may be underpaid for their position or time at the company relative to their working hours. 
# 
#     3. JobHopper works to identify employees who have worked for more than 2 companies. It is derived from the 'NumCompaniesWorked' feature. This would mean that they are more than likely job hopping from company to company. There would be little to do to keep them. 
# 
#     4. PromotionInLastYear is a binary feature that shows whether the company has promoted that employee within the last year. This column could be used to see if employees generally stay longer if they are promoted earlier that year. 
# 
#     5. IncomeCategory was a category feature that puts 'MonthlyIncome' into 3 different brackets ('Low, Medium, High'). These brackets can be used to see a more granular view of the salary levels. 
#     

# %%
# use new features to see attrition by IncomeCategory
plt.figure(figsize=(10, 6))
sns.countplot(x='IncomeCategory', hue='Attrition', data=data1_drop, palette='pastel')
plt.xlabel('Income Category')
plt.ylabel('Count')
plt.title('Attrition by Income Category')
plt.legend(title='Attrition', loc='upper right', labels=['No', 'Yes'])
plt.xticks(rotation=0, ha='right')
plt.tight_layout()
plt.show()

# %% [markdown]
# The above plot shows that there is a higher attrition rate with employees that fall into the 'low' income category. This could be brocken down into the original 'MonthlyIncome' feature to see what the potential salary range is for the 'Low' bracket. 

# %%
# use new features to see attrition by JobHopper
plt.figure(figsize=(10, 6))
sns.countplot(x='JobHopper', hue='Attrition', data=data1_drop, palette='pastel')
plt.xlabel('Job Hopper')
plt.ylabel('Count')
plt.title('Attrition by Job Hoppers')
plt.legend(title='Attrition', loc='upper right', labels=['No', 'Yes'])
plt.xticks(rotation=0, ha='right')
plt.tight_layout()
plt.show()

# %% [markdown]
# The above graph shows that there is not a significant difference between employees that have worked for more than 2 companies and employees that have not worked for more companies. Meaning that employee attrition for this company is not impacted by those who are Job Hopping. 

# %%
# use new features to see attrition by PromotionInLastYear
plt.figure(figsize=(10, 6))
sns.countplot(x='PromotionInLastYear', hue='Attrition', data=data1_drop, palette='pastel')
plt.xlabel('Recent Promotions - Last 12 months')
plt.ylabel('Count')
plt.title('Attrition by Yearly Promotions')
plt.legend(title='Attrition', loc='upper right', labels=['No', 'Yes'])
plt.xticks(rotation=0, ha='right')
plt.tight_layout()
plt.show()

# %% [markdown]
# The above graph shows that there is not a significant difference in employee attrition between empployees that have had a promotion in the last 12 months and employees who have not. This would mean that this does not pose a significant effect on employees staying with the company. 

# %%
# perform one-hot encoding on categorical features
data1_encoded = pd.get_dummies(data1_drop, drop_first=True) # this was done because of an error I got about the 'Low', 'Medium, and 'high' values

# Seperate features into a training and test set
X = data1_encoded.drop('Attrition', axis=1)
y = data1_encoded['Attrition']

# Split the data into training and test set (80% train to 20/5 test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)

# Print results
print('Training set shape: ', X_train.shape, 'y_train shape: ', y_train.shape)
print('Testing set shape: ', X_test.shape, 'y_test shape: ', y_test.shape)

# %% [markdown]
# At this point, the data is prepared for models to be performed.


