import matplotlib.pyplot as plt

Year=[2017,2018,2019,2020]
Population=[18, 19, 20, 21]
	  
plt.bar(Year, Population)

plt.xlabel('Year')
plt.ylabel('Population in lakhs')

plt.title('Population Graph of Mumbai')

plt.show()
