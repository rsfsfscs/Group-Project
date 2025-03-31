# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn. preprocessing import PolynomialFeatures


excel = r'C:\Users\ip00517\Downloads\Athletics data 2025.xlsx'

#function for egression lines, n is the polynomial of degree n
def f(x,y,n):
    polyn = PolynomialFeatures(degree=n, include_bias=False)
    polyn_ind_var = polyn.fit_transform(x.reshape(-1, 1))
    poly_regn = LinearRegression(fit_intercept = True)
    poly_regn.fit(polyn_ind_var,y)
    y_predicted_n = poly_regn.predict(polyn_ind_var)
    return y_predicted_n

#format data for 100m
men_100m = pd.read_excel(excel, skiprows=1)
men_100m = men_100m.dropna(subset=['Time (seconds)'])
women_100m = pd.read_excel(excel, sheet_name = 'womens 100m' , skiprows=1)
women_100m['Date'] = pd.to_datetime(women_100m['Date'], format='%B %d, %Y')

plt.scatter(men_100m['Date'], men_100m["Time (seconds)"] )
plt.scatter(women_100m['Date'], women_100m["Time"] )
plt.plot(men_100m['Date'].values, f(men_100m['Date'].values, men_100m['Time (seconds)'].values, 1))
#plt.plot(women_100m['Date'].values, f(women_100m['Date'].values, women_100m['Time'].values, 2))
plt.plot(women_100m['Date'].values, f(women_100m['Date'].values, women_100m['Time'].values, 1))

plt.title('men and women 100m world record')
plt.xlabel('Date')
plt.ylabel('records (seconds)')

plt.show()


# #format data for 1500m
# men_1500m = pd.read_excel(excel, sheet_name="men's 1500m", skiprows=1)
# women_1500m = pd.read_excel(excel, sheet_name = "women's 1500m" , skiprows=2)

# men_1500m['time'] = pd.to_timedelta(men_1500m['time'])
# women_1500m['time'] = pd.to_timedelta(women_1500m['time'])


# plt.scatter(men_1500m['date'], men_1500m["time"] )
# plt.scatter(women_1500m['date'], women_1500m["time"] )
# plt.plot(men_1500m['date'].values, f(men_1500m['date'].values, men_1500m['time'].values, 1))
# plt.plot(women_1500m['date'].values, f(women_1500m['date'].values, women_1500m['time'].values, 1))

# plt.title('men and women 1500m world record')
# plt.xlabel('Date')
# plt.ylabel('records (seconds)')


# plt.show()


#format data for long jump
men_long_jump = pd.read_excel(excel, sheet_name="men's long jump", skiprows=1)
women_long_jump = pd.read_excel(excel, sheet_name = "women's long jump" , skiprows=2)

men_long_jump['year'] = pd.to_datetime(men_long_jump['year'].astype(str) + '-01-01', format='%Y-%m-%d')
women_long_jump['Date'] = pd.to_datetime(women_long_jump['Date'].str.strip(), format= '%d %B %Y')

print(men_long_jump['year'].dtype)  # Should show datetime64[ns]
print(women_long_jump['Date'].dtype)  # Should show datetime64[ns]



plt.scatter(men_long_jump['year'], men_long_jump['distance'] )
plt.scatter(women_long_jump['Date'], women_long_jump['distance (m)'] )
plt.plot(men_long_jump['year'].values, f(men_long_jump['year'].values, men_long_jump['distance'].values, 1))
plt.plot(women_long_jump['Date'].values, f(women_long_jump['Date'].values, women_long_jump['distance (m)'].values, 1))

plt.title('men and women long jump world record')
plt.xlabel('Date')
plt.ylabel('records (m)')


plt.show()












