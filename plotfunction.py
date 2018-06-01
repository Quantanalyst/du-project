## import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class PlotFunction():

    def __init__(self):
        self.testtype = input(" [PI]   :  Planned Islanding \n [AI]   :  Accidental Islanding \n [UPI]  :  Islanding-Abnormal V/F  \n"
                              " [RS]   :  Re-sync & Reconnect  \n [PQ]   :  Power Quality cases  \n [FLT]  :  Fault Test Cases  \n"
                              " [BD]   :  Basic Dispatch Test cases  \n [DAD]  :  Day-Ahead Dispatch  \n"
                              " [RTD]  :  Real-time Dispatch Test Cases  \n [ECDR] :  Economic Demand Response  \n"
                              " [EDR]  :  Reliable Operation (Emergency DR)  \n [LR]   :  Reliable Operation (LR)  \n"
                              " [CLUST]:  Microgrid Clustering  \n Enter Test Type: \n ")
        if (self.testtype == 'PI'):
            self.testnumber = input("test numbers : 1-2 \n Enter test number: \n")
        elif (self.testtype == 'AI'):
            self.testnumber = input("test numbers : 1-12 \n Enter test number: \n")
        elif (self.testtype == 'UPI'):
            self.testnumber = input("test numbers : 1-15 \n Enter test number: \n")
        elif (self.testtype == 'RS'):
            self.testnumber = input("test numbers : 1-12 \n Enter test number: \n")
        elif (self.testtype == 'PQ'):
            self.testnumber = input("test numbers : 1-26 \n Enter test number: \n")
        elif (self.testtype == 'FLT'):
            self.testnumber = input("test numbers : 1-145 \n Enter test number: \n")
        elif (self.testtype == 'BD'):
            self.testnumber = input("test numbers : 1-100 \n Enter test number: \n")
        elif (self.testtype == 'DAD'):
            self.testnumber = input("test numbers : 1-8 \n Enter test number: \n")
        elif (self.testtype == 'RTD'):
            self.testnumber = input("test numbers : 1-2 \n Enter test number: \n")
        elif (self.testtype == 'ECDR'):
            self.testnumber = input("test numbers : 1 \n Enter test number: \n")
        elif (self.testtype == 'EDR'):
            self.testnumber = input("test numbers : 1-2 \n Enter test number: \n")
        elif (self.testtype == 'LR'):
            self.testnumber = input("test numbers : 1-3 \n Enter test number: \n")
        elif (self.testtype == 'CLUST'):
            self.testnumber = input("test numbers : 1-2 \n Enter test number: \n")

        self.testnumber = int(self.testnumber)

        ## finding the directory path
        os.chdir("..")
        os.chdir("..")
        self.path = os.getcwd()

        ### read the info from HR info excel file
        self.infoloc = self.path + "\\Reports_Slides_Codes\\du-project\\PI Point List_v13.5.xlsm"
        print('HR number info location: {}'.format(self.infoloc))

        ### read test data set
        if (self.testtype == 'AI'):
            self.Fileloc = self.path + '\\tests\\3.' + str(self.testnumber) + ' AI-' + str(self.testnumber) + '.csv'
        elif (self.testtype == 'PI'):
            self.Fileloc = self.path + '\\tests\\2.' + str(self.testnumber - 1) + ' PI-' + str(self.testnumber) + '.csv'
        elif (self.testtype == 'UPI'):
            self.Fileloc = self.path + '\\tests\\4.' + str(self.testnumber - 1) + ' UPI-' + str(self.testnumber) + '.csv'
        elif (self.testtype == 'RS'):
            self.Fileloc = self.path + '\\tests\\5.' + str(self.testnumber - 1) + ' RS-' + str(self.testnumber) + '.csv'
        elif (self.testtype == 'PQ'):
            self.Fileloc = self.path + '\\tests\\6.' + str(self.testnumber - 1) + ' PQ-' + str(self.testnumber) + '.csv'
        elif (self.testtype == 'FLT'):
            self.Fileloc = self.path + '\\tests\\7.' + str(self.testnumber - 1) + ' FLT-' + str(self.testnumber) + '.csv'
        elif (self.testtype == 'BD'):
            self.Fileloc = self.path + '\\tests\\8.' + str(self.testnumber - 1) + ' BD-' + str(self.testnumber) + '.csv'
        elif (self.testtype == 'LR'):
            self.Fileloc = self.path + '\\tests\\9.' + str(self.testnumber - 1) + ' LR-' + str(self.testnumber) + '.csv'
        elif (self.testtype == 'RTD'):
            self.Fileloc = self.path + '\\tests\\11.' + str(self.testnumber - 1) + ' RTD-' + str(self.testnumber) + '.csv'
        elif (self.testtype == 'CLUST'):
            self.Fileloc = self.path + '\\tests\\14.' + str(self.testnumber - 1) + ' CLUST-' + str(self.testnumber) + '.csv'
        print('test data location: {}'.format(self.Fileloc))

########################################################################################################################
########################################################################################################################
#############################################      PLOT VOLTAGE      ###################################################
########################################################################################################################
########################################################################################################################

    def plotvoltage(self, device, number):
        self.device = device
        self.number = number
        ## check the device
        if (self.device == 'B' or self.device == 'F' or self.device == 'Synch'):

            # read the info from HR info excel file
            measurement = pd.read_excel(self.infoloc, sheet_name='PI Measurement')
            testdata = pd.read_csv(self.Fileloc)

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
            VrmsA = testdata[str(int(hr_list[0]))][1:]
            VangA = testdata[str(int(hr_list[1]))][1:]
            VrmsB = testdata[str(int(hr_list[2]))][1:]
            VangB = testdata[str(int(hr_list[3]))][1:]
            VrmsC = testdata[str(int(hr_list[4]))][1:]
            VangC = testdata[str(int(hr_list[5]))][1:]
            time = pd.DataFrame(np.arange(1, len(VrmsA) + 1))

            ############# plotting voltage  #############
            fig, axes = plt.subplots(nrows=2, ncols=3)  ## create a subplot
            # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

            ## plot Phase A rms value
            axes[0, 0].plot(time, VrmsA.apply(lambda x: int(x) / 100))
            axes[0, 0].set_xlim([0, len(time)])
            axes[0, 0].set_ylim([0.7, 1.3])
            axes[0, 0].set_xlabel('time(sec)')
            axes[0, 0].set_ylabel('Phase A pu value')

            ## plot Phase A phase angle
            axes[1, 0].plot(time, VangA.apply(lambda x: int(x) / 100))
            axes[1, 0].set_xlim([0, len(time)])
            axes[1, 0].set_xlabel('time(sec)')
            axes[1, 0].set_ylabel('Phase A phase angle')

            ## plot Phase B rms value
            axes[0, 1].plot(time, VrmsB.apply(lambda x: int(x) / 100))
            axes[0, 1].set_xlim([0, len(time)])
            axes[0, 1].set_ylim([0.7, 1.3])
            axes[0, 1].set_xlabel('time(sec)')
            axes[0, 1].set_ylabel('Phase B pu value')

            ## plot Phase B phase angle
            axes[1, 1].plot(time, VangB.apply(lambda x: int(x) / 100))
            axes[1, 1].set_xlim([0, len(time)])
            axes[1, 1].set_xlabel('time(sec)')
            axes[1, 1].set_ylabel('Phase B phase angle')

            ## plot Phase C rms value
            axes[0, 2].plot(time, VrmsC.apply(lambda x: int(x) / 100))
            axes[0, 2].set_xlim([0, len(time)])
            axes[0, 2].set_ylim([0.7, 1.3])
            axes[0, 2].set_xlabel('time(sec)')
            axes[0, 2].set_ylabel('Phase C pu value')

            ## plot Phase C phase angle
            axes[1, 2].plot(time, VangC.apply(lambda x: int(x) / 100))
            axes[1, 2].set_xlim([0, len(time)])
            axes[1, 2].set_xlabel('time(sec)')
            axes[1, 2].set_ylabel('Phase C phase angle')

            plt.tight_layout()
            plt.show()
            # fig.savefig("test.png")
        else:
            raise ValueError('There is not any voltage value for this device')   ## raise

########################################################################################################################
########################################################################################################################
#############################################      PLOT CURRENT      ###################################################
########################################################################################################################
########################################################################################################################

    def plotcurrent(self, device, number):
        self.device = device
        self.number = number

        ## check the device
        if (self.device == 'PCL' or self.device == 'PCT' or self.device == 'VISTA' or self.device == 'CB'):

            # read the info from HR info excel file
            measurement = pd.read_excel(self.infoloc, sheet_name='PI Measurement')
            testdata = pd.read_csv(self.Fileloc)

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
            IrmsA = testdata[str(int(hr_list[0]))][1:]
            IrmsB = testdata[str(int(hr_list[1]))][1:]
            IrmsC = testdata[str(int(hr_list[2]))][1:]
            time = pd.DataFrame(np.arange(1, len(IrmsA) + 1))

            ############# plotting voltage  #############
            fig, axes = plt.subplots(nrows=1, ncols=3)  ## create a subplot
            # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

            ## plot Phase A rms value
            axes[0].plot(time, IrmsA.apply(lambda x: int(x) / 100))
            axes[0].set_xlim([0, len(time)])
            axes[0].set_ylim([0, 1.1*max(IrmsA.apply(lambda x: int(x) / 100))])
            axes[0].set_xlabel('time(sec)')
            axes[0].set_ylabel('Phase A rms value')

            ## plot Phase B rms value
            axes[1].plot(time, IrmsB.apply(lambda x: int(x) / 100))
            axes[1].set_xlim([0, len(time)])
            axes[1].set_ylim([0, 1.1*max(IrmsB.apply(lambda x: int(x) / 100))])
            axes[1].set_xlabel('time(sec)')
            axes[1].set_ylabel('Phase B rms value')

            ## plot Phase C rms value
            axes[2].plot(time, IrmsC.apply(lambda x: int(x) / 100))
            axes[2].set_xlim([0, len(time)])
            axes[2].set_ylim([0, 1.1*max(IrmsC.apply(lambda x: int(x) / 100))])
            axes[2].set_xlabel('time(sec)')
            axes[2].set_ylabel('Phase C rms value')

            plt.tight_layout()
            plt.show()
            # fig.savefig("test.png")
        else:
            raise print('There is not any current value for this device')

########################################################################################################################
########################################################################################################################
#############################################      PLOT POWER      #####################################################
########################################################################################################################
########################################################################################################################

    def plotpower(self,device,number):
        self.device = device
        self.number = number

        ## check the device
        if (self.device == 'L'):

            # read the info from HR info excel file
            measurement = pd.read_excel(self.infoloc, sheet_name='PI Measurement')
            testdata = pd.read_csv(self.Fileloc)

            devicelist = measurement['Measurement Name'].str.split('_', 2).tolist()  ## list of device names and numbers
            hrlist = measurement['HR Number']  ## list of HR numbers

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
            PA = testdata[str(int(hr_list[0]))][1:]
            QA = testdata[str(int(hr_list[1]))][1:]
            PB = testdata[str(int(hr_list[2]))][1:]
            QB = testdata[str(int(hr_list[3]))][1:]
            PC = testdata[str(int(hr_list[4]))][1:]
            QC = testdata[str(int(hr_list[5]))][1:]
            time = pd.DataFrame(np.arange(1, len(PA) + 1))

            ############# plotting voltage  #############
            fig, axes = plt.subplots(nrows=2, ncols=3)  ## create a subplot
            # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

            ## plot Phase A rms value
            axes[0, 0].plot(time, PA.apply(lambda x: int(x) / 1))
            axes[0, 0].set_xlim([0, len(time)])
            #axes[0, 0].set_ylim([0.7, 1.3])
            axes[0, 0].set_xlabel('time(sec)')
            axes[0, 0].set_ylabel('Phase A kW')

            ## plot Phase A phase angle
            axes[1, 0].plot(time, QA.apply(lambda x: int(x) / 1))
            axes[1, 0].set_xlim([0, len(time)])
            axes[1, 0].set_xlabel('time(sec)')
            axes[1, 0].set_ylabel('Phase A kVAr')

            ## plot Phase B rms value
            axes[0, 1].plot(time, PB.apply(lambda x: int(x) / 1))
            axes[0, 1].set_xlim([0, len(time)])
            #axes[0, 1].set_ylim([0.7, 1.3])
            axes[0, 1].set_xlabel('time(sec)')
            axes[0, 1].set_ylabel('Phase B kW')

            ## plot Phase B phase angle
            axes[1, 1].plot(time, QB.apply(lambda x: int(x) / 1))
            axes[1, 1].set_xlim([0, len(time)])
            axes[1, 1].set_xlabel('time(sec)')
            axes[1, 1].set_ylabel('Phase B kVAr')

            ## plot Phase C rms value
            axes[0, 2].plot(time, PC.apply(lambda x: int(x) / 1))
            axes[0, 2].set_xlim([0, len(time)])
            #axes[0, 2].set_ylim([0.7, 1.3])
            axes[0, 2].set_xlabel('time(sec)')
            axes[0, 2].set_ylabel('Phase C kW')

            ## plot Phase C phase angle
            axes[1, 2].plot(time, QC.apply(lambda x: int(x) / 1))
            axes[1, 2].set_xlim([0, len(time)])
            axes[1, 2].set_xlabel('time(sec)')
            axes[1, 2].set_ylabel('Phase C kVAr')

            plt.tight_layout()
            plt.show()
            # fig.savefig("test.png")
        else:
            raise ValueError('There is not any power value for this device')   ## raise

########################################################################################################################
########################################################################################################################
#############################################      PLOT LOAD aggregated    #############################################
########################################################################################################################
########################################################################################################################

    def loadagg(self):
        measurement = pd.read_excel(self.infoloc, sheet_name='PI Measurement')
        testdata = pd.read_csv(self.Fileloc)
        Load1p = []
        Load1q = []
        for val in np.arange(0, len(list(testdata['556'][1:]))):
            ptemp = 0
            qtemp = 0
            for indp in np.arange(556, 622, 2):
                ptemp = ptemp + int(list(testdata[str(indp)][1:])[val])
            for indq in np.arange(557, 623, 2):
                qtemp = qtemp + int(list(testdata[str(indq)][1:])[val])
            Load1p.append(ptemp)
            Load1q.append(qtemp)

        Load2p = []
        Load2q = []
        for val in np.arange(0, len(list(testdata['556'][1:]))):
            ptemp = 0
            qtemp = 0
            for indp in np.arange(622, 730, 2):
                ptemp = ptemp + int(list(testdata[str(indp)][1:])[val])
            for indq in np.arange(623, 731, 2):
                qtemp = qtemp + int(list(testdata[str(indq)][1:])[val])
            Load2p.append(ptemp)
            Load2q.append(qtemp)
        return [Load1p, Load1q, Load2p, Load2q]

    def plotloadagg(self):
        Loads = self.loadagg()
        Load1p = Loads[0]
        Load1q = Loads[1]
        Load2p = Loads[2]
        Load2q = Loads[3]
        time = pd.DataFrame(np.arange(1, len(Load1p) + 1))

    ############# plotting loads  #############
        fig, axes = plt.subplots(nrows=2, ncols=2)  ## create a subplot
        # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

        ## plot Microgrid 1 active power [kW]
        axes[0, 0].plot(time, Load1p)
        axes[0, 0].set_xlim([0, len(time)])
        axes[0, 0].set_ylim([0, 1.1*max(Load1p)])
        # axes[0, 0].set_ylim([0, 4500])
        # axes[0, 0].set_ylim([0, 4000])
        axes[0, 0].set_xlabel('time(sec)')
        axes[0, 0].set_ylabel('Microgrid 1 Loads \n active power [kW] ')

        ## plot Microgrid 1 reactive power [kVAr]
        axes[1, 0].plot(time, Load1q)
        axes[1, 0].set_xlim([0, len(time)])
        axes[1, 0].set_ylim([0, 1.1*max(Load1q)])
        axes[1, 0].set_xlabel('time(sec)')
        axes[1, 0].set_ylabel('Microgrid 1 Loads \n reactive power [kVAr] ')

        ## plot Microgrid 2 active power [kW]
        axes[0, 1].plot(time, Load2p)
        axes[0, 1].set_xlim([0, len(time)])
        axes[0, 1].set_ylim([0, 1.1*max(Load2p)])
        # axes[0, 1].set_ylim([0, 4500])
        axes[0, 1].set_xlabel('time(sec)')
        axes[0, 1].set_ylabel('Microgrid 2 Loads \n active power [kW] ')

        ## plot Microgrid 2 reactive power [kVAr]
        axes[1, 1].plot(time, Load2q)
        axes[1, 1].set_xlim([0, len(time)])
        axes[1, 1].set_ylim([0, 1.1*max(Load2q)])
        axes[1, 1].set_xlabel('time(sec)')
        axes[1, 1].set_ylabel('Microgrid 2 Loads \n reactive power [kVAr] ')

        plt.tight_layout()
        plt.show()


########################################################################################################################
########################################################################################################################
#############################################      PLOT GEN aggregated    ##############################################
########################################################################################################################
########################################################################################################################

    def genagg(self):
        measurement = pd.read_excel(self.infoloc, sheet_name='PI Measurement')
        testdata = pd.read_csv(self.Fileloc)

        gen1p = []
        gen1q = []
        for val in np.arange(0, len(list(testdata['556'][1:]))):
            ptemp = 0
            qtemp = 0
            for indp in [730, 734, 741, 745]:
                ptemp = ptemp + int(list(testdata[str(indp)][1:])[val])
            for indq in [731, 735, 742, 746]:
                qtemp = qtemp + int(list(testdata[str(indq)][1:])[val])
            gen1p.append(ptemp)
            gen1q.append(qtemp)

        gen2p = []
        gen2q = []
        for val in np.arange(0, len(list(testdata['556'][1:]))):
            ptemp = 0
            qtemp = 0
            for indp in [737]:
                ptemp = ptemp + int(list(testdata[str(indp)][1:])[val])
            for indq in [738]:
                qtemp = qtemp + int(list(testdata[str(indq)][1:])[val])
            gen2p.append(ptemp)
            gen2q.append(qtemp)
        return [gen1p, gen1q, gen2p, gen2q]

    def plotgenagg(self):
        Gens = self.genagg()
        gen1p = Gens[0]
        gen1q = Gens[1]
        gen2p = Gens[2]
        gen2q = Gens[3]
        time = pd.DataFrame(np.arange(1, len(gen1p) + 1))

    ############# plotting generation  #############
        fig, axes = plt.subplots(nrows=2, ncols=2)  ## create a subplot
        # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

        ## plot Microgrid 1 active power [kW]
        axes[0, 0].plot(time, gen1p)
        axes[0, 0].set_xlim([0, len(time)])
        if (max(gen1p) > 0 and min(gen1p) > 0):
            axes[0, 0].set_ylim([0, 1.1 * max(gen1p)])
        elif (max(gen1p) > 0 and min(gen1p) < 0):
            axes[0, 0].set_ylim([1.1 * min(gen1p), 1.1 * max(gen1p)])
        elif (max(gen1p) < 0):
            axes[0, 0].set_ylim([1.1 * min(gen1p), 0])
        axes[0, 0].set_xlabel('time(sec)')
        axes[0, 0].set_ylabel('Microgrid 1 Generation \n active power [kW] ')

        ## plot Microgrid 1 reactive power [kVAr]
        axes[1, 0].plot(time, gen1q)
        axes[1, 0].set_xlim([0, len(time)])
        if (max(gen1q) > 0 and min(gen1q) > 0):
            axes[1, 0].set_ylim([0, 1.1 * max(gen1q)])
        elif (max(gen1q) > 0 and min(gen1q) < 0):
            axes[1, 0].set_ylim([1.1 * min(gen1q), 1.1 * max(gen1q)])
        elif (max(gen1q) < 0):
            axes[1, 0].set_ylim([1.1 * min(gen1q), 0])
        # axes[1, 0].set_ylim([1.1*min(gen1q), 1.1*max(gen1q)])
        axes[1, 0].set_xlabel('time(sec)')
        axes[1, 0].set_ylabel('Microgrid 1 Generation \n reactive power [kVAr] ')

        ## plot Microgrid 2 active power [kW]
        axes[0, 1].plot(time, gen2p)
        axes[0, 1].set_xlim([0, len(time)])
        if (max(gen2p) > 0 and min(gen2p) > 0):
            axes[0, 1].set_ylim([0, 1.1 * max(gen2p)])
        elif (max(gen2p) > 0 and min(gen2p) < 0):
            axes[0, 1].set_ylim([1.1 * min(gen2p), 1.1 * max(gen2p)])
        elif (max(gen2p) < 0):
            axes[0, 1].set_ylim([1.1 * min(gen2p), 0])
        axes[0, 1].set_xlabel('time(sec)')
        axes[0, 1].set_ylabel('Microgrid 2 Generation \n active power [kW] ')

        ## plot Microgrid 2 reactive power [kVAr]
        axes[1, 1].plot(time, gen2q)
        axes[1, 1].set_xlim([0, len(time)])
        if (max(gen2q) > 0 and min(gen2q) > 0):
            axes[1, 1].set_ylim([0, 1.1 * max(gen2q)])
        elif (max(gen2q) > 0 and min(gen2q) < 0):
            axes[1, 1].set_ylim([1.1 * min(gen2q), 1.1 * max(gen2q)])
        elif (max(gen2q) < 0):
            axes[1, 1].set_ylim([1.1 * min(gen2q), 0])
        axes[1, 1].set_xlabel('time(sec)')
        axes[1, 1].set_ylabel('Microgrid 2 Generation \n reactive power [kVAr] ')

        plt.tight_layout()
        plt.show()


########################################################################################################################
########################################################################################################################
########################################    PLOT TOT AGGREGATED    #####################################################
########################################################################################################################
########################################################################################################################

    def plotallgenloads(self):

        Loads = self.loadagg()
        Load1p = Loads[0]
        Load1q = Loads[1]
        Load2p = Loads[2]
        Load2q = Loads[3]

        Gens = self.genagg()
        gen1p = Gens[0]
        gen1q = Gens[1]
        gen2p = Gens[2]
        gen2q = Gens[3]
        AllLoadp = [x + y for x, y in zip(Load1p, Load2p)]
        AllLoadq = [x + y for x, y in zip(Load1q, Load2q)]
        AllGenp = [x + y for x, y in zip(gen1p, gen2p)]
        AllGenq = [x + y for x, y in zip(gen1q, gen2q)]
        time = pd.DataFrame(np.arange(1, len(AllLoadp) + 1))

        ############# plotting all loads and gens  #############
        fig, axes = plt.subplots(nrows=2, ncols=2)  ## create a subplot
        # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

        ## plot Microgrid 1 active power [kW]
        axes[0, 0].plot(time, AllGenp)
        axes[0, 0].set_xlim([0, len(time)])
        axes[0, 0].set_ylim([0, 1.1*max(AllGenp)])
        # axes[0, 0].set_ylim([0, 5500])
        axes[0, 0].set_xlabel('time(sec)')
        axes[0, 0].set_ylabel('System Generation \n active power [kW] ')

        ## plot Microgrid 1 reactive power [kVAr]
        axes[1, 0].plot(time, AllGenq)
        axes[1, 0].set_xlim([0, len(time)])
        axes[1, 0].set_ylim([0, 1.1*max(AllGenq)])
        axes[1, 0].set_xlabel('time(sec)')
        axes[1, 0].set_ylabel('System Generation \n reactive power [kVAr] ')

        ## plot Microgrid 2 active power [kW]
        axes[0, 1].plot(time, AllLoadp)
        axes[0, 1].set_xlim([0, len(time)])
        axes[0, 1].set_ylim([0, 1.1*max(AllLoadp)])
        # axes[0, 1].set_ylim([0, 4500])
        axes[0, 1].set_xlabel('time(sec)')
        axes[0, 1].set_ylabel('System Load \n active power [kW] ')

        ## plot Microgrid 2 reactive power [kVAr]
        axes[1, 1].plot(time, AllLoadq)
        axes[1, 1].set_xlim([0, len(time)])
        axes[1, 1].set_ylim([0, 1.1*max(AllLoadq)])
        axes[1, 1].set_xlabel('time(sec)')
        axes[1, 1].set_ylabel('System Load \n reactive power [kVAr] ')

        plt.tight_layout()
        plt.show()

########################################################################################################################
########################################################################################################################
########################################      PLOT FEEDER power    #####################################################
########################################################################################################################
########################################################################################################################

    def plotfeeder(self):
        testdata = pd.read_csv(self.Fileloc)

        F11phdata = testdata['541'][1:]
        F11phcurrent = [int(x) / 100 for x in F11phdata]
        F11power = [np.sqrt(3) * x * 12470 for x in F11phcurrent]

        F09phdata = testdata['544'][1:]
        F09phcurrent = [int(x) / 100 for x in F09phdata]
        F09power = [np.sqrt(3) * x * 12470 for x in F09phcurrent]

        FIITphdata = testdata['553'][1:]
        FIITphcurrent = [int(x) / 100 for x in FIITphdata]
        FIITpower = [np.sqrt(3) * x * 12470 for x in FIITphcurrent]

        time = pd.DataFrame(np.arange(1, len(F11power) + 1))

        ############# plotting all loads and gens  #############
        fig, axes = plt.subplots(nrows=3, ncols=1)  ## create a subplot
        # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

        ## plot Substation feeder 1 apparant power [kW]
        axes[0].plot(time, F11power)
        axes[0].set_xlim([0, len(time)])
        axes[0].set_yticks([0,500000,1000000,1500000,2000000,2500000,3000000,3500000,4000000,4500000,5000000,5500000,6000000,6500000,7000000])
        axes[0].set_yticklabels(['0','0.5','1','1.5','2','2.5','3','3.5','4','4.5','5','5.5','6','6.5','7'])
        axes[0].set_ylim([0, 1.1*max(F11power)])
        axes[0].set_xlabel('time(sec)')
        axes[0].set_ylabel('Substation feeder 1 \napparant power [MVA] ')

        ## plot Substation feeder 2 apparant power [kW]
        axes[1].plot(time, F09power)
        axes[1].set_xlim([0, len(time)])
        axes[1].set_yticks([0,500000,1000000,1500000,2000000,2500000,3000000,3500000,4000000,4500000,5000000,5500000,6000000,6500000,7000000])
        axes[1].set_yticklabels(['0','0.5','1','1.5','2','2.5','3','3.5','4','4.5','5','5.5','6','6.5','7'])
        axes[1].set_ylim([0, 1.1*max(F09power)])
        axes[1].set_xlabel('time(sec)')
        axes[1].set_ylabel('Substation feeder 2 \napparant power [VA] ')

        ## plot IIT Substation feeder apparant power [kW]
        axes[2].plot(time, FIITpower)
        axes[2].set_xlim([0, len(time)])
        axes[2].set_yticks([0,500000,1000000,1500000,2000000,2500000,3000000,3500000,4000000,4500000,5000000,5500000,6000000,6500000,7000000])
        axes[2].set_yticklabels(['0','0.5','1','1.5','2','2.5','3','3.5','4','4.5','5','5.5','6','6.5','7'])
        axes[2].set_ylim([0, 1.1*max(FIITpower)])
        axes[2].set_xlabel('time(sec)')
        axes[2].set_ylabel('IIT Substation feeder \napparant power [VA] ')

        plt.tight_layout()
        plt.show()


########################################################################################################################
########################################################################################################################
########################################      PLOT GENERATION      #####################################################
########################################################################################################################
########################################################################################################################

    def plotgen(self,device,number = 0):
        self.device = device
        self.number = number
        testdata = pd.read_csv(self.Fileloc)
        if (self.device == 'CHP'):
            ## creating a dataset of desired values to be plotted
            CHPP = testdata[str(730)][1:]
            CHPQ = testdata[str(731)][1:]
            CHPS = testdata[str(732)][1:]
            CHPF = testdata[str(733)][1:]
            time = pd.DataFrame(np.arange(1, len(CHPP) + 1))

            ############# plotting power  #############
            fig, axes = plt.subplots(nrows=1, ncols=2)  ## create a subplot
            # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

            ## plot CHP kW
            axes[0].plot(time, CHPP.apply(lambda x: int(x) / 1))
            axes[0].set_xlim([0, len(time)])
            axes[0].set_ylim([0, 1.1*max(CHPP.apply(lambda x: int(x) / 1))])
            axes[0].set_xlabel('time(sec)')
            axes[0].set_ylabel('CHP active power (kW)')

            ## plot CHP kVAr
            axes[1].plot(time, CHPQ.apply(lambda x: int(x) / 1))
            axes[1].set_xlim([0, len(time)])
            if (max(CHPQ.apply(lambda x: int(x) / 1)) > 0 and min(CHPQ.apply(lambda x: int(x) / 1)) > 0):
                axes[1].set_ylim([0, 1.1*max(CHPQ.apply(lambda x: int(x) / 1))])
            elif (max(CHPQ.apply(lambda x: int(x) / 1)) > 0 and min(CHPQ.apply(lambda x: int(x) / 1)) < 0):
                axes[1].set_ylim([1.1 * min(CHPQ.apply(lambda x: int(x) / 1)), 1.1 * max(CHPQ.apply(lambda x: int(x) / 1))])
            elif (max(CHPQ.apply(lambda x: int(x) / 1)) < 0):
                axes[1].set_ylim([1.1 * min(CHPQ.apply(lambda x: int(x) / 1)), 0])
            axes[1].set_xlabel('time(sec)')
            axes[1].set_ylabel('CHP reactive power (kVAr)')

            ## plot CHP Speed
            # axes[1, 0].plot(time, CHPS.apply(lambda x: int(x) / 100))
            # axes[1, 0].set_xlim([0, len(time)])
            # #axes[0, 1].set_ylim([0.7, 1.3])
            # axes[1, 0].set_xlabel('time(sec)')
            # axes[1, 0].set_ylabel('CHP speed (rad/sec)')

            ## plot CHP fuel
            # axes[1, 1].plot(time, CHPF.apply(lambda x: int(x) / 100))
            # axes[1, 1].set_xlim([0, len(time)])
            # axes[1, 1].set_xlabel('time(sec)')
            # axes[1, 1].set_ylabel('CHP fuel (f^3)')

            plt.tight_layout()
            plt.show()
            # fig.savefig("test.png")
        elif (self.device == 'PV'):
            PVP = testdata[str(734)][1:]
            PVQ = testdata[str(735)][1:]
            PVIr = testdata[str(736)][1:]
            time = pd.DataFrame(np.arange(1, len(PVP) + 1))

            ############# plotting voltage  #############
            fig, axes = plt.subplots(nrows=1, ncols=2)  ## create a subplot
            # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

            ## plot PV kW
            axes[0].plot(time, PVP.apply(lambda x: int(x) / 1))
            axes[0].set_xlim([0, len(time)])
            axes[0].set_ylim([0, 1.1*max(PVP.apply(lambda x: int(x) / 1))])
            axes[0].set_xlabel('time(sec)')
            axes[0].set_ylabel('PV active power (kW)')

            ## plot PV kVAr
            axes[1].plot(time, PVQ.apply(lambda x: int(x) / 1))
            axes[1].set_xlim([0, len(time)])
            axes[1].set_ylim([0, 1.1*max(PVQ.apply(lambda x: int(x) / 1))])
            axes[1].set_xlabel('time(sec)')
            axes[1].set_ylabel('PV reactive power (kVAr)')

            ## plot PV Irradiation
            # axes[2].plot(time, PVIr.apply(lambda x: int(x) / 100))
            # axes[2].set_xlim([0, len(time)])
            # # axes[0, 1].set_ylim([0.7, 1.3])
            # axes[2].set_xlabel('time(sec)')
            # axes[2].set_ylabel('PV Irradiation (%)')

            plt.tight_layout()
            plt.show()
            # fig.savefig("test.png")
        elif (self.device == 'Eng' or self.device == 'Diesel'):
            ENGP = testdata[str(737)][1:]
            ENGQ = testdata[str(738)][1:]
            ENGS = testdata[str(739)][1:]
            ENGF = testdata[str(740)][1:]
            time = pd.DataFrame(np.arange(1, len(ENGP) + 1))

            ############# plotting voltage  #############
            fig, axes = plt.subplots(nrows=2, ncols=2)  ## create a subplot
            # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

            ## plot Diesel kW
            axes[0, 0].plot(time, ENGP.apply(lambda x: int(x) / 1))
            axes[0, 0].set_xlim([0, len(time)])
            if (max(ENGP.apply(lambda x: int(x) / 1)) > 0 and min(ENGP.apply(lambda x: int(x) / 1)) > 0):
                axes[0, 0].set_ylim([0, 1.1*max(ENGP.apply(lambda x: int(x) / 1))])
            elif (max(ENGP.apply(lambda x: int(x) / 1)) > 0 and min(ENGP.apply(lambda x: int(x) / 1)) < 0):
                axes[0, 0].set_ylim([1.1 * min(ENGP.apply(lambda x: int(x) / 1)), 1.1 * max(ENGP.apply(lambda x: int(x) / 1))])
            elif (max(ENGP.apply(lambda x: int(x) / 1)) < 0):
                axes[0, 0].set_ylim([1.1 * min(ENGP.apply(lambda x: int(x) / 1)), 0])
            # axes[0, 0].set_ylim([0, 1.1*max(ENGP.apply(lambda x: int(x) / 1))])
            axes[0, 0].set_xlabel('time(sec)')
            axes[0, 0].set_ylabel('Diesel active power (kW)')

            ## plot Diesel kVAr
            axes[0, 1].plot(time, ENGQ.apply(lambda x: int(x) / 1))
            axes[0, 1].set_xlim([0, len(time)])
            if (max(ENGQ.apply(lambda x: int(x) / 1)) > 0 and min(ENGQ.apply(lambda x: int(x) / 1)) > 0):
                axes[0, 1].set_ylim([0, 1.1*max(ENGQ.apply(lambda x: int(x) / 1))])
            elif (max(ENGQ.apply(lambda x: int(x) / 1)) > 0 and min(ENGQ.apply(lambda x: int(x) / 1)) < 0):
                axes[0, 1].set_ylim([1.1 * min(ENGQ.apply(lambda x: int(x) / 1)), 1.1 * max(ENGQ.apply(lambda x: int(x) / 1))])
            elif (max(ENGQ.apply(lambda x: int(x) / 1)) < 0):
                axes[0, 1].set_ylim([1.1 * min(ENGQ.apply(lambda x: int(x) / 1)), 0])
            # axes[0, 1].set_ylim([0, 1.1*max(ENGQ.apply(lambda x: int(x) / 1))])
            axes[0, 1].set_xlabel('time(sec)')
            axes[0, 1].set_ylabel('Diesel reactive power (kVAr)')

            ## plot Diesel Speed
            # axes[1, 0].plot(time, ENGS.apply(lambda x: int(x) / 100))
            # axes[1, 0].set_xlim([0, len(time)])
            # # axes[0, 1].set_ylim([0.7, 1.3])
            # axes[1, 0].set_xlabel('time(sec)')
            # axes[1, 0].set_ylabel('Diesel speed (rad/sec)')

            ## plot Diesel fuel
            # axes[1, 1].plot(time, ENGF.apply(lambda x: int(x) / 100))
            # axes[1, 1].set_xlim([0, len(time)])
            # axes[1, 1].set_xlabel('time(sec)')
            # axes[1, 1].set_ylabel('Diesel fuel (f^3)')

            plt.tight_layout()
            plt.show()
            # fig.savefig("test.png")
        elif (self.device == 'Battery'):
            ## creating a dataset of desired values to be plotted
            BAT1P = testdata[str(741)][1:]
            BAT1Q = testdata[str(742)][1:]
            BAT1SOC = testdata[str(743)][1:]
            BAT1F = testdata[str(744)][1:]
            BAT2P = testdata[str(745)][1:]
            BAT2Q = testdata[str(746)][1:]
            BAT2SOC = testdata[str(747)][1:]
            BAT2F = testdata[str(748)][1:]
            time = pd.DataFrame(np.arange(1, len(BAT1P) + 1))

            ############# plotting voltage  #############
            fig, axes = plt.subplots(nrows=2, ncols=2)  ## create a subplot
            # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

            ## plot Battery 1 kW
            axes[0, 0].plot(time, BAT1P.apply(lambda x: int(x) / 1))
            axes[0, 0].set_xlim([0, len(time)])
            if (max(BAT1P.apply(lambda x: int(x) / 1)) > 0 and min(BAT1P.apply(lambda x: int(x) / 1)) > 0):
                axes[0, 0].set_ylim([0, 1.1*max(BAT1P.apply(lambda x: int(x) / 1))])
            elif (max(BAT1P.apply(lambda x: int(x) / 1)) > 0 and min(BAT1P.apply(lambda x: int(x) / 1)) < 0):
                axes[0, 0].set_ylim([1.1 * min(BAT1P.apply(lambda x: int(x) / 1)), 1.1 * max(BAT1P.apply(lambda x: int(x) / 1))])
            elif (max(BAT1P.apply(lambda x: int(x) / 1)) < 0):
                axes[0, 0].set_ylim([1.1 * min(BAT1P.apply(lambda x: int(x) / 1)), 0])
            # axes[0, 0].set_ylim([0, 1.1*max(BAT1P.apply(lambda x: int(x) / 1))])
            axes[0, 0].set_xlabel('time(sec)')
            axes[0, 0].set_ylabel('Battery 1 active power (kW)')

            ## plot Battery 1 kVAr
            axes[0, 1].plot(time, BAT1Q.apply(lambda x: int(x) / 1))
            axes[0, 1].set_xlim([0, len(time)])
            if (max(BAT1Q.apply(lambda x: int(x) / 1)) > 0 and min(BAT1Q.apply(lambda x: int(x) / 1)) > 0):
                axes[0, 1].set_ylim([0, 1.1*max(BAT1Q.apply(lambda x: int(x) / 1))])
            elif (max(BAT1Q.apply(lambda x: int(x) / 1)) > 0 and min(BAT1Q.apply(lambda x: int(x) / 1)) < 0):
                axes[0, 1].set_ylim([1.1 * min(BAT1Q.apply(lambda x: int(x) / 1)), 1.1 * max(BAT1Q.apply(lambda x: int(x) / 1))])
            elif (max(BAT1Q.apply(lambda x: int(x) / 1)) < 0):
                axes[0, 1].set_ylim([1.1 * min(BAT1Q.apply(lambda x: int(x) / 1)), 0])
            # axes[0, 1].set_ylim([0, 1.1*max(BAT1Q.apply(lambda x: int(x) / 1))])
            axes[0, 1].set_xlabel('time(sec)')
            axes[0, 1].set_ylabel('Battery 1 reactive power (kVAr)')

            # # plot Battery 1 SOC
            # axes[1, 0].plot(time, BAT1SOC.apply(lambda x: int(x) / 100))
            # axes[1, 0].set_xlim([0, len(time)])
            # # axes[0, 1].set_ylim([0.7, 1.3])
            # axes[1, 0].set_xlabel('time(sec)')
            # axes[1, 0].set_ylabel('Battery 1 SOC (%)')

            ## plot Battery 1 frequency
            # axes[1, 1].plot(time, BAT1F.apply(lambda x: int(x) / 100))
            # axes[1, 1].set_xlim([0, len(time)])
            # axes[1, 1].set_ylim([59.5, 60.5])
            # axes[1, 1].set_xlabel('time(sec)')
            # axes[1, 1].set_ylabel('Battery 1 frequency (Hz)')

            ## plot Battery 2 kW
            axes[1, 0].plot(time, BAT2P.apply(lambda x: int(x) / 1))
            axes[1, 0].set_xlim([0, len(time)])
            if (max(BAT2P.apply(lambda x: int(x) / 1)) > 0 and min(BAT2P.apply(lambda x: int(x) / 1)) > 0):
                axes[1, 0].set_ylim([0, 1.1*max(BAT2P.apply(lambda x: int(x) / 1))])
            elif (max(BAT2P.apply(lambda x: int(x) / 1)) > 0 and min(BAT2P.apply(lambda x: int(x) / 1)) < 0):
                axes[1, 0].set_ylim([1.1 * min(BAT2P.apply(lambda x: int(x) / 1)), 1.1 * max(BAT2P.apply(lambda x: int(x) / 1))])
            elif (max(BAT2P.apply(lambda x: int(x) / 1)) < 0):
                axes[1, 0].set_ylim([1.1 * min(BAT2P.apply(lambda x: int(x) / 1)), 0])
            # axes[0, 2].set_ylim([0, 1.1*max(BAT2P.apply(lambda x: int(x) / 1))])
            axes[1, 0].set_xlabel('time(sec)')
            axes[1, 0].set_ylabel('Battery 2 active power (kW)')

            ## plot Battery 2 kVAr
            axes[1, 1].plot(time, BAT2Q.apply(lambda x: int(x) / 1))
            axes[1, 1].set_xlim([0, len(time)])
            if (max(BAT2Q.apply(lambda x: int(x) / 1)) > 0 and min(BAT2Q.apply(lambda x: int(x) / 1)) > 0):
                axes[1, 1].set_ylim([0, 1.1*max(BAT2Q.apply(lambda x: int(x) / 1))])
            elif (max(BAT2Q.apply(lambda x: int(x) / 1)) > 0 and min(BAT2Q.apply(lambda x: int(x) / 1)) < 0):
                axes[1, 1].set_ylim([1.1 * min(BAT2Q.apply(lambda x: int(x) / 1)), 1.1 * max(BAT2Q.apply(lambda x: int(x) / 1))])
            elif (max(BAT2Q.apply(lambda x: int(x) / 1)) < 0):
                axes[1, 1].set_ylim([1.1 * min(BAT2Q.apply(lambda x: int(x) / 1)), 0])
            # axes[0, 3].set_ylim([0, 1.1*max(BAT2Q.apply(lambda x: int(x) / 1))])
            axes[1, 1].set_xlabel('time(sec)')
            axes[1, 1].set_ylabel('Battery 2 reactive power (kVAr)')

            ## plot Battery 2 SOC
            # axes[1, 1].plot(time, BAT2SOC.apply(lambda x: int(x) / 100))
            # axes[1, 1].set_xlim([0, len(time)])
            # # axes[0, 1].set_ylim([0.7, 1.3])
            # axes[1, 1].set_xlabel('time(sec)')
            # axes[1, 1].set_ylabel('Battery 2 SOC (%)')

            ## plot Battery 2 frequency
            # axes[1, 3].plot(time, BAT2F.apply(lambda x: int(x) / 100))
            # axes[1, 3].set_xlim([0, len(time)])
            # axes[1, 3].set_ylim([59.5, 60.5])
            # axes[1, 3].set_xlabel('time(sec)')
            # axes[1, 3].set_ylabel('Battery 2 frequency (Hz)')
            plt.tight_layout()
            ############# plotting voltage  #############
            fig, axes = plt.subplots(nrows=2, ncols=2)  ## create a subplot
            # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

            ## plot Battery 1 kW
            axes[0, 0].plot(time, BAT1P.apply(lambda x: int(x) / 1))
            axes[0, 0].set_xlim([0, len(time)])
            if (max(BAT1P.apply(lambda x: int(x) / 1)) > 0 and min(BAT1P.apply(lambda x: int(x) / 1)) > 0):
                axes[0, 0].set_ylim([0, 1.1 * max(BAT1P.apply(lambda x: int(x) / 1))])
            elif (max(BAT1P.apply(lambda x: int(x) / 1)) > 0 and min(BAT1P.apply(lambda x: int(x) / 1)) < 0):
                axes[0, 0].set_ylim(
                    [1.1 * min(BAT1P.apply(lambda x: int(x) / 1)), 1.1 * max(BAT1P.apply(lambda x: int(x) / 1))])
            elif (max(BAT1P.apply(lambda x: int(x) / 1)) < 0):
                axes[0, 0].set_ylim([1.1 * min(BAT1P.apply(lambda x: int(x) / 1)), 0])
            # axes[0, 0].set_ylim([0, 1.1*max(BAT1P.apply(lambda x: int(x) / 1))])
            axes[0, 0].set_xlabel('time(sec)')
            axes[0, 0].set_ylabel('Battery 1 active power (kW)')

            ## plot Battery 1 kVAr
            # axes[0, 1].plot(time, BAT1Q.apply(lambda x: int(x) / 1))
            # axes[0, 1].set_xlim([0, len(time)])
            # if (max(BAT1Q.apply(lambda x: int(x) / 1)) > 0 and min(BAT1Q.apply(lambda x: int(x) / 1)) > 0):
            #     axes[0, 1].set_ylim([0, 1.1 * max(BAT1Q.apply(lambda x: int(x) / 1))])
            # elif (max(BAT1Q.apply(lambda x: int(x) / 1)) > 0 and min(BAT1Q.apply(lambda x: int(x) / 1)) < 0):
            #     axes[0, 1].set_ylim(
            #         [1.1 * min(BAT1Q.apply(lambda x: int(x) / 1)), 1.1 * max(BAT1Q.apply(lambda x: int(x) / 1))])
            # elif (max(BAT1Q.apply(lambda x: int(x) / 1)) < 0):
            #     axes[0, 1].set_ylim([1.1 * min(BAT1Q.apply(lambda x: int(x) / 1)), 0])
            # # axes[0, 1].set_ylim([0, 1.1*max(BAT1Q.apply(lambda x: int(x) / 1))])
            # axes[0, 1].set_xlabel('time(sec)')
            # axes[0, 1].set_ylabel('Battery 1 reactive power (kVAr)')

            # plot Battery 1 SOC
            axes[1, 0].plot(time, BAT1SOC.apply(lambda x: int(x) / 100))
            axes[1, 0].set_xlim([0, len(time)])
            # axes[0, 1].set_ylim([0.7, 1.3])
            axes[1, 0].set_xlabel('time(sec)')
            axes[1, 0].set_ylabel('Battery 1 SOC (%)')

            ## plot Battery 1 frequency
            # axes[1, 1].plot(time, BAT1F.apply(lambda x: int(x) / 100))
            # axes[1, 1].set_xlim([0, len(time)])
            # axes[1, 1].set_ylim([59.5, 60.5])
            # axes[1, 1].set_xlabel('time(sec)')
            # axes[1, 1].set_ylabel('Battery 1 frequency (Hz)')

            ## plot Battery 2 kW
            axes[0, 1].plot(time, BAT2P.apply(lambda x: int(x) / 1))
            axes[0, 1].set_xlim([0, len(time)])
            if (max(BAT2P.apply(lambda x: int(x) / 1)) > 0 and min(BAT2P.apply(lambda x: int(x) / 1)) > 0):
                axes[0, 1].set_ylim([0, 1.1 * max(BAT2P.apply(lambda x: int(x) / 1))])
            elif (max(BAT2P.apply(lambda x: int(x) / 1)) > 0 and min(BAT2P.apply(lambda x: int(x) / 1)) < 0):
                axes[0, 1].set_ylim(
                    [1.1 * min(BAT2P.apply(lambda x: int(x) / 1)), 1.1 * max(BAT2P.apply(lambda x: int(x) / 1))])
            elif (max(BAT2P.apply(lambda x: int(x) / 1)) < 0):
                axes[0, 1].set_ylim([1.1 * min(BAT2P.apply(lambda x: int(x) / 1)), 0])
            # axes[0, 2].set_ylim([0, 1.1*max(BAT2P.apply(lambda x: int(x) / 1))])
            axes[0, 1].set_xlabel('time(sec)')
            axes[0, 1].set_ylabel('Battery 2 active power (kW)')

            ## plot Battery 2 kVAr
            # axes[1, 1].plot(time, BAT2Q.apply(lambda x: int(x) / 1))
            # axes[1, 1].set_xlim([0, len(time)])
            # if (max(BAT2Q.apply(lambda x: int(x) / 1)) > 0 and min(BAT2Q.apply(lambda x: int(x) / 1)) > 0):
            #     axes[1, 1].set_ylim([0, 1.1 * max(BAT2Q.apply(lambda x: int(x) / 1))])
            # elif (max(BAT2Q.apply(lambda x: int(x) / 1)) > 0 and min(BAT2Q.apply(lambda x: int(x) / 1)) < 0):
            #     axes[1, 1].set_ylim(
            #         [1.1 * min(BAT2Q.apply(lambda x: int(x) / 1)), 1.1 * max(BAT2Q.apply(lambda x: int(x) / 1))])
            # elif (max(BAT2Q.apply(lambda x: int(x) / 1)) < 0):
            #     axes[1, 1].set_ylim([1.1 * min(BAT2Q.apply(lambda x: int(x) / 1)), 0])
            # # axes[0, 3].set_ylim([0, 1.1*max(BAT2Q.apply(lambda x: int(x) / 1))])
            # axes[1, 1].set_xlabel('time(sec)')
            # axes[1, 1].set_ylabel('Battery 2 reactive power (kVAr)')

            ## plot Battery 2 SOC
            axes[1, 1].plot(time, BAT2SOC.apply(lambda x: int(x) / 100))
            axes[1, 1].set_xlim([0, len(time)])
            # axes[0, 1].set_ylim([0.7, 1.3])
            axes[1, 1].set_xlabel('time(sec)')
            axes[1, 1].set_ylabel('Battery 2 SOC (%)')

            ## plot Battery 2 frequency
            # axes[1, 3].plot(time, BAT2F.apply(lambda x: int(x) / 100))
            # axes[1, 3].set_xlim([0, len(time)])
            # axes[1, 3].set_ylim([59.5, 60.5])
            # axes[1, 3].set_xlabel('time(sec)')
            # axes[1, 3].set_ylabel('Battery 2 frequency (Hz)')

            plt.tight_layout()
            plt.show()
            # fig.savefig("test.png")
        else:
            raise ValueError('There is not such generation resource')   ## raise

########################################################################################################################
########################################################################################################################
########################################      PLOT FREQUENCY       #####################################################
########################################################################################################################
########################################################################################################################

    def plotfrequency(self):
        testdata = pd.read_csv(self.Fileloc)
        ## creating a dataset of desired values to be plotted
        FL1 = testdata[str(749)][1:]
        FL3 = testdata[str(750)][1:]
        FL5 = testdata[str(751)][1:]
        FL7 = testdata[str(752)][1:]
        FL8 = testdata[str(753)][1:]
        FL11 = testdata[str(754)][1:]
        FL12 = testdata[str(755)][1:]
        time = pd.DataFrame(np.arange(1, len(FL1) + 1))

        ############# plotting voltage  #############
        fig, axes = plt.subplots(nrows=3, ncols=3)  ## create a subplot
        # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")


        ## plot frequency of Load 1
        axes[0, 0].plot(time, FL1.apply(lambda x: int(x) / 100))
        axes[0, 0].set_xlim([0, len(time)])
        axes[0, 0].set_ylim([59.5, 60.5])
        axes[0, 0].set_xlabel('time(sec)')
        axes[0, 0].set_ylabel('Frequency of \n Load 1 (Hz)')

        ## plot frequency of Load 3
        axes[0, 1].plot(time, FL3.apply(lambda x: int(x) / 100))
        axes[0, 1].set_xlim([0, len(time)])
        axes[0, 1].set_ylim([59.5, 60.5])
        axes[0, 1].set_xlabel('time(sec)')
        axes[0, 1].set_ylabel('Frequency of \n Load 3 (Hz)')

        ## plot frequency of Load 5
        axes[0, 2].plot(time, FL5.apply(lambda x: int(x) / 100))
        axes[0, 2].set_xlim([0, len(time)])
        axes[0, 2].set_ylim([59.5, 60.5])
        axes[0, 2].set_xlabel('time(sec)')
        axes[0, 2].set_ylabel('Frequency of \n Load 5 (Hz)')

        ## plot frequency of Load 7
        axes[1, 0].plot(time, FL7.apply(lambda x: int(x) / 100))
        axes[1, 0].set_xlim([0, len(time)])
        axes[1, 0].set_ylim([59.95, 60.05])
        axes[1, 0].set_xlabel('time(sec)')
        axes[1, 0].set_ylabel('Frequency of \n Load 7 (Hz)')

        ## plot frequency of Load 8
        axes[1, 1].plot(time, FL8.apply(lambda x: int(x) / 100))
        axes[1, 1].set_xlim([0, len(time)])
        axes[1, 1].set_ylim([59.5, 60.5])
        axes[1, 1].set_xlabel('time(sec)')
        axes[1, 1].set_ylabel('Frequency of \n Load 8 (Hz)')

        ## plot frequency of Load 11
        axes[1, 2].plot(time, FL11.apply(lambda x: int(x) / 100))
        axes[1, 2].set_xlim([0, len(time)])
        axes[1, 2].set_ylim([59.5, 60.5])
        axes[1, 2].set_xlabel('time(sec)')
        axes[1, 2].set_ylabel('Frequency of \n Load 11 (Hz)')

        ## plot frequency of Load 12
        axes[2, 0].plot(time, FL12.apply(lambda x: int(x) / 100))
        axes[2, 0].set_xlim([0, len(time)])
        axes[2, 0].set_ylim([59.5, 60.5])
        axes[2, 0].set_xlabel('time(sec)')
        axes[2, 0].set_ylabel('Frequency of \n Load 12 (Hz)')

        plt.tight_layout()
        plt.show()

########################################################################################################################
########################################################################################################################
########################################      PLOT HIL TIME       #####################################################
########################################################################################################################
########################################################################################################################

    def plothiltime(self):
        testdata = pd.read_csv(self.Fileloc)
        ## creating a dataset of desired values to be plotted
        HILT = testdata[str(756)][1:]
        time = pd.DataFrame(np.arange(1, len(HILT) + 1))

        ############# plotting voltage  #############
        fig, axes = plt.subplots(nrows=1, ncols=1)  ## create a subplot
        # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")


        ## plot HIL time
        axes.plot(time, HILT.apply(lambda x: int(x) / 100))
        axes.set_xlim([0, len(time)])
        #axes.set_ylim([59.5, 60.5])
        axes.set_xlabel('time(sec)')
        axes.set_ylabel('Hardware in the Loop time (Sec)')

        plt.tight_layout()
        plt.show()


########################################################################################################################
########################################################################################################################
#####################################     PLOT STATUS (temporary)       ################################################
########################################################################################################################
########################################################################################################################


    def plotstatus(self, hrnumber):
        self.hrnumber = hrnumber
        testdata = pd.read_csv(self.Fileloc)
        ## creating a dataset of desired values to be plotted
        status = testdata[str(self.hrnumber)][1:]
        time = pd.DataFrame(np.arange(1, len(status) + 1))

        ############# plotting voltage  #############
        fig, axes = plt.subplots(nrows=1, ncols=1)  ## create a subplot
        # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")


        ## plot HIL time
        axes.plot(time, status.apply(lambda x: int(x) / 1))
        axes.set_xlim([0, len(time)])
        #axes.set_ylim([59.5, 60.5])
        axes.set_yticks([0,1])
        axes.set_yticklabels(['0','1'])
        # ylabels = ['0','1']
        # axes.set_yticklabels(ylabels)
        axes.set_xlabel('time(sec)')
        axes.set_ylabel('Status [0]: open [1]: close')

        plt.tight_layout()
        plt.show()