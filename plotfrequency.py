### plot frequency


## import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class PlotFrequency():

    def plotfrequency(self):
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
        FL1 = AI1[str(749)][1:]
        FL3 = AI1[str(750)][1:]
        FL5 = AI1[str(751)][1:]
        FL7 = AI1[str(752)][1:]
        FL8 = AI1[str(753)][1:]
        FL11 = AI1[str(754)][1:]
        FL12 = AI1[str(755)][1:]
        time = pd.DataFrame(np.arange(1, len(FL1) + 1))

        ############# plotting voltage  #############
        fig, axes = plt.subplots(nrows=3, ncols=3)  ## create a subplot
        # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")


        ## plot frequency of Load 1
        axes[0, 0].plot(time, FL1.apply(lambda x: int(x) / 100))
        axes[0, 0].set_xlim([0, 300])
        axes[0, 0].set_ylim([57, 63.5])
        axes[0, 0].set_xlabel('time(sec)')
        axes[0, 0].set_ylabel('Frequency of Load 1 (Hz)')

        ## plot frequency of Load 3
        axes[0, 1].plot(time, FL3.apply(lambda x: int(x) / 100))
        axes[0, 1].set_xlim([0, 300])
        axes[0, 1].set_ylim([57, 63.5])
        axes[0, 1].set_xlabel('time(sec)')
        axes[0, 1].set_ylabel('Frequency of Load 3 (Hz)')

        ## plot frequency of Load 5
        axes[0, 2].plot(time, FL5.apply(lambda x: int(x) / 100))
        axes[0, 2].set_xlim([0, 300])
        axes[0, 2].set_ylim([57, 63.5])
        axes[0, 2].set_xlabel('time(sec)')
        axes[0, 2].set_ylabel('Frequency of Load 5 (Hz)')

        ## plot frequency of Load 7
        axes[1, 0].plot(time, FL7.apply(lambda x: int(x) / 100))
        axes[1, 0].set_xlim([0, 300])
        axes[1, 0].set_ylim([57, 63.5])
        axes[1, 0].set_xlabel('time(sec)')
        axes[1, 0].set_ylabel('Frequency of Load 7 (Hz)')

        ## plot frequency of Load 8
        axes[1, 1].plot(time, FL8.apply(lambda x: int(x) / 100))
        axes[1, 1].set_xlim([0, 300])
        axes[1, 1].set_ylim([57, 63.5])
        axes[1, 1].set_xlabel('time(sec)')
        axes[1, 1].set_ylabel('Frequency of Load 8 (Hz)')

        ## plot frequency of Load 11
        axes[1, 2].plot(time, FL11.apply(lambda x: int(x) / 100))
        axes[1, 2].set_xlim([0, 300])
        axes[1, 2].set_ylim([57, 63.5])
        axes[1, 2].set_xlabel('time(sec)')
        axes[1, 2].set_ylabel('Frequency of Load 11 (Hz)')

        ## plot frequency of Load 12
        axes[2, 0].plot(time, FL12.apply(lambda x: int(x) / 100))
        axes[2, 0].set_xlim([0, 300])
        axes[2, 0].set_ylim([57, 63.5])
        axes[2, 0].set_xlabel('time(sec)')
        axes[2, 0].set_ylabel('Frequency of Load 12 (Hz)')

        plt.tight_layout()
        plt.show()







