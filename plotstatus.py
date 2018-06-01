## make plotting status automatic

## import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class PlotStatus():

    #def __init__(self):
        #self.device = device
        #self.number = number

    def plotswitchstatus(self, device, number = 0):
        self.device = device
        self.number = number

        ## check the device
        if (self.device == 'VIS' or self.device == 'PCL' or self.device == 'PCT'):
            # print(os.getcwd())
            os.chdir("..")
            os.chdir("..")
            path = os.getcwd()
            # print(path)
            # read the info from HR info excel file
            infoloc = path + "\\Data from Dr\\BCM HIL PI Point List Draft 1 - 20161108.xlsx"
            #print(infoloc)
            status = pd.read_excel(infoloc, sheet_name='Status (feedback)')

            ### read AI1 data set
            Fileloc = path + '\\tests\\3.1 AI-1.csv'
            #print(Fileloc)
            AI1 = pd.read_csv(Fileloc)

            devicelist = status['Feedback/Status Name'].str.split('_', 2).tolist()  ## list of device names and numbers
            hrlist = status['HR Number']  ## list of HR numbers

            hr_list = []
            for val in np.arange(0, len(devicelist)):
                if str(devicelist[val]) == 'nan':
                    pass
                elif devicelist[val][0] == str(self.device) and devicelist[val][1] == str(
                        self.number):  # if it finds a match, it will append the hr_list
                    hr_list.append(hrlist[val])

            ## creating a dataset of desired values to be plotted
            Status = AI1[str(int(hr_list[0]))][1:]
            time = pd.DataFrame(np.arange(1, len(Status) + 1))

            ############# plotting voltage  #############
            fig, axes = plt.subplots(nrows=1, ncols=1)  ## create a subplot
            # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

            ## plot Switch Status
            axes.plot(time, Status.apply(lambda x: int(x) / 1))
            axes.set_xlim([0, 300])
            #axes.set_ylim([0.7, 1.3])
            axes.set_xlabel('time(sec)')
            axes.set_ylabel('Switch Status [0: open , 1: close]')

            plt.tight_layout()
            plt.show()
            # fig.savefig("test.png")
        else:
            raise ValueError('There is not any switch status for this device')   ## raise


    def plotcbstatus(self, connection):
        self.connection = connection

        ## check the device
        if (self.connection == 'F11' or self.connection == 'F9' or self.connection == 'IIT'):
            # print(os.getcwd())
            os.chdir("..")
            os.chdir("..")
            path = os.getcwd()
            # print(path)
            # read the info from HR info excel file
            infoloc = path + "\\Data from Dr\\BCM HIL PI Point List Draft 1 - 20161108.xlsx"
            #print(infoloc)
            status = pd.read_excel(infoloc, sheet_name='Status (feedback)')

            ### read AI1 data set
            Fileloc = path + '\\tests\\3.1 AI-1.csv'
            #print(Fileloc)
            AI1 = pd.read_csv(Fileloc)

            devicelist = status['Feedback/Status Name'].str.split('_', 2).tolist()  ## list of device names and numbers
            hrlist = status['HR Number']  ## list of HR numbers

            hr_list = []
            for val in np.arange(0, len(devicelist)):
                if str(devicelist[val]) == 'nan':
                    pass
                elif devicelist[val][1] == str(
                        self.connection):  # if it finds a match, it will append the hr_list
                    hr_list.append(hrlist[val])

            ## creating a dataset of desired values to be plotted
            Status = AI1[str(int(hr_list[0]))][1:]
            time = pd.DataFrame(np.arange(1, len(Status) + 1))

            ############# plotting voltage  #############
            fig, axes = plt.subplots(nrows=1, ncols=1)  ## create a subplot
            # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

            ## plot CB Status
            axes.plot(time, Status.apply(lambda x: int(x) / 1))
            axes.set_xlim([0, 300])
            #axes.set_ylim([0.7, 1.3])
            axes.set_xlabel('time(sec)')
            axes.set_ylabel('CB Status [0: open , 1: close]')

            plt.tight_layout()
            plt.show()
            # fig.savefig("test.png")
        else:
            raise ValueError('The connection is not valid')   ## raise


    def plotloadstatus(self, number):
        self.number = number

        ## check the device
        if (self.number == 104
            or self.number == 105
            or self.number == 106
            or self.number == 107
            or self.number == 108
            or self.number == 109
            or self.number == 110
            or self.number == 114
            or self.number == 120
            or self.number == 122
            or self.number == 127
            or self.number == 129
            or self.number == 205
            or self.number == 207
            or self.number == 210
            or self.number == 213
            or self.number == 215
            or self.number == 216
            or self.number == 217
            or self.number == 218
            or self.number == 222
            or self.number == 223
            or self.number == 224
            or self.number == 225
            or self.number == 227
            or self.number == 228
            or self.number == 232
            or self.number == 233
            or self.number == 234
            or self.number == 235
            ):
            # print(os.getcwd())
            os.chdir("..")
            os.chdir("..")
            path = os.getcwd()
            # print(path)
            # read the info from HR info excel file
            infoloc = path + "\\Data from Dr\\BCM HIL PI Point List Draft 1 - 20161108.xlsx"
            #print(infoloc)
            status = pd.read_excel(infoloc, sheet_name='Status (feedback)')

            ### read AI1 data set
            Fileloc = path + '\\tests\\3.1 AI-1.csv'
            #print(Fileloc)
            AI1 = pd.read_csv(Fileloc)

            devicelist = status['Feedback/Status Name'].str.split('_', 2).tolist()  ## list of device names and numbers
            hrlist = status['HR Number']  ## list of HR numbers

            hr_list = []
            for val in np.arange(0, len(devicelist)):
                if str(devicelist[val]) == 'nan':
                    pass
                elif devicelist[val][1] == str(self.number):  # if it finds a match, it will append the hr_list
                    hr_list.append(hrlist[val])

            ## creating a dataset of desired values to be plotted
            Status = AI1[str(int(hr_list[0]))][1:]
            time = pd.DataFrame(np.arange(1, len(Status) + 1))

            ############# plotting voltage  #############
            fig, axes = plt.subplots(nrows=1, ncols=1)  ## create a subplot
            # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

            ## plot Switch Status
            axes.plot(time, Status.apply(lambda x: int(x) / 1))
            axes.set_xlim([0, 300])
            #axes.set_ylim([0.7, 1.3])
            axes.set_xlabel('time(sec)')
            axes.set_ylabel('Switch Status [0: open , 1: close]')

            plt.tight_layout()
            plt.show()
            # fig.savefig("test.png")
        else:
            raise ValueError('There is not such load number in the dataset')   ## raise


    def plotgenerationstatus(self, device):
        self.device = device

        ## check the device
        if (self.device == 'CHP'
            or self.device == 'PV'
            or self.device == 'Eng'
            or self.device == 'Battery1'
            or self.device == 'Battery2'
            ):
            # print(os.getcwd())
            os.chdir("..")
            os.chdir("..")
            path = os.getcwd()
            # print(path)
            # read the info from HR info excel file
            infoloc = path + "\\Data from Dr\\BCM HIL PI Point List Draft 1 - 20161108.xlsx"
            #print(infoloc)
            status = pd.read_excel(infoloc, sheet_name='Status (feedback)')

            ### read AI1 data set
            Fileloc = path + '\\tests\\3.1 AI-1.csv'
            #print(Fileloc)
            AI1 = pd.read_csv(Fileloc)

            devicelist = status['Feedback/Status Name'].str.split('_', 2).tolist()  ## list of device names and numbers
            hrlist = status['HR Number']  ## list of HR numbers

            hr_list = []
            for val in np.arange(0, len(devicelist)):
                if str(devicelist[val]) == 'nan':
                    pass
                elif devicelist[val][0] == str(self.device):  # if it finds a match, it will append the hr_list
                    hr_list.append(hrlist[val])

            ## creating a dataset of desired values to be plotted
            Status = AI1[str(int(hr_list[0]))][1:]
            time = pd.DataFrame(np.arange(1, len(Status) + 1))

            ############# plotting voltage  #############
            fig, axes = plt.subplots(nrows=1, ncols=1)  ## create a subplot
            # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

            ## plot Resource's CB Status
            axes.plot(time, Status.apply(lambda x: int(x) / 1))
            axes.set_xlim([0, 300])
            #axes.set_ylim([0.7, 1.3])
            axes.set_xlabel('time(sec)')
            axes.set_ylabel('Resouce CB Status [0: open , 1: close]')

            plt.tight_layout()
            plt.show()
            # fig.savefig("test.png")
        else:
            raise ValueError('There is not such generation resource')   ## raise

    def plotoperatorcommandstatus(self, command):
        self.command = command

        ## check the device
        if (self.command == 'CB05_St'
            or self.command == 'LR1_St'
            or self.command == 'RL1CB_St'
            or self.command == 'RL3CB_St'
            or self.command == 'EF3_St'
            or self.command == 'EF1_St'
            or self.command == 'IF1_St'
            or self.command == 'IF2_St'
            or self.command == 'IF3_St'
            or self.command == 'IF4_St'
            or self.command == 'EF4_St'
            or self.command == 'EF2_St'
            or self.command == 'IF5_St'
            or self.command == 'IF6_St'
            or self.command == 'IF7_St'
            or self.command == 'CBdis_St'
            or self.command == 'TimeRst_St'
            or self.command == 'LR2_St'
            or self.command == 'RecPOI1_St'
            or self.command == 'RecPOI2_St'
            or self.command == 'RTD_St'
            or self.command == 'ConctIIT_St'
            or self.command == 'PI1_St'
            or self.command == 'PI2_St'
            or self.command == 'BlkStrt_St'
            or self.command == 'EDR_St'
            or self.command == 'LR1_Rdy'
            or self.command == 'LR2_Rdy'
            or self.command == 'Trf1to2_St'
            or self.command == 'Trf2to1_St'
            or self.command == 'Norm1_St'
            or self.command == 'Norm2_St'
            or self.command == 'PIF_St'
            or self.command == 'Clst1_St'
            or self.command == 'Clst2_St'
            or self.command == 'ClstFul_St'
            ):
            # print(os.getcwd())
            os.chdir("..")
            os.chdir("..")
            path = os.getcwd()
            # print(path)
            # read the info from HR info excel file
            infoloc = path + "\\Data from Dr\\BCM HIL PI Point List Draft 1 - 20161108.xlsx"
            # print(infoloc)
            status = pd.read_excel(infoloc, sheet_name='Status (feedback)')

            ### read AI1 data set
            Fileloc = path + '\\tests\\3.1 AI-1.csv'
            # print(Fileloc)
            AI1 = pd.read_csv(Fileloc)

            devicelist = status['Feedback/Status Name']
            hrlist = status['HR Number']  ## list of HR numbers

            hr_list = []
            for val in np.arange(0, len(devicelist)):
                if str(devicelist[val]) == 'nan':
                    pass
                elif devicelist[val] == str(self.command):  # if it finds a match, it will append the hr_list
                    hr_list.append(hrlist[val])

            ## creating a dataset of desired values to be plotted
            Status = AI1[str(int(hr_list[0]))][1:]
            time = pd.DataFrame(np.arange(1, len(Status) + 1))

            ############# plotting voltage  #############
            fig, axes = plt.subplots(nrows=1, ncols=1)  ## create a subplot
            # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

            ## plot Resource's CB Status
            axes.plot(time, Status.apply(lambda x: int(x) / 1))
            axes.set_xlim([0, 300])
            # axes.set_ylim([0.7, 1.3])
            axes.set_xlabel('time(sec)')
            axes.set_ylabel('Command Status [0: open/NA , 1: close/active]')

            plt.tight_layout()
            plt.show()
            # fig.savefig("test.png")
        else:
            raise ValueError('There is not such operator command')  ## raise



