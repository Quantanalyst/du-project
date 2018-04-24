##### The code for data analytics of tests performed to evaluate the microgrid master controller
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from AI import Accidental
from plotvoltage import PlotVoltage
from plotcurrent import PlotCurrent
from plotpower import PlotPower
from plotgeneration import PlotGeneration


# pltv = PlotVoltage('F',11)
# pltv.plotvoltage()

# pltc = PlotCurrent('PCL',1)
# pltc.plotcurrent()

# pltp = PlotPower('L',105)
# pltp.plotpower()

pltg = PlotGeneration()
pltg.plotbattery()




# read the info from HR info excel file
# infoloc = "C:\\Users\\Saeed Mohajeryami\\Dropbox\\DOE project\\Data from Dr\\BCM HIL PI Point List Draft 1 - 20161108.xlsx"
# measurement = pd.read_excel(infoloc,sheet_name='Measurement')
# status = pd.read_excel(infoloc,sheet_name='Status (feedback)')
# setpoint = pd.read_excel(infoloc,sheet_name='Setpoint')
# commands = pd.read_excel(infoloc,sheet_name='Commands')

# test = Accidental(OPC = 'Normal1',CBF11 = 'Open',CBF09 = 'Open',Tie= 'Open',Load ='Max',CHP ='On',PV ='Off',BESSs ='Off',Diesel ='Off',Contingency ="CBF09" )
# print(test.initialcondition())


# print(commands.head())
# Fileloc = 'C:\\Users\\Saeed Mohajeryami\\Dropbox\\DOE project\\tests\\3.1 AI-1.csv'
# AI1 = pd.read_csv(Fileloc)
#
# F_11_VrmsA = AI1['1'][1:]
# time = pd.DataFrame(np.arange(1,len(F_11_VrmsA)+1))

# print(type(time))

## plot
# fig = plt.figure()
# ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
# ax1.plot(time,F_11_VrmsA)
# ax1.set_ylim(bottom=50,top=110)
# plt.tight_layout()
# plt.show()
# print(type(AI1))


# # creating subplots with OO
# fig, axes=plt.subplots(nrows=1,ncols=2)   # subplot creates a list called axes
# axes[0].plot(x,y,'r')  # first element in the list of axes --> axes [0]
# axes[0].set_title('First Plot')
# axes[1].plot(y,x,'b')  # second element in the list of axes --> axes [1]
# axes[1].set_title('Second Plot')
#
# plt.tight_layout()
# plt.show()
#
# # How to save a figure ?
# fig.savefig('test.png',dpi=100)  # save file as png

#
# F_11_VrmsA = AI1['1'][1:]
# F_11_VangA = AI1['2'][1:]
# F_11_VrmsB = AI1['3'][1:]
# F_11_VangB = AI1['4'][1:]
# F_11_VrmsC = AI1['5'][1:]
# F_11_VangC = AI1['6'][1:]
# fig, axes=plt.subplots(nrows=2,ncols=3)
# # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")
#
# ## plot Phase A rms value
# axes[0,0].plot(time,F_11_VrmsA.apply(lambda x: int(x)/100))
# axes[0,0].set_xlim([0,300])
# axes[0,0].set_ylim([0.7,1.3])
# axes[0,0].set_xlabel('time(sec)')
# axes[0,0].set_ylabel('Phase A rms value')
#
# ## plot Phase A phase angle
# axes[1,0].plot(time,F_11_VangA.apply(lambda x: int(x)/100))
# axes[1,0].set_xlim([0,300])
# axes[1,0].set_xlabel('time(sec)')
# axes[1,0].set_ylabel('Phase A phase angle')
#
# ## plot Phase B rms value
# axes[0,1].plot(time,F_11_VrmsB.apply(lambda x: int(x)/100))
# axes[0,1].set_xlim([0,300])
# axes[0,1].set_ylim([0.7,1.3])
# axes[0,1].set_xlabel('time(sec)')
# axes[0,1].set_ylabel('Phase B rms value')
#
# ## plot Phase B phase angle
# axes[1,1].plot(time,F_11_VangB.apply(lambda x: int(x)/100))
# axes[1,1].set_xlim([0,300])
# axes[1,1].set_xlabel('time(sec)')
# axes[1,1].set_ylabel('Phase B phase angle')
#
# ## plot Phase C rms value
# axes[0,2].plot(time,F_11_VrmsC.apply(lambda x: int(x)/100))
# axes[0,2].set_xlim([0,300])
# axes[0,2].set_ylim([0.7,1.3])
# axes[0,2].set_xlabel('time(sec)')
# axes[0,2].set_ylabel('Phase C rms value')
#
# ## plot Phase C phase angle
# axes[1,2].plot(time,F_11_VangC.apply(lambda x: int(x)/100))
# axes[1,2].set_xlim([0,300])
# axes[1,2].set_xlabel('time(sec)')
# axes[1,2].set_ylabel('Phase C phase angle')
#
# plt.tight_layout()
# plt.show()
# fig.savefig("f_11_voltage.png")
#

















# AccidentalIslanding[0:5].to_csv('Accidental.csv',index=False)  # write into a csv file

# read from excel file --> datafile = pd.read_excel('file name', sheetname = '')
# write to excel file --> datafile.to_excel('file name', sheet_name = )

## reading from a website with pandas -->
# data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')  ## reading from html source
# print(data[0].head())  ### print head of the list





