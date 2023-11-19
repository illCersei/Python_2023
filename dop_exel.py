import pandas as pd
import matplotlib.pyplot as plt

file = 'df.csv'
xd = pd.read_csv(file)

df = xd[xd["name"] == "Average salary"]
regions = list(df.region.unique())
salary = {}
for i in regions:
    temp = df[df["region"] == i]
    salary.update({i:temp["value"].mean()})
#print((salary))

salary = dict(sorted(salary.items(), key = lambda x: x[1], reverse=True))
plt.rcParams['figure.figsize'] = (18,9)

salary_list = list(salary.keys())
index = salary_list.index("Russia")

x = range(len(salary))
ax = plt.gca()
ax.bar(x,salary.values())
ax.set_xticks(x)
ax.tick_params(labelsize="large")
ax.set_xticklabels(salary.keys(), rotation='vertical', fontsize=10)

plt.setp(ax.get_xticklabels()[index], color='red')


plt.tight_layout()
plt.show()