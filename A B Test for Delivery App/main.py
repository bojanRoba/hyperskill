# write your code here
# from operator import index
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as st
# from statsmodels.stats import power
# import matplotlib.pyplot as plt


# 01 Sampling Strategy --

# data_frame = pd.read_csv(r'data\aa_test.csv')
# sample_1 = data_frame['Sample 1']
# sample_2 = data_frame['Sample 2']
#
# stat, p = st.levene(sample_1, sample_2, center='mean')
# # H0, The variances of a given samples are equal.
# # H1, The variances of a given samples are NOT equal.
#
# print(f'''Levene's test
# W = {round(stat, 3)}, p-value {'> 0.05' if p > 0.05 else '<= 0.05'}
# Reject null hypothesis: {'no' if p > 0.05 else 'yes'}
# Variances are equal: {'yes' if p > 0.05 else 'no'}''')
#
#
# stat, p = st.ttest_ind(sample_1, sample_2, equal_var=True)
# # H0, The means of a given sample are equal
# # H1, The means of a given sample NOT are equal
#
# print(f'''
# T-test
# t = {round(stat, 3)}, p-value {'> 0.05' if p > 0.05 else '<= 0.05'}
# Reject null hypothesis: {'no' if p > 0.05 else 'yes'}
# Means are equal: {'yes' if p > 0.05 else 'no'}''')


# 02 Sample Size Calculation --

# data_frame = pd.read_csv(r'data\ab_test.csv')
# ss_group = power.tt_ind_solve_power(effect_size=0.2, alpha=0.05, power=0.8)
# print(f'''Sample size: {int(((ss_group//100)+1)*100)}  # it is the result of power analysis
#
# Control group: {data_frame[data_frame.group == 'Control'].group.count()}
# Experimental group: {data_frame[data_frame.group == 'Experimental'].group.count()}''')


# 03 Know Your Clients --

data_frame = pd.read_csv(r'data\ab_test.csv')
# data = data_frame.pivot_table(values='session_duration',
#                               index='date',
#                               columns='group',
#                               aggfunc='count').reset_index()
#
# data['day'] = pd.to_datetime(data['date']).dt.day
# data['month'] = pd.to_datetime(data['date']).dt.month
# data[['Control', 'Experimental', 'day']].set_index('day').plot(kind='bar')
# plt.xlabel('June')
# plt.ylabel('Number of sessions')
# # plt.legend(loc=9)
# plt.tight_layout()
# plt.show()  # plt.savefig('f_plot.png')
#
# # 2
# pd.DataFrame.hist(data=data_frame, column='order_value', by='group',legend=False)
# plt.xlabel('Order value')
# plt.ylabel('Frequency')
# plt.tight_layout()
# plt.show()  # plt.savefig('s_plot.png')
#
# # 3
# pd.DataFrame.hist(data=data_frame, column='session_duration', by='group', legend=False)
# plt.xlabel('Session duration')
# plt.ylabel('Frequency')
# plt.tight_layout()
# plt.show()  # plt.savefig('t_plot.png')

ov_limit = np.percentile(data_frame['order_value'], 99)
sd_limit = np.percentile(data_frame['session_duration'], 99)

filtered_data = data_frame[(data_frame.order_value < ov_limit)&
                           (data_frame.session_duration < sd_limit)]

# print(f'Mean: {round(filtered_data.order_value.mean(), 2)}')
# print(f'Standard deviation: {round(filtered_data.order_value.std(ddof=0), 2)}')
# print(f'Max: {round(filtered_data.order_value.max(), 2)}')


# 04 Non-Parametric A/B Test --

# H0: The two populations are equal
# H1: The two populations are NOT equal

# ov_con = filtered_data[filtered_data.group == 'Control'].order_value
# ov_exp = filtered_data[filtered_data.group == 'Experimental'].order_value
#
# U1, p = st.mannwhitneyu(ov_con, ov_exp, method='exact')
# nx, ny = len(ov_con), len(ov_exp)
# U2 = nx*ny - U1
# print(f'U1: {U1}')
# print(f'U2: {U2}')

# _, pnorm = st.mannwhitneyu(ov_con, ov_exp, method='asymptotic')
# print(f'p: {p}')
# print(f'pnorm: {pnorm}')

# print(f'''Mann-Whitney U test
# U1 = {round(U1, 2)}, p-value {'<=' if p <= 0.05 else '>'} 0.05
# Reject null hypothesis: {'yes' if p <= 0.05 else 'no'}
# Distributions are same: {'no' if p <= 0.05 else 'yes'}''')


# 05 Double Check with the Parametric A/B Test --

col_series = filtered_data['order_value'].apply(np.log)
filtered_data = filtered_data.assign(log_order_value=col_series.values)

filtered_data.hist(column='log_order_value', bins=30, grid=False, legend=True)
plt.title('Log Order Value')
plt.tight_layout()
plt.show()

sample_1 = filtered_data[filtered_data.group == 'Control'].log_order_value
sample_2 = filtered_data[filtered_data.group == 'Experimental'].log_order_value

stat, p = st.levene(sample_1, sample_2)
# H0, The variances of a given samples are equal.
# H1, The variances of a given samples are NOT equal.

print(f'''Levene's test
W = {round(stat, 3)}, p-value {'>' if p > 0.05 else '<='} 0.05
Reject null hypothesis: {'no' if p > 0.05 else 'yes'}
Variances are equal: {'yes' if p > 0.05 else 'no'}''')

stat, p = st.ttest_ind(sample_1, sample_2, equal_var=False)
# H0, The means of a given sample are equal
# H1, The means of a given sample NOT are equal

print()
print(f'''T-test
t = {round(stat, 3)}, p-value {'>' if p > 0.05 else '<='} 0.05
Reject null hypothesis: {'no' if p > 0.05 else 'yes'}
Means are equal: {'yes' if p > 0.05 else 'no'}''')