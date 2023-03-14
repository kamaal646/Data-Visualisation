import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='ticks', color_codes=True)

titanic = sns.load_dataset('titanic')

print(titanic)

sns.countplot(x='pclass', hue='class', data=titanic )
plt.show()