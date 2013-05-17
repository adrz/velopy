import csv
import numpy as np
import json
import matplotlib.pyplot as plt
import matplotlib
#from datetime import MinuteLocator, Hourlocator, Daylocator
import datetime


csv_file = open('logs/2013-05-16_2.csv','r')
csv_data = csv.DictReader(csv_file, fieldnames = ("num","lat","long","banking","bonus","status","stands","free_stands","free_bikes","update"))
csv_list = list(csv_data)

a_freebikes 	= []
a_update 	= []
a_freestands 	= []
a_date 		= []

for line in csv_list:
	if line['num'] == '13011':
		a_freebikes.append(float(line['free_bikes']))
		tmp_time = float(line['update'])/1000
		a_update.append(tmp_time)
		#a_date.append()
		a_freestands.append(float(line['free_stands']))



# Sorting
idx_sort = np.argsort(a_update)
a_update = np.sort(a_update)
a_update = a_update #- array_update[0]
for t in a_update:
	a_date.append( datetime.datetime.fromtimestamp(t) )#.strftime('%Y-%m-%d %H:%M:%S'))

a_freebikes = np.take(a_freebikes, idx_sort)
a_freestands = np.take(a_freestands, idx_sort)

plt.plot(a_date, a_freebikes)
plt.gcf().autofmt_xdate()
plt.show()

#dates = matplotlib.dates.date2num(a_update)

#dates = matplotlib.dates.date2num(a_date)
## Ploting
#fig = plt.figure(1)
#plt.plot_date(dates, a_freebikes)
##plt.plot(array_update, array_freestands,'r')
#plt.show()
