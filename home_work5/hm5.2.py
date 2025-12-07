import pandas as pd
import numpy as np

file = pd.read_csv("tested.csv")

#1
surv_men = np.mean(file[file['Sex'] == 'male']['Survived'])*100
surv_women = np.mean(file[file['Sex'] == 'female']['Survived'])*100
print(surv_men, surv_women)

age_men = np.mean(file[file['Sex']== 'male']['Age'])
age_women = np.mean(file[file['Sex'] == 'female']['Age'])
print(age_men, age_women)

for sex in ['male', 'female']:
    for surv in [1,0]:
        age_surv = np.mean(file[(file['Sex'] == sex)&(file['Survived']==surv)]['Age'])
        print(age_surv)

#2
fil1 = file[(file['Age'] > 30) & (file['Sex'] == 'male') & (file['Pclass'] == 1)]
fil2 = file[((file['Age'] < 18) | (file['Sex'] == 'female'))&(file['Survived'] == 1)]

grouped = file.groupby(['Pclass', 'Sex'])

print(grouped['Age'].apply(np.mean))
print(grouped['Survived'].apply(np.mean))
print(grouped['Fare'].apply(np.mean))