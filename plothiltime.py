### plot HIL time


## import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class PlotHILTime():

    def plothiltime(self):
        # print(os.getcwd())
        os.chdir("..")
        os.chdir("..")
        path = os.getcwd()
        # print(path)
        # read the info from HR info excel file
        infoloc = path + "\\Data from Dr\\BCM HIL PI Point List Draft 1 - 20161108.xlsx"
        measurement = pd.read_excel(infoloc, sheet_name='Measurement')
        ### read AI1 data set
        Fileloc = path + '\\tests\\3.1 AI-1.csv'
        AI1 = pd.read_csv(Fileloc)

        ## creating a dataset of desired values to be plotted
        HILtime = AI1[str(756)][1:]
        time = pd.DataFrame(np.arange(1, len(HILtime) + 1))

        fig, axes = plt.subplots(nrows=1, ncols=1)  ## create a subplot
        # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")


        ## plot HIL time
        axes.plot(time, HILtime.apply(lambda x: int(x) / 1))
        axes.set_xlim([0, 300])
        #axes.set_ylim([59.5, 60.5])
        axes.set_xlabel('time(sec)')
        axes.set_ylabel('HIL time (sec)')

        plt.tight_layout()
        plt.show()