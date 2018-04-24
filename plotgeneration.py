# plotting generation resources


## import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class PlotGeneration():

#############################################################
########################  CHP ###############################
#############################################################

    def plotchp(self):
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
        CHPP = AI1[str(730)][1:]
        CHPQ = AI1[str(731)][1:]
        CHPS = AI1[str(732)][1:]
        CHPF = AI1[str(733)][1:]
        time = pd.DataFrame(np.arange(1, len(CHPP) + 1))

        ############# plotting voltage  #############
        fig, axes = plt.subplots(nrows=2, ncols=2)  ## create a subplot
        # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

        ## plot CHP kW
        axes[0, 0].plot(time, CHPP.apply(lambda x: int(x) / 1))
        axes[0, 0].set_xlim([0, 300])
        #axes[0, 0].set_ylim([0.7, 1.3])
        axes[0, 0].set_xlabel('time(sec)')
        axes[0, 0].set_ylabel('CHP active power (kW)')

        ## plot CHP kVAr
        axes[0, 1].plot(time, CHPQ.apply(lambda x: int(x) / 1))
        axes[0, 1].set_xlim([0, 300])
        axes[0, 1].set_xlabel('time(sec)')
        axes[0, 1].set_ylabel('CHP reactive power (kVAr)')

        ## plot CHP Speed
        axes[1, 0].plot(time, CHPS.apply(lambda x: int(x) / 100))
        axes[1, 0].set_xlim([0, 300])
        #axes[0, 1].set_ylim([0.7, 1.3])
        axes[1, 0].set_xlabel('time(sec)')
        axes[1, 0].set_ylabel('CHP speed (rad/sec)')

        ## plot CHP fuel
        axes[1, 1].plot(time, CHPF.apply(lambda x: int(x) / 100))
        axes[1, 1].set_xlim([0, 300])
        axes[1, 1].set_xlabel('time(sec)')
        axes[1, 1].set_ylabel('CHP fuel (f^3)')

        plt.tight_layout()
        plt.show()
        # fig.savefig("test.png")

#############################################################
##################### SOLAR PV ##############################
#############################################################

    def plotsolarpv(self):
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
        PVP = AI1[str(734)][1:]
        PVQ = AI1[str(735)][1:]
        PVIr = AI1[str(736)][1:]
        time = pd.DataFrame(np.arange(1, len(PVP) + 1))

        ############# plotting voltage  #############
        fig, axes = plt.subplots(nrows=1, ncols=3)  ## create a subplot
        # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

        ## plot PV kW
        axes[0].plot(time, PVP.apply(lambda x: int(x) / 1))
        axes[0].set_xlim([0, 300])
        #axes[0, 0].set_ylim([0.7, 1.3])
        axes[0].set_xlabel('time(sec)')
        axes[0].set_ylabel('PV active power (kW)')

        ## plot PV kVAr
        axes[1].plot(time, PVQ.apply(lambda x: int(x) / 1))
        axes[1].set_xlim([0, 300])
        axes[1].set_xlabel('time(sec)')
        axes[1].set_ylabel('PV reactive power (kVAr)')

        ## plot PV Irradiation
        axes[2].plot(time, PVIr.apply(lambda x: int(x) / 100))
        axes[2].set_xlim([0, 300])
        #axes[0, 1].set_ylim([0.7, 1.3])
        axes[2].set_xlabel('time(sec)')
        axes[2].set_ylabel('PV Irradiation (%)')

        plt.tight_layout()
        plt.show()
        # fig.savefig("test.png")


#############################################################
######################  DIESEL  #############################
#############################################################

    def plotdiesel(self):
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
        ENGP = AI1[str(737)][1:]
        ENGQ = AI1[str(738)][1:]
        ENGS = AI1[str(739)][1:]
        ENGF = AI1[str(740)][1:]
        time = pd.DataFrame(np.arange(1, len(ENGP) + 1))

        ############# plotting voltage  #############
        fig, axes = plt.subplots(nrows=2, ncols=2)  ## create a subplot
        # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

        ## plot Diesel kW
        axes[0, 0].plot(time, ENGP.apply(lambda x: int(x) / 1))
        axes[0, 0].set_xlim([0, 300])
        #axes[0, 0].set_ylim([0.7, 1.3])
        axes[0, 0].set_xlabel('time(sec)')
        axes[0, 0].set_ylabel('Diesel active power (kW)')

        ## plot Diesel kVAr
        axes[0, 1].plot(time, ENGQ.apply(lambda x: int(x) / 1))
        axes[0, 1].set_xlim([0, 300])
        axes[0, 1].set_xlabel('time(sec)')
        axes[0, 1].set_ylabel('Diesel reactive power (kVAr)')

        ## plot Diesel Speed
        axes[1, 0].plot(time, ENGS.apply(lambda x: int(x) / 100))
        axes[1, 0].set_xlim([0, 300])
        #axes[0, 1].set_ylim([0.7, 1.3])
        axes[1, 0].set_xlabel('time(sec)')
        axes[1, 0].set_ylabel('Diesel speed (rad/sec)')

        ## plot Diesel fuel
        axes[1, 1].plot(time, ENGF.apply(lambda x: int(x) / 100))
        axes[1, 1].set_xlim([0, 300])
        axes[1, 1].set_xlabel('time(sec)')
        axes[1, 1].set_ylabel('Diesel fuel (f^3)')

        plt.tight_layout()
        plt.show()
        # fig.savefig("test.png")



#############################################################
######################  Battery  #############################
#############################################################

    def plotbattery(self):
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
        BAT1P = AI1[str(741)][1:]
        BAT1Q = AI1[str(742)][1:]
        BAT1SOC = AI1[str(743)][1:]
        BAT1F = AI1[str(744)][1:]
        BAT2P = AI1[str(745)][1:]
        BAT2Q = AI1[str(746)][1:]
        BAT2SOC = AI1[str(747)][1:]
        BAT2F = AI1[str(748)][1:]
        time = pd.DataFrame(np.arange(1, len(BAT1P) + 1))

        ############# plotting voltage  #############
        fig, axes = plt.subplots(nrows=2, ncols=4)  ## create a subplot
        # st = fig.suptitle("F_11 Breaker Voltage", fontsize="x-large")

        ## plot Battery 1 kW
        axes[0, 0].plot(time, BAT1P.apply(lambda x: int(x) / 1))
        axes[0, 0].set_xlim([0, 300])
        #axes[0, 0].set_ylim([0.7, 1.3])
        axes[0, 0].set_xlabel('time(sec)')
        axes[0, 0].set_ylabel('Battery 1 active power (kW)')

        ## plot Battery 1 kVAr
        axes[0, 1].plot(time, BAT1Q.apply(lambda x: int(x) / 1))
        axes[0, 1].set_xlim([0, 300])
        axes[0, 1].set_xlabel('time(sec)')
        axes[0, 1].set_ylabel('Battery 1 reactive power (kVAr)')

        ## plot Battery 1 SOC
        axes[1, 0].plot(time, BAT1SOC.apply(lambda x: int(x) / 100))
        axes[1, 0].set_xlim([0, 300])
        #axes[0, 1].set_ylim([0.7, 1.3])
        axes[1, 0].set_xlabel('time(sec)')
        axes[1, 0].set_ylabel('Battery 1 SOC (%)')

        ## plot Battery 1 frequency
        axes[1, 1].plot(time, BAT1F.apply(lambda x: int(x) / 100))
        axes[1, 1].set_xlim([0, 300])
        axes[1, 1].set_ylim([59.5, 60.5])
        axes[1, 1].set_xlabel('time(sec)')
        axes[1, 1].set_ylabel('Battery 1 frequency (Hz)')

        ## plot Battery 2 kW
        axes[0, 2].plot(time, BAT2P.apply(lambda x: int(x) / 1))
        axes[0, 2].set_xlim([0, 300])
        #axes[0, 0].set_ylim([0.7, 1.3])
        axes[0, 2].set_xlabel('time(sec)')
        axes[0, 2].set_ylabel('Battery 2 active power (kW)')

        ## plot Battery 1 kVAr
        axes[0, 3].plot(time, BAT2Q.apply(lambda x: int(x) / 1))
        axes[0, 3].set_xlim([0, 300])
        axes[0, 3].set_xlabel('time(sec)')
        axes[0, 3].set_ylabel('Battery 2 reactive power (kVAr)')

        ## plot Battery 1 SOC
        axes[1, 2].plot(time, BAT2SOC.apply(lambda x: int(x) / 100))
        axes[1, 2].set_xlim([0, 300])
        #axes[0, 1].set_ylim([0.7, 1.3])
        axes[1, 2].set_xlabel('time(sec)')
        axes[1, 2].set_ylabel('Battery 2 SOC (%)')

        ## plot Battery 1 frequency
        axes[1, 3].plot(time, BAT2F.apply(lambda x: int(x) / 100))
        axes[1, 3].set_xlim([0, 300])
        axes[1, 3].set_ylim([59.5, 60.5])
        axes[1, 3].set_xlabel('time(sec)')
        axes[1, 3].set_ylabel('Battery 2 frequency (Hz)')

        plt.tight_layout()
        plt.show()
        # fig.savefig("test.png")