#### This piece of code checks the changes in the commands
# attributes : typetest, testnumber
# methods : catstatuscheck, allstatuscheck, onlychangedstatus
## import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from colorama import Fore
from colorama import Style

class ChangeStatusCheck():

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
        self.status = pd.read_excel(self.infoloc,sheet_name="PI Status (feedback)")
        # print('HR number info location: {}'.format(self.infoloc))

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

        # print('test data location: {}'.format(self.Fileloc))

        self.testdata = pd.read_csv(self.Fileloc)

    def catstatuscheck(self):

        ##### vista switches #####
        vista_hr_list = []
        for val1 in np.arange(801, 817):
            D = list(self.testdata[str(val1)][1:])
            lens = len(D)
            #     print(D)
            for val2 in np.arange(0, lens - 1):
                if (int(D[val2 + 1]) - int(D[val2]) != 0):
                    vista_hr_list.append(val1)
                    break
        if (len(vista_hr_list) == 0):
            print(f'{Fore.GREEN}\nRESULT{Style.RESET_ALL}' + ' : NO change has been detected in vista switches')
        else:
            print(f'{Fore.RED}\nRESULT{Style.RESET_ALL}' + ' : There is a change in following vista switches {}'.format(vista_hr_list))

        ##### PCL switches #####
        pcl_hr_list = []
        for val1 in np.arange(817, 826):
            D = list(self.testdata[str(val1)][1:])
            lens = len(D)
            #     print(D)
            for val2 in np.arange(0, lens - 1):
                if (int(D[val2 + 1]) - int(D[val2]) != 0):
                    pcl_hr_list.append(val1)
                    break
        if (len(pcl_hr_list) == 0):
            print(f'{Fore.GREEN}RESULT{Style.RESET_ALL}' + ' : NO change has been detected in PCL switches')
        else:
            print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in following PCL switches {}'.format(pcl_hr_list))

        ##### PCT switches #####
        pct_hr_list = []
        for val1 in [826]:
            D = list(self.testdata[str(val1)][1:])
            lens = len(D)
            #     print(D)
            for val2 in np.arange(0, lens - 1):
                if (int(D[val2 + 1]) - int(D[val2]) != 0):
                    pct_hr_list.append(val1)
                    break
        if (len(pct_hr_list) == 0):
            print(f'{Fore.GREEN}RESULT{Style.RESET_ALL}' + ' : NO change has been detected in PCT switches')
        else:
            print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in following PCT switches {}'.format(pct_hr_list))

        ##### Load Status #####
        load_hr_list = []
        for val1 in np.arange(830,859):
            D = list(self.testdata[str(val1)][1:])
            lens = len(D)
            #     print(D)
            for val2 in np.arange(0, lens - 1):
                if (int(D[val2 + 1]) - int(D[val2]) != 0):
                    load_hr_list.append(val1)
                    break
        if (len(load_hr_list) == 0):
            print(f'{Fore.GREEN}RESULT{Style.RESET_ALL}' + ' : NO change has been detected in Loads')
        else:
            print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in following Loads {}'.format(load_hr_list))

        ##### CHP Status #####
        chp_hr_list = []
        for val1 in [859]:
            D = list(self.testdata[str(val1)][1:])
            lens = len(D)
            #     print(D)
            for val2 in np.arange(0, lens - 1):
                if (int(D[val2 + 1]) - int(D[val2]) != 0):
                    chp_hr_list.append(val1)
                    break
        if (len(chp_hr_list) == 0):
            print(f'{Fore.GREEN}RESULT{Style.RESET_ALL}' + ' : NO change has been detected in CHP')
        else:
            print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in CHP {}'.format(chp_hr_list))

        ##### Solar PV Status #####
        pv_hr_list = []
        for val1 in [860]:
            D = list(self.testdata[str(val1)][1:])
            lens = len(D)
            #     print(D)
            for val2 in np.arange(0, lens - 1):
                if (int(D[val2 + 1]) - int(D[val2]) != 0):
                    pv_hr_list.append(val1)
                    break
        if (len(pv_hr_list) == 0):
            print(f'{Fore.GREEN}RESULT{Style.RESET_ALL}' + ' : NO change has been detected in Solar PV')
        else:
            print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in Solar PV {}'.format(pv_hr_list))

        ##### Diesel Generator Status #####
        eng_hr_list = []
        for val1 in [861]:
            D = list(self.testdata[str(val1)][1:])
            lens = len(D)
            #     print(D)
            for val2 in np.arange(0, lens - 1):
                if (int(D[val2 + 1]) - int(D[val2]) != 0):
                    eng_hr_list.append(val1)
                    break
        if (len(eng_hr_list) == 0):
            print(f'{Fore.GREEN}RESULT{Style.RESET_ALL}' + ' : NO change has been detected in Diesel Generator')
        else:
            print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in Diesel Generator {}'.format(eng_hr_list))

        ##### Battery 1 Status #####
        bat1_hr_list = []
        for val1 in [862]:
            D = list(self.testdata[str(val1)][1:])
            lens = len(D)
            #     print(D)
            for val2 in np.arange(0, lens - 1):
                if (int(D[val2 + 1]) - int(D[val2]) != 0):
                    bat1_hr_list.append(val1)
                    break
        if (len(bat1_hr_list) == 0):
            print(f'{Fore.GREEN}RESULT{Style.RESET_ALL}' + ' : NO change has been detected in Battery 1')
        else:
            print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in Battery 1 {}'.format(bat1_hr_list))

        ##### Battery 2 Status #####
        bat2_hr_list = []
        for val1 in [863]:
            D = list(self.testdata[str(val1)][1:])
            lens = len(D)
            #     print(D)
            for val2 in np.arange(0, lens - 1):
                if (int(D[val2 + 1]) - int(D[val2]) != 0):
                    bat2_hr_list.append(val1)
                    break
        if (len(bat2_hr_list) == 0):
            print(f'{Fore.GREEN}RESULT{Style.RESET_ALL}' + ' : NO change has been detected in Battery 2')
        else:
            print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in Battery 2 {}'.format(bat2_hr_list))

        ##### Operator Command Feedback/Status #####
        operator_hr_list = []
        for val1 in np.arange(864, 900):
            D = list(self.testdata[str(val1)][1:])
            lens = len(D)
            #     print(D)
            for val2 in np.arange(0, lens - 1):
                if (int(D[val2 + 1]) - int(D[val2]) != 0):
                    operator_hr_list.append(val1)
                    break
        if (len(operator_hr_list) == 0):
            print(f'{Fore.GREEN}RESULT{Style.RESET_ALL}' + ' : NO change has been detected in operator commands')
        else:
            print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in operator command {}'.format(operator_hr_list))

        ##### Synch Check Status #####
        sycheck_hr_list = []
        for val1 in np.arange(900, 912):
            D = list(self.testdata[str(val1)][1:])
            lens = len(D)
            #     print(D)
            for val2 in np.arange(0, lens - 1):
                if (int(D[val2 + 1]) - int(D[val2]) != 0):
                    sycheck_hr_list.append(val1)
                    break
        if (len(sycheck_hr_list) == 0):
            print(f'{Fore.GREEN}RESULT{Style.RESET_ALL}' + ' : NO change has been detected in Synch Check Status')
        else:
            print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in Synch Check Status {}'.format(
                sycheck_hr_list))

        ##### Logic Feedback/Status #####
        logic_hr_list = []
        for val1 in np.arange(922, 929):
            D = list(self.testdata[str(val1)][1:])
            lens = len(D)
            #     print(D)
            for val2 in np.arange(0, lens - 1):
                if (int(D[val2 + 1]) - int(D[val2]) != 0):
                    logic_hr_list.append(val1)
                    break
        if (len(logic_hr_list) == 0):
            print(f'{Fore.GREEN}RESULT{Style.RESET_ALL}' + ' : NO change has been detected in Logic Feedback/Status')
        else:
            print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in Logic Feedback/Status {}'.format(
                logic_hr_list))

        ##### Applied Commands for Logic Status #####
        alogic_hr_list = []
        for val1 in np.arange(940, 964):
            D = list(self.testdata[str(val1)][1:])
            lens = len(D)
            #     print(D)
            for val2 in np.arange(0, lens - 1):
                if (int(D[val2 + 1]) - int(D[val2]) != 0):
                    alogic_hr_list.append(val1)
                    break
        if (len(alogic_hr_list) == 0):
            print(f'{Fore.GREEN}RESULT{Style.RESET_ALL}' + ' : NO change has been detected in Applied Commands for Logic')
        else:
            print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in Applied Commands for Logic {}'.format(
                alogic_hr_list))

        ##### Applied Commands for all Breakers Status #####
        acb_hr_list = []
        for val1 in np.arange(975, 1124):
            D = list(self.testdata[str(val1)][1:])
            lens = len(D)
            #     print(D)
            for val2 in np.arange(0, lens - 1):
                if (int(D[val2 + 1]) - int(D[val2]) != 0):
                    acb_hr_list.append(val1)
                    break
        if (len(acb_hr_list) == 0):
            print(f'{Fore.GREEN}RESULT{Style.RESET_ALL}' + ' : NO change has been detected in Applied Commands for all Breakers')
        else:
            print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in Applied Commands for all Breakers {}'.format(
                acb_hr_list))


    def allstatuscheck(self):
        for val1 in np.arange(801, 1151):
            if (list(self.status['Description'][self.status['HR Number'] == val1])[0] == 'RESERVED'):
                pass
            else:
                hr_list = []
                D = list(self.testdata[str(val1)][1:])
                lens = len(D)
                #     print(D)
                for val2 in np.arange(0, lens - 1):
                    if (int(D[val2 + 1]) - int(D[val2]) != 0):
                        hr_list.append(val1)
                        break
                if (len(hr_list) == 0):
                    print( f'{Fore.GREEN}RESULT{Style.RESET_ALL}' + ' : NO change has been detected in ' + '"' +
                          list(self.status['Description'][self.status['HR Number'] == val1])[0] + '"')
                else:
                    print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in ' + '"' +
                          list(self.status['Description'][self.status['HR Number'] == val1])[0] + '"')

    def onlychangedstatus(self):
        self.change = 0
        for val1 in np.arange(801, 1151):
            if (list(self.status['Description'][self.status['HR Number'] == val1])[0] == 'RESERVED'):
                pass
            else:
                hr_list = []
                D = list(self.testdata[str(val1)][1:])
                lens = len(D)
                #     print(D)
                for val2 in np.arange(0, lens - 1):
                    if (int(D[val2 + 1]) - int(D[val2]) != 0):
                        hr_list.append(val1)
                        break
                if (len(hr_list) != 0):
                    self.change = self.change +1
                    print(f'{Fore.RED}RESULT{Style.RESET_ALL}' + ' : There is a change in ' + '"' +
                          list(self.status['Description'][self.status['HR Number'] == val1])[0] + '"')
        if (self.change == 0):
            print(f'{Fore.GREEN}NO CHANGE{Style.RESET_ALL}')