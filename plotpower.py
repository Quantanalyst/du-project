## make plotting power automatic

## import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class PlotPower():

    def __init__(self,device,number):
        self.device = device
        self.number = number

    def plotpower(self):

        ## check the device
        if (self.device == 'L'):
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

            devicelist = measurement['Measurement Name'].str.split('_', 2).tolist()  ## list of device names and numbers
            hrlist = measurement['HR Number']  ## list of HR numbers

            hr_list = []
            for val in np.arange(0, len(devicelist)):
                if str(devicelist[val]) == 'nan':
                    pass
                elif devicelist[val][0] == str(self.device) and devicelist[val][1] == str(
                        self.number):  # if it finds a match, it will append the hr_list
                    hr_list.append(hrlist[val])

            ## creating a dataset of desired values to be plotted
            PA = AI1[str(int(hr_list[0]))][1:]
            QA = AI1[str(int(hr_list[1]))][1:]
            PB = AI1[str(int(hr_list[2]))][1:]
            QB = AI1[str(int(hr_list[3]))][1:]
            PC = AI1[str(int(hr_list[4]))][1:]
            QC = AI1[str(int(hr_list[5]))][1:]
            time = pd.DataFrame(np.arange(1, len(PA) + 1))

            ############# plotting voltage  #############
            fig, axes = plt.subplots(nrows=2, ncols=3)  ## create a subplot
            # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

            ## plot Phase A rms value
            axes[0, 0].plot(time, PA.apply(lambda x: int(x) / 1))
            axes[0, 0].set_xlim([0, 300])
            #axes[0, 0].set_ylim([0.7, 1.3])
            axes[0, 0].set_xlabel('time(sec)')
            axes[0, 0].set_ylabel('Phase A kW')

            ## plot Phase A phase angle
            axes[1, 0].plot(time, QA.apply(lambda x: int(x) / 1))
            axes[1, 0].set_xlim([0, 300])
            axes[1, 0].set_xlabel('time(sec)')
            axes[1, 0].set_ylabel('Phase A kVAr')

            ## plot Phase B rms value
            axes[0, 1].plot(time, PB.apply(lambda x: int(x) / 1))
            axes[0, 1].set_xlim([0, 300])
            #axes[0, 1].set_ylim([0.7, 1.3])
            axes[0, 1].set_xlabel('time(sec)')
            axes[0, 1].set_ylabel('Phase B kW')

            ## plot Phase B phase angle
            axes[1, 1].plot(time, QB.apply(lambda x: int(x) / 1))
            axes[1, 1].set_xlim([0, 300])
            axes[1, 1].set_xlabel('time(sec)')
            axes[1, 1].set_ylabel('Phase B kVAr')

            ## plot Phase C rms value
            axes[0, 2].plot(time, PC.apply(lambda x: int(x) / 1))
            axes[0, 2].set_xlim([0, 300])
            #axes[0, 2].set_ylim([0.7, 1.3])
            axes[0, 2].set_xlabel('time(sec)')
            axes[0, 2].set_ylabel('Phase C kW')

            ## plot Phase C phase angle
            axes[1, 2].plot(time, QC.apply(lambda x: int(x) / 1))
            axes[1, 2].set_xlim([0, 300])
            axes[1, 2].set_xlabel('time(sec)')
            axes[1, 2].set_ylabel('Phase C kVAr')

            plt.tight_layout()
            plt.show()
            # fig.savefig("test.png")
        else:
            raise ValueError('There is not any power value for this device')   ## raise










