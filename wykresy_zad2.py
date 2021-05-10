
import pandas as pd
import matplotlib.pyplot as plt

xlsx=pd.ExcelFile('datasets\imiona.xlsx')
  df1 = pd.read_excel(xlsx,)

data = pd.read_excel(xlsx, header=0)

  df = pd.DataFrame(data)

dane = df.groupby(['Plec']).agg({'Liczba': {'sum'}})

  wykres = dane.plot.bar()
  wykres.set_ylabel('Mld')

plt.show()
