import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

# write your code here
office_a = pd.read_xml('../Data/A_office_data.xml')
office_b = pd.read_xml('../Data/B_office_data.xml')
hr_data = pd.read_xml('../Data/hr_data.xml')

office_a.set_index(keys='A' + office_a.employee_office_id.astype(str), inplace=True)
office_b.set_index(keys='B' + office_b.employee_office_id.astype(str), inplace=True)
hr_data.set_index(keys='employee_id', inplace=True)

office_data = pd.concat(objs=[office_a, office_b], axis=0)
office_data_hr = office_data.merge(hr_data, how='left', left_index=True, right_index=True, indicator=True)
office_data_hr = office_data_hr[office_data_hr['_merge'] == 'both']
office_data_hr.drop(labels=['employee_office_id', '_merge'], axis=1, inplace=True)
office_data_hr.sort_index(inplace=True, ascending=True)

top_10 = office_data_hr.sort_values('average_monthly_hours', ascending=False).index.tolist()[:10]

def count_bigger_5(series):
    count = 0
    for value in series:
        if 5 < value:
            count += 1
    return count

the_dict = office_data_hr.groupby('left').agg({'number_project': ['median', count_bigger_5],
                                               'time_spend_company': ['mean', 'median'],
                                               'Work_accident': 'mean',
                                               'last_evaluation': ['mean', 'std']}).round(2).to_dict()


# pd.set_option('display.max_columns', None)
pivot_table1 = office_data_hr.pivot_table(index='Department',
                                          columns=['left', 'salary'],
                                          values='average_monthly_hours',
                                          aggfunc='median').round(2)

print(pivot_table1[
          (pivot_table1[0.0, 'high'] < pivot_table1[0.0, 'medium'])|
          (pivot_table1[1.0, 'low'] < pivot_table1[1.0, 'high'])].to_dict())

pivot_table2 = office_data_hr.pivot_table(index='time_spend_company',
                                          columns='promotion_last_5years',
                                          values=['satisfaction_level', 'last_evaluation'],
                                          aggfunc=['min', 'max', 'mean']).round(2)

print(pivot_table2[
          pivot_table2['mean', 'last_evaluation', 0] >
          pivot_table2['mean', 'last_evaluation', 1]].to_dict())