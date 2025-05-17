import seaborn as sns
import matplotlib.pyplot as plt

a = sns.get_dataset_names()
print(a)

tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")


sns.histplot(tips["total_bill"], kde=True)
plt.savefig("plot.png")
plt.show()


