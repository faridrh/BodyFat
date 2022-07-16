import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('surveyofbodyfat.csv', header =0)
df['BMI']= df.apply(
    lambda row: (row.Weight/(row.Height)**2)*703, axis= 1
)

print(df)
y= df.corr()
print(y)

fig, ax1= plt.subplots()
ax1.boxplot(df.BodyFat)
ax1.set_ylabel('Body Fat', fontsize=15)
print (np.average(df.BodyFat), np.max(df.BodyFat), np.min(df.BodyFat))
fig, ax2 = plt.subplots()
x= df.Abdomen
y= df.BodyFat
ax2.scatter(x,y)
ax2.set_xlabel('Abdomen', fontsize=15)
ax2.set_ylabel('Body Fat', fontsize=15)
ax2.set_title('Abdomen and Body Fat scatter plot')
fig, ax3 = plt.subplots()
z= df.Hip
ax3.scatter(z,y)
ax3.set_xlabel('Hip', fontsize=15)
ax3.set_ylabel('Body Fat', fontsize=15)
ax3.set_title('Hip and Body Fat scatter plot')
fig, ax4 = plt.subplots()
k= df.Weight
ax4.scatter(k,y)
ax4.set_xlabel('Weight', fontsize=15)
ax4.set_ylabel('Body Fat', fontsize=15)
ax4.set_title('Weight and Body Fat scatter plot')
plt.show()
fig, ax5 = plt.subplots()
m= df.Height
ax5.scatter(m,y)
ax5.set_xlabel('Height', fontsize=15)
ax5.set_ylabel('Body Fat', fontsize=15)
ax5.set_title('Height and Body Fat scatter plot')
plt.show()
