import pandas as pd 



#data
subscriptions = [
    {"user_id": 1, "name": "Ana", "plan": "Premium", "monthly_fee": 20, "months_active": 12, "city": "Beograd", "start_date": "2024-01-05"},
    {"user_id": 2, "name": "Marko", "plan": "Basic", "monthly_fee": 10, "months_active": 5, "city": "Novi Sad", "start_date": "2024-01-10"},
    {"user_id": 3, "name": "Jelena", "plan": "Premium", "monthly_fee": 20, "months_active": 8, "city": "Niš", "start_date": "2024-02-01"},
    {"user_id": 4, "name": "Petar", "plan": "Standard", "monthly_fee": 15, "months_active": 3, "city": "Beograd", "start_date": "2024-02-15"},
    {"user_id": 5, "name": "Ivana", "plan": "Premium", "monthly_fee": 20, "months_active": 10, "city": "Kragujevac", "start_date": "2024-03-01"},
    {"user_id": 6, "name": "Nikola", "plan": "Basic", "monthly_fee": 10, "months_active": 2, "city": "Novi Sad", "start_date": "2024-03-10"},
    {"user_id": 7, "name": "Milica", "plan": "Standard", "monthly_fee": 15, "months_active": 6, "city": "Beograd", "start_date": "2024-04-01"},
]

#create a DataFrame and perform analysis

df = pd.DataFrame(subscriptions)
print(df.head())
print(df.info())
print(df.dtypes)
print(df.describe())
print(df.isna().sum())

#adding new column revenue

df['revenue'] = df['monthly_fee'] * df['months_active']
print(df[['name','revenue']])

#converting start_date u datetime

df['start_date'] = pd.to_datetime(df['start_date'])

#adding new column month

df['month'] = df['start_date'].dt.month


#kpi analysis
#total_revenue

total_revenue = df['revenue'].sum()
print('Total revenue:',total_revenue)

#average revene per customer 

avg_revenue_per_customer = df.groupby('name')['revenue'].mean()
print('Average revenue per customer:', avg_revenue_per_customer)


#best subscription plan

best_subscription_plan = df.groupby('plan')['revenue'].sum().sort_values(ascending = False).head(1)
print('Best subscription plan is :',best_subscription_plan)

# city with highest revenue 

top_city_by_revenue = df.groupby('city')['revenue'].sum().sort_values(ascending = False).head(1)
print('Top city by revenue:',top_city_by_revenue)

#number of users per subscription plan

num_of_users_per_plan = df.groupby('plan')['user_id'].count()
print('Number of users per plan:',num_of_users_per_plan)

#loyal users

loyal_users = df[df['months_active']>=6]
print('Loyal users:',loyal_users[['name','months_active']])


#revenue per customer 

revenue_per_customer = df.groupby('name')['revenue'].sum()
print('Revenue per customer:',revenue_per_customer)

#average active_months per plan

avg_active_months_per_plan = df.groupby('plan')['months_active'].mean()
print('Average active months per plan:',avg_active_months_per_plan)

#revenue per month

revenue_per_month = df.groupby('month')['revenue'].sum().reset_index()
print('Revenue per month:',revenue_per_month)

#number of new users per month

num_of_new_users_per_month = df.groupby('month')['user_id'].nunique()
print('Number of new users per month:',num_of_new_users_per_month)

#visualization 

#barchart revenue per plan

import matplotlib.pyplot as plt 
import seaborn as sns 

plt.figure(figsize = (10,6))
sns.barplot(data =df,x ='plan',y = 'revenue',color = 'red')
plt.title('Revenue per subscription plan')
plt.xlabel('Subscription plan')
plt.ylabel('Revenue')
plt.show()

#revenue per month lineplot

plt.figure(figsize = (10,6))
sns.lineplot(data = revenue_per_month,x = 'month',y = 'revenue',marker = "o",color = 'Blue')
plt.title('Revenue per month')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.grid(True)
plt.show()

#number of users per plan countplot

plt.figure(figsize = (10,6))
sns.countplot(data = df,x = 'plan',color = 'Green')
plt.title('Number of users per subscription plan')
plt.xlabel('Subscription plan')
plt.ylabel('Number of users')
plt.show()

#heatmap correlation between monthly_fee,months_active and revenue

corr_matrix = df[['monthly_fee', 'months_active', 'revenue']].corr()
sns.heatmap(corr_matrix,annot = True,cmap = 'Blues')
plt.title('Correlation matrix')
plt.show()

#box plot total revenue

plt.figure(figsize = (10,6))
sns.boxplot(data = df, x = 'revenue', color = 'Purple')
plt.title('Total revenue distribution')
plt.xlabel('Total revenue')
plt.show()