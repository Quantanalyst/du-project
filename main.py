##### The code for data analytics of tests performed to evaluate the microgrid master controller
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotfunction import PlotFunction
from changestatuscheck import ChangeStatusCheck
from systemcondition import SystemCondition

# # # step 1 : find transitions
# sys = SystemCondition()
# sys.systemconditionchange()
# sys.loadrestoration()
# print(list)
#


# #step 2 : plot transitions
# pltf = PlotFunction()
# pltf.plotfrequency()
# pltf.plotstatus(922)    # Anti-islanding
# pltf.plotstatus(923)    # fast load shedding
# pltf.plotstatus(924)    # Loss of voltage
# pltf.plotstatus(827)    # CB F11 status
# pltf.plotstatus(828)    # CB F09 status
# pltf.plotstatus(829)    # CB FIIT status
# pltf.plotstatus(826)    # PCT switch
# pltf.plotstatus(877)    # IF6 fault status
# pltf.plotstatus(866)    # Loads
# pltf.plotstatus(805)
# pltf.plotfeeder()

## step 3 : plot feeder POI voltage and current
# pltf = PlotFunction()
# pltf.plotvoltage('F','09')
# pltf.plotcurrent('CB','F09')
# pltf.plotvoltage('F','11')
# pltf.plotcurrent('CB','F11')
# pltf.plotcurrent('CB','FIIT')
# pltf.plotcurrent('PCT',1)
# pltf.plotcurrent('VISTA',33)
# pltf.plotcurrent('PCL',1)
# pltf.plotcurrent('PCL',2)
# pltf.plotcurrent('PCL',7)
# pltf.plotcurrent('PCL',8)
# pltf.plotcurrent('PCL',9)
# pltf.plotcurrent('VISTA',41)
#
# ## step 4 : plot generation resources
# pltf = PlotFunction()
# pltf.plotgen('CHP')
# pltf.plotgen('PV')
# pltf.plotgen('Battery')
# pltf.plotgen('Eng')

## step 5 : plot loads
pltf = PlotFunction()
pltf.plotloadagg()
pltf.plotgenagg()
# pltf.plotfrequency()
# pltf.plotpower('L',104)
# pltf.plotpower('L',105)
# pltf.plotpower('L',107)
# pltf.plotpower('L',110)
# pltf.plotpower('L',228)
# pltf.plotpower('L',225)
# pltf.plotpower('L',110)
# pltf.plotallgenloads()



# Fileloc = "C:\\Users\\Saeed Mohajeryami\\Dropbox\\DOE project\\tests\\PQ-10-PMU_B202.csv"
# testdata = pd.read_csv(Fileloc)
#
# f = testdata['PMU_B202:Frequency']
# time = pd.DataFrame(np.arange(1, len(f) + 1))
#
#
# fig, axes = plt.subplots(nrows=1, ncols=1)  ## create a subplot
# # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")
#
# # .apply(lambda x: int(x) / 1)
# ## plot frequency of Load 1
# axes.plot(time, f)
# axes.set_xlim([3300, 3800])
# axes.set_ylim([59.5, 61])
# axes.set_xlabel('cycle( 1/60 sec)')
# axes.set_ylabel('Frequency (Hz)')
#
# plt.show()

# pltf = PlotFunction()
# for val in [104,105,106,107,109,110,114,120,122,127,129,205,207,210,213,215,216,217,218,222,223,224,225,227,228,232,233,234,235]:
#     pltf.plotpower('L',val)
# pltf.plotloadagg()