#### This piece of code stores the intial and final status of all devices and in case of status change, the timing of change
# attributes :
# methods :
# systemcondition : this method return a list of all HR numbers that their status changed
# systemconditionchange : this method prints the list of all HR numbers with status change, with their full description and time of status change
## import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from colorama import Fore
from colorama import Style

class SystemCondition():

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
        elif (self.testtype == 'BD'):
            self.Fileloc = self.path + '\\tests\\8.' + str(self.testnumber - 1) + ' BD-' + str(self.testnumber) + '.csv'
        elif (self.testtype == 'LR'):
            self.Fileloc = self.path + '\\tests\\9.' + str(self.testnumber - 1) + ' LR-' + str(self.testnumber) + '.csv'
        elif (self.testtype == 'RTD'):
            self.Fileloc = self.path + '\\tests\\11.' + str(self.testnumber - 1) + ' RTD-' + str(self.testnumber) + '.csv'
        elif (self.testtype == 'CLUST'):
            self.Fileloc = self.path + '\\tests\\14.' + str(self.testnumber - 1) + ' CLUST-' + str(self.testnumber) + '.csv'

        # print('test data location: {}'.format(self.Fileloc))

        self.testdata = pd.read_csv(self.Fileloc)

    def systemcondition(self):        # this method return a list of all HR numbers that their status changed
        self.systemcondition = []
        for val1 in np.arange(801, 1151):
            if (list(self.status['Description'][self.status['HR Number'] == val1])[0] == 'RESERVED'):
                pass
            else:
                cond_list = []
                D = list(self.testdata[str(val1)][1:])
                lens = len(D)
                cond_list.append(val1)
                cond_list.append(D[0])
                for val2 in np.arange(0, lens - 1):
                    if (int(D[val2 + 1]) - int(D[val2]) != 0):
                        cond_list.append(val2)
                        break
                if (len(cond_list) != 3):
                    cond_list.append('nan')
                cond_list.append(D[lens - 1])
                self.systemcondition.append(cond_list)
        self.changedHRnumber = []
        for val in np.arange(0, len(self.systemcondition)):
            if (self.systemcondition[val][2] != 'nan'):
                self.changedHRnumber.append(self.systemcondition[val][0])
        return self.changedHRnumber

    def systemconditionchange(self):    # this method prints the list of all HR numbers with status change, with their description and time of status change
        self.systemcondition = []
        for val1 in np.arange(801, 1151):
            if (list(self.status['Description'][self.status['HR Number'] == val1])[0] == 'RESERVED'):
                pass
            else:
                cond_list = []
                D = list(self.testdata[str(val1)][1:])
                lens = len(D)
                cond_list.append(val1)
                cond_list.append(D[0])
                for val2 in np.arange(0, lens - 1):
                    if (int(D[val2 + 1]) - int(D[val2]) != 0):
                        time = val2 + 1
                        cond_list.append(time)
                if (len(cond_list) == 2):
                    cond_list.append('nan')
                cond_list.append(D[lens - 1])
                self.systemcondition.append(cond_list)

        for val in np.arange(0, len(self.systemcondition)):
            if (self.systemcondition[val][2] != 'nan'):
                print('HR Number ' + str(self.systemcondition[val][0]) + ' changed : ' +
                      list(self.status['Description'][self.status['HR Number'] == self.systemcondition[val][0]])[0])
                changecount = len(self.systemcondition[val]) - 3
                dstatus = ['open', 'close']
                if (self.systemcondition[val][1] == '0'):
                    for val3 in np.arange(1, changecount + 1):
                        print(dstatus[val3 % 2] + ' at t= ' + str(self.systemcondition[val][1 + val3]) + ' [sec]')
                else:
                    for val3 in np.arange(1, changecount + 1):
                        print(dstatus[(val3 + 1) % 2] + ' at t= ' + str(self.systemcondition[val][1 + val3]) + ' [sec]')


    def statuschanges(self):    # this method return the detailed status changes
        self.statuschanges = []
        for val1 in np.arange(801, 1151):
            if (list(self.status['Description'][self.status['HR Number'] == val1])[0] == 'RESERVED'):
                pass
            else:
                cond_list = []
                D = list(self.testdata[str(val1)][1:])
                lens = len(D)
                cond_list.append(val1)
                cond_list.append(D[0])
                for val2 in np.arange(0, lens - 1):
                    if (int(D[val2 + 1]) - int(D[val2]) != 0):
                        time = val2 + 2
                        cond_list.append(time)
                if (len(cond_list) == 2):
                    cond_list.append('nan')
                cond_list.append(D[lens - 1])
                self.statuschanges.append(cond_list)
        return self.statuschanges

    def loadrestoration(self):
        self.statuschanges = self.statuschanges()
        self.sysre = []
        self.syssh = []
        self.acsysop = []  # operands activated
        self.desysop = []  # operands deactivated

        for val in np.arange(0, len(self.statuschanges)):
            if (self.statuschanges[val][2] == 'nan'):
                pass
            elif (self.statuschanges[val][2] != 'nan' and int(self.statuschanges[val][0]) > 863):
                changenum = len(self.statuschanges[val]) - 3
                for val2 in np.arange(0, changenum):
                    if (self.statuschanges[val][1] == '0'):
                        if (val2 % 2 == 0):
                            lr = [self.statuschanges[val][2 + val2],int(list(self.status['HR Number'][self.status['HR Number'] == self.statuschanges[val][0]])[0]),
                                  list(self.status['Description'][self.status['HR Number'] == self.statuschanges[val][0]])[0]]
                            self.acsysop.append(lr)
                        else:
                            ls = [self.statuschanges[val][2 + val2],int(list(self.status['HR Number'][self.status['HR Number'] == self.statuschanges[val][0]])[0]),
                                  list(self.status['Description'][self.status['HR Number'] == self.statuschanges[val][0]])[0]]
                            self.desysop.append(ls)
                    elif (self.statuschanges[val][1] == '1'):
                        if (val2 % 2 == 0):
                            ls = [self.statuschanges[val][2 + val2],int(list(self.status['HR Number'][self.status['HR Number'] == self.statuschanges[val][0]])[0]),
                                  list(self.status['Description'][self.status['HR Number'] == self.statuschanges[val][0]])[0]]
                            self.desysop.append(ls)
                        else:
                            lr = [self.statuschanges[val][2 + val2],int(list(self.status['HR Number'][self.status['HR Number'] == self.statuschanges[val][0]])[0]),
                                  list(self.status['Description'][self.status['HR Number'] == self.statuschanges[val][0]])[0]]
                            self.acsysop.append(lr)
            else:
                changenum = len(self.statuschanges[val]) - 3
                for val2 in np.arange(0, changenum):
                    if (self.statuschanges[val][1] == '0'):
                        if (val2 % 2 == 0):
                            lr = [self.statuschanges[val][2 + val2],int(list(self.status['HR Number'][self.status['HR Number'] == self.statuschanges[val][0]])[0]),
                                  list(self.status['Description'][self.status['HR Number'] == self.statuschanges[val][0]])[0]]
                            self.sysre.append(lr)
                        else:
                            ls = [self.statuschanges[val][2 + val2],int(list(self.status['HR Number'][self.status['HR Number'] == self.statuschanges[val][0]])[0]),
                                  list(self.status['Description'][self.status['HR Number'] == self.statuschanges[val][0]])[0]]
                            self.syssh.append(ls)
                    elif (self.statuschanges[val][1] == '1'):
                        if (val2 % 2 == 0):
                            ls = [self.statuschanges[val][2 + val2],int(list(self.status['HR Number'][self.status['HR Number'] == self.statuschanges[val][0]])[0]),
                                  list(self.status['Description'][self.status['HR Number'] == self.statuschanges[val][0]])[0]]
                            self.syssh.append(ls)
                        else:
                            lr = [self.statuschanges[val][2 + val2],int(list(self.status['HR Number'][self.status['HR Number'] == self.statuschanges[val][0]])[0]),
                                  list(self.status['Description'][self.status['HR Number'] == self.statuschanges[val][0]])[0]]
                            self.sysre.append(lr)

                            ######### Print the results ########
        self.syssh = sorted(self.syssh)
        self.sysre = sorted(self.sysre)
        self.acsysop = sorted(self.acsysop)
        self.desysop = sorted(self.desysop)
        print('------------------ Activated/Close operands ---------------------\n')
        for val in np.arange(0, len(self.acsysop)):
            print(self.acsysop[val])
        print('\n------------------ Deactivated/Open operands ---------------------\n')
        for val in np.arange(0, len(self.desysop)):
            print(self.desysop[val])
        print('\n------------------ System Shutdown ---------------------\n')
        for val in np.arange(0, len(self.syssh)):
            print(self.syssh[val])
        print('\n------------------ System Restoration ---------------------\n')
        for val in np.arange(0, len(self.sysre)):
            print(self.sysre[val])
