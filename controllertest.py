##### The code for data analytics of tests performed to evaluate the microgrid master controller
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read the info from HR info excel file
infoloc = "C:\\Users\\Saeed Mohajeryami\\Dropbox\\DOE project\\Data from Dr\\BCM HIL PI Point List Draft 1 - 20161108.xlsx"
measurement = pd.read_excel(infoloc,sheet_name='Measurement')
status = pd.read_excel(infoloc,sheet_name='Status (feedback)')
setpoint = pd.read_excel(infoloc,sheet_name='Setpoint')
commands = pd.read_excel(infoloc,sheet_name='Commands')




# print(commands.head())
Fileloc = 'C:\\Users\\Saeed Mohajeryami\\Dropbox\\DOE project\\tests\\3.1 AI-1.csv'
AI1 = pd.read_csv(Fileloc)

F_11_VrmsA = AI1['1'][1:]
time = pd.DataFrame(np.arange(1,len(F_11_VrmsA)+1))

print(type(time))

## plot
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(time,F_11_VrmsA)
# ax1.set_ylim(bottom=50,top=110)
# plt.tight_layout()
# plt.show()
# print(type(AI1))

























# AccidentalIslanding[0:5].to_csv('Accidental.csv',index=False)  # write into a csv file

# read from excel file --> datafile = pd.read_excel('file name', sheetname = '')
# write to excel file --> datafile.to_excel('file name', sheet_name = )

## reading from a website with pandas -->
# data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')  ## reading from html source
# print(data[0].head())  ### print head of the list





