import matplotlib.pyplot as plt
import math
import pandas as pd
import seaborn as sns

figure, axes = plt.subplots()
data=pd.read_csv('data_real.csv', delimiter=';')
print(data)


fecal= data[data["sample_type"] == "fecal"][["mouse_ID", "treatment", "experimental_day", "counts_live_bacteria_per_wet_g"]]
plt.figure(figsize=(11,4))
for mouse_id in fecal ["mouse_ID"]:
     mouse = fecal [fecal ["mouse_ID"] == mouse_id]
     plt.plot( mouse["experimental_day"], mouse["counts_live_bacteria_per_wet_g"], label=f" Mouse {mouse_id} ({mouse['treatment'].iloc[0]})")
plt.title('Fecal live bacteria', fontsize=12)
plt.xlabel('Washout day', fontsize=12)
plt.ylabel('(log10)Live bacteria/ wet g', fontsize=12)
plt.yscale("log")
plt.legend(bbox_to_anchor=(1.00, 1), loc='best', fontsize= 12)
plt.tight_layout()
plt.savefig('fecal live bacteria_line_chart.png', dpi=300)
plt.show()
plt.close()


cecal = data[(data["sample_type"] == "cecal") & (data["mouse_age_days"] == 21)][["treatment","experimental_day", "counts_live_bacteria_per_wet_g"]]
plt.figure(figsize=(11,4))
sns.violinplot(x= 'treatment', y = 'counts_live_bacteria_per_wet_g', data = cecal)
plt.title('Cecal live bacteria', fontsize=12)
axes.set_xlabel('treatment', fontsize=12)
axes.set_ylabel('(log10)Live bacteria/ wet g', fontsize=12)
plt.yscale("log")
plt.grid(6)
figure.savefig('cecal live bacteria_violin_chart.png', dpi=300)
plt.show()
plt.close()


ileal = data[(data["sample_type"] == "ileal") & (data["mouse_age_days"] == 21)][["treatment", "experimental_day", "counts_live_bacteria_per_wet_g"]]
plt.figure(figsize=(11,4))
sns.violinplot(x= 'treatment', y = 'counts_live_bacteria_per_wet_g', data = ileal)
plt.title('Ileal live bacteria', fontsize=12)
axes.set_xlabel('treatment', fontsize=12)
axes.set_ylabel('(log10)Live bacteria/ wet g', fontsize=12)
plt.yscale("log")
plt.grid(6)
figure.savefig('ileal live bacteria_violin_chart.png', dpi=300)
plt.show()
plt.close()


print(" ok ")