import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Saturn V edited_20231221215230.csv")

plt.style.use('dark_background')
plt.rcParams['figure.figsize'] = [10, 7]
plt.rc('axes', edgecolor='#FFE9CC')
plt.rc('axes', labelcolor='#FFE9CC')
plt.rc('axes', titlecolor='#FFE9CC')
plt.rc('xtick', color='#FFE9CC')
plt.rc('ytick', color='#FFE9CC')

plt.figure(figsize=(10, 5))
plt.plot(df['TimeSinceMark'], df['AltitudeTrue'], label='Высота от времени', color="#C24124")
plt.title('Зависимость высоты от времени')
plt.xlabel('Время (с)')
plt.ylabel('Высота (м)')
plt.legend()
plt.grid(True)
plt.show()
