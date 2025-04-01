#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 16:04:25 2025

@author: ip00517
"""
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
excel = r"C:\Users\ip00517\Downloads\Book1.xlsx"
df = pd.read_excel(excel)

df['Start Date'] = pd.to_datetime(df['Start Date'],format = "%d/%m/%Y")
df['End Date'] = pd.to_datetime(df['End Date'],format = "%m/%d/%Y")
df['Duration'] = df['Duration'].str.replace(" days", "", regex=False).astype(int)
df['Task Duration'] = df['End Date'] - df['Start Date'] + pd.Timedelta(days = 1)
person_colours = {'A':'g','B':'r','C':'b', 'D':'y', 'E':'pink', 'F':'#8B4513', 'G':'#4B0082', 'H':'#FFDAB9', 'I':'#708090'}

fig, ax = plt.subplots()
ax.xaxis_date()
ax.barh(y = df['Task'], width = df['Duration'],
left = df['Start Date'])

patches = []
for person in person_colours:
    patches.append(mpatches.Patch(color=person_colours[person]))


for index, row in df.iterrows():
    ax.barh(y=row['Task'], width=row['Duration'],
    left=row['Start Date'], color=person_colours[row['Persons']],alpha = 1)

# ax.axvline(x = pd.to_datetime("2025-04-27"),color = 'b')
# current_date = pd.to_datetime("2025-04-27")
# ax.text(x = current_date + pd.Timedelta(days = 0.2),y = 2,s= f"Current Date:{current_date.date()}",color = 'b')


ax.set_title('Gantt Chart Project Plan')
ax.set_xlabel('Date')
ax.set_ylabel('Task')
ax.set_xlim(df['Start Date'].min(),df['End Date'].max())
ax.tick_params(axis = 'x', labelrotation = 45)
ax.legend(handles=patches,  labels=person_colours.keys(), fontsize=11,bbox_to_anchor = (1,0.56))

plt.show()