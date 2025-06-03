# write your code here
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)

general_df = pd.read_csv(r'test\general.csv')
prenatal_df = pd.read_csv(r'test\prenatal.csv')
sports_df = pd.read_csv(r'test\sports.csv')


for data_set in [general_df, prenatal_df, sports_df]:
    # print(data_set.columns.tolist())
    data_set.columns = [col_name.lower() for col_name in data_set.columns]

prenatal_df.rename(columns={'sex': 'gender'}, inplace=True)
sports_df.rename(columns={'male/female': 'gender'}, inplace=True)

hospital_df = pd.concat(
    objs=[general_df, prenatal_df, sports_df], axis=0, ignore_index=True).drop(
    labels='unnamed: 0', axis=1)

hospital_df.dropna(axis=0, how='all', inplace=True)

def one_letter_gender(s):
    return 'm' if s[0] == 'm' else 'f'


hospital_df['gender'] = hospital_df.gender.fillna('f')
hospital_df['gender'] = hospital_df.gender.apply(one_letter_gender)

for col in hospital_df.columns:
    if hospital_df[col].dtype == float:
        hospital_df[col] = hospital_df[col].fillna(0)
    else:
        hospital_df[col] = hospital_df[col].fillna('0')


stomach_perc = round((hospital_df[(hospital_df.hospital == 'general')&
                                  (hospital_df.diagnosis == 'stomach')].diagnosis.count() /
                      hospital_df[(hospital_df.hospital == 'general')].diagnosis.count()), 3)


dislocation_perc = round((hospital_df[(hospital_df.hospital == 'sports')&
                                      (hospital_df.diagnosis == 'dislocation')].diagnosis.count() /
                          hospital_df[(hospital_df.hospital == 'sports')].diagnosis.count()), 3)


median_age_diff = (hospital_df[hospital_df.hospital == 'general'].age.median() -
                   hospital_df[hospital_df.hospital == 'sports'].age.median())


hospital = hospital_df[hospital_df.blood_test == 't'].hospital.value_counts(dropna=False).index[0]
test_num = hospital_df[hospital_df.blood_test == 't'].hospital.value_counts(dropna=False).values[0]

# print(f'The answer to the 1st question is {hospital_df.hospital.value_counts().index[0]}')
# print(f'The answer to the 2nd question is {stomach_perc}')
# print(f'The answer to the 3rd question is {dislocation_perc}')
# print(f'The answer to the 4th question is {median_age_diff}')
# print(f'The answer to the 5th question is {hospital}, {test_num} blood tests')

hospital_df.plot(column='age', kind='hist', bins=[15, 35, 55, 70, 80])
plt.show()

hospital_df.diagnosis.value_counts().plot.pie(subplots=True)
plt.show()

fig, axes = plt.subplots()
axes.violinplot(dataset = hospital_df.height)
plt.show()

print(f'''The answer to the 1st question: {'15-35'}
The answer to the 2nd question: {hospital_df.diagnosis.value_counts().index[0]}
The answer to the 3rd question: It's because imperial vs. metric measures''')