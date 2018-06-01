#### This piece of code performs power flow
# attributes : typetest, testnumber
# methods : catstatuscheck, allstatuscheck, onlychangedstatus
## import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from colorama import Fore
from colorama import Style


class PowerFlow():

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
        self.status = pd.read_excel(self.infoloc,sheet_name="PI Measurement")
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

        # print('test data location: {}'.format(self.Fileloc))

        self.testdata = pd.read_csv(self.Fileloc)

    def powerflow(self):

        # import pandas as pd
        # import numpy as np
        # import matplotlib.pyplot as plt
        #
        # from colorama import Fore
        # from colorama import Style
        #
        # infoloc = "C:\\Users\\Saeed Mohajeryami\\Dropbox\\DOE project\\Reports_Slides_Codes\\du-project\\PI Point List_v13.5.xlsm"
        # status = pd.read_excel(infoloc, sheet_name="PI Status (feedback)")
        # measurement = pd.read_excel(infoloc, sheet_name='PI Measurement')
        #
        # Fileloc = "C:\\Users\\Saeed Mohajeryami\\Dropbox\\DOE project\\tests\\2.0 PI-1.csv"
        # testdata = pd.read_csv(Fileloc)
        #
        #
        # print(
        #     '---------------------------------------------subsystem 1 ----------------------------------------------------------')
        #
        # print(
        #     '\nF11 ------ B101 ------- B102 ------- B103 ------- B108 ------- B111 ------ B112 ------- B113 ------- B115')
        # print(str(int(testdata[str(2)][1]) / 100) + ' ----- ' + str(int(testdata[str(14)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(20)][1]) / 100) + ' ----- ' + str(int(testdata[str(26)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(56)][1]) / 100) + ' ----- ' + str(int(testdata[str(74)][1]) / 100) + ' ---- ' +
        #       str(int(testdata[str(80)][1]) / 100) + ' ----- ' + str(int(testdata[str(86)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(98)][1]) / 100))
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch from B103) ----->  B104  ------- B105 ------- B106 ------- B107')
        # print('------------------------> ' + str(int(testdata[str(32)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(38)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(44)][1]) / 100) + ' ----- ' + str(int(testdata[str(50)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> ' + str(int(testdata[str(556)][1]) * 3) + '+' + str(
        #     int(testdata[str(557)][1]) * 3) + 'i ' +
        #       '--- ' + str(int(testdata[str(562)][1]) * 3) + '+' + str(int(testdata[str(563)][1]) * 3) + 'i ' +
        #       '---- ' + str(int(testdata[str(568)][1]) * 3) + '+' + str(int(testdata[str(569)][1]) * 3) + 'i ' +
        #       '------ ' + str(int(testdata[str(574)][1]) * 3) + '+' + str(int(testdata[str(575)][1]) * 3) + 'i ')
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch from B108) ----->  B109  ------- B110')
        # print('------------------------> ' + str(int(testdata[str(62)][1]) / 100) +
        #       ' ----- ' + str(int(testdata[str(68)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> ' + str(int(testdata[str(580)][1]) * 3) + '+' + str(
        #     int(testdata[str(581)][1]) * 3) + 'i ' +
        #       '------ ' + str(int(testdata[str(586)][1]) * 3) + '+' + str(int(testdata[str(587)][1]) * 3) + 'i ')
        # print('[GEN - PV]:  ' + ' ----------> ' + str(int(testdata[str(734)][1])) + '+' + str(
        #     int(testdata[str(735)][1])) + 'i ')
        # print('[GEN - BAT1]:  ' + ' --------> ' + str(int(testdata[str(741)][1])) + '+' + str(
        #     int(testdata[str(742)][1])) + 'i ')
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch from B113) ----->  B114')
        # print('------------------------> ' + str(int(testdata[str(92)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> ' + str(int(testdata[str(592)][1]) * 3) + '+' + str(
        #     int(testdata[str(593)][1]) * 3) + 'i ')
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print(
        #     '\n(cont.) B116 ------ B117 ------- B118 -------  B123 ------- B124 ------ B125 ------- B130 ------- B131')
        # print('      ' + str(int(testdata[str(104)][1]) / 100) + ' ----- ' + str(
        #     int(testdata[str(110)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(116)][1]) / 100) + ' ----- ' + str(int(testdata[str(146)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(152)][1]) / 100) + ' ----- ' + str(int(testdata[str(158)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(188)][1]) / 100) + ' ----- ' + str(int(testdata[str(194)][1]) / 100))
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch 1 from B118) ----->  B119 ----->  B120')
        # print('--------------------------> ' + str(int(testdata[str(122)][1]) / 100) + ' ----- ' + str(
        #     int(testdata[str(128)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> -------------- ' + str(int(testdata[str(598)][1]) * 3) + '+' + str(
        #     int(testdata[str(599)][1]) * 3) + 'i ')
        # print('[GEN - CHP]:  ' + ' ---------> -------------- ' + str(int(testdata[str(730)][1])) + '+' + str(
        #     int(testdata[str(731)][1])) + 'i ')
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch 2 from B118) ----->  B121 ----->  B122')
        # print('--------------------------> ' + str(int(testdata[str(134)][1]) / 100) + ' ----- ' + str(
        #     int(testdata[str(140)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> -------------- ' + str(int(testdata[str(604)][1]) * 3) + '+' + str(
        #     int(testdata[str(605)][1]) * 3) + 'i ')
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch 1 from B125) ----->  B126 ----->  B127')
        # print('--------------------------> ' + str(int(testdata[str(164)][1]) / 100) + ' ----- ' + str(
        #     int(testdata[str(170)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> -------------- ' + str(int(testdata[str(610)][1]) * 3) + '+' + str(
        #     int(testdata[str(611)][1]) * 3) + 'i ')
        # print('[GEN - BAT2]:  ' + ' --------> -------------- ' + str(int(testdata[str(745)][1])) + '+' + str(
        #     int(testdata[str(746)][1])) + 'i ')
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch 2 from B125) ----->  B128 ----->  B129 ----->  B233')
        # print('--------------------------> ' + str(int(testdata[str(176)][1]) / 100) + ' ----- ' + str(
        #     int(testdata[str(182)][1]) / 100) +
        #       ' ----- ' + str(int(testdata[str(440)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> -------------- ' + str(int(testdata[str(616)][1]) * 3) + '+' + str(
        #     int(testdata[str(617)][1]) * 3) + 'i ' + '-------------- ')
        #
        # print('\n(Branch from B131) ----->  B132')
        # print('--------------------------> ' + str(int(testdata[str(200)][1]) / 100))
        #
        # print('\n(cont.) (To/From IIT) B131 ------ B133 ------- B134 ------- B137 ------- FIIT')
        # print('                     ' + str(int(testdata[str(194)][1]) / 100) + ' ----- ' + str(
        #     int(testdata[str(206)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(212)][1]) / 100) + ' ----- ' + str(int(testdata[str(230)][1]) / 100))
        #
        # print('\n(Branch 1 from B134) ----->  B135')
        # print('--------------------------> ' + str(int(testdata[str(218)][1]) / 100))
        #
        # print('\n(Branch 2 from B134) ----->  B136')
        # print('--------------------------> ' + str(int(testdata[str(224)][1]) / 100))
        #
        # print(
        #     '\n---------------------------------------------subsystem 2 ----------------------------------------------------------')
        #
        # print(
        #     '\nF09 ------ B201 ------- B202 ------- B203 ------- B208 ------- B209 ------ B211 ------- B212 ------- B214')
        # print(str(int(testdata[str(236)][1]) / 100) + ' ----- ' + str(int(testdata[str(248)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(254)][1]) / 100) + ' ----- ' + str(int(testdata[str(260)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(290)][1]) / 100) + ' ----- ' + str(int(testdata[str(296)][1]) / 100) + ' ---- ' +
        #       str(int(testdata[str(308)][1]) / 100) + ' ----- ' + str(int(testdata[str(314)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(326)][1]) / 100))
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch 1 from B203) ----->  B204 ----->  B205')
        # print('--------------------------> ' + str(int(testdata[str(266)][1]) / 100) + ' ----- ' + str(
        #     int(testdata[str(272)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> -------------- ' + str(int(testdata[str(622)][1]) * 3) + '+' + str(
        #     int(testdata[str(623)][1]) * 3) + 'i ')
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch 2 from B203) ----->  B206 ----->  B207')
        # print('--------------------------> ' + str(int(testdata[str(278)][1]) / 100) + ' ----- ' + str(
        #     int(testdata[str(284)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> -------------- ' + str(int(testdata[str(628)][1]) * 3) + '+' + str(
        #     int(testdata[str(629)][1]) * 3) + 'i ')
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch from B209) ----->  B210')
        # print('------------------------> ' + str(int(testdata[str(302)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> ' + str(int(testdata[str(634)][1]) * 3) + '+' + str(
        #     int(testdata[str(635)][1]) * 3) + 'i ')
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch from B212) ----->  B213')
        # print('------------------------> ' + str(int(testdata[str(320)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> ' + str(int(testdata[str(640)][1]) * 3) + '+' + str(
        #     int(testdata[str(641)][1]) * 3) + 'i ')
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(cont.) B219 ------ B220 ------- B221 ------  B226 ------ B229 ------ B230 ------ B231')
        # print('      ' + str(int(testdata[str(356)][1]) / 100) + ' ----- ' + str(
        #     int(testdata[str(362)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(368)][1]) / 100) + ' ----- ' + str(int(testdata[str(398)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(416)][1]) / 100) + ' ----- ' + str(int(testdata[str(422)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(428)][1]) / 100))
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch from B214) ----->  B215  ------- B216 ------- B217 ------- B218')
        # print('------------------------> ' + str(int(testdata[str(332)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(338)][1]) / 100) + ' ----- ' + str(int(testdata[str(344)][1]) / 100) +
        #       ' ----- ' + str(int(testdata[str(350)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> ' + str(int(testdata[str(646)][1]) * 3) + '+' + str(
        #     int(testdata[str(647)][1]) * 3) + 'i ' +
        #       '--- ' + str(int(testdata[str(652)][1]) * 3) + '+' + str(int(testdata[str(653)][1]) * 3) + 'i ' +
        #       '---- ' + str(int(testdata[str(658)][1]) * 3) + '+' + str(int(testdata[str(659)][1]) * 3) + 'i ' +
        #       '------ ' + str(int(testdata[str(664)][1]) * 3) + '+' + str(int(testdata[str(665)][1]) * 3) + 'i ')
        # print('[GEN - ENG]:  ' + ' ---------> -------------------------------------- ' + str(
        #     int(testdata[str(737)][1])) + '+' + str(int(testdata[str(738)][1])) + 'i ')
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch from B221) ----->  B222  ------- B223 ------- B224 ------- B225')
        # print('------------------------> ' + str(int(testdata[str(374)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(380)][1]) / 100) + ' ----- ' + str(int(testdata[str(386)][1]) / 100) +
        #       ' ----- ' + str(int(testdata[str(392)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> ' + str(int(testdata[str(670)][1]) * 3) + '+' + str(
        #     int(testdata[str(671)][1]) * 3) + 'i ' +
        #       '--- ' + str(int(testdata[str(676)][1]) * 3) + '+' + str(int(testdata[str(677)][1]) * 3) + 'i ' +
        #       '---- ' + str(int(testdata[str(682)][1]) * 3) + '+' + str(int(testdata[str(683)][1]) * 3) + 'i ' +
        #       '------ ' + str(int(testdata[str(688)][1]) * 3) + '+' + str(int(testdata[str(689)][1]) * 3) + 'i ')
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch from B226) ----->  B227  ------- B228')
        # print('------------------------> ' + str(int(testdata[str(404)][1]) / 100) + ' ----- ' + str(
        #     int(testdata[str(410)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> ' + str(int(testdata[str(694)][1]) * 3) + '+' + str(
        #     int(testdata[str(695)][1]) * 3) + 'i ' +
        #       '--- ' + str(int(testdata[str(700)][1]) * 3) + '+' + str(int(testdata[str(701)][1]) * 3) + 'i ')
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch from B231) ----->  B232')
        # print('--------------------------> ' + str(int(testdata[str(434)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> ' + str(int(testdata[str(706)][1]) * 3) + '+' + str(
        #     int(testdata[str(707)][1]) * 3) + 'i ')
        #
        # # -------------------------------------------------------------------------------------------------------#
        # print('\n(Branch from B231) ----->  B233  ------- B234 ------- B235')
        # print('------------------------> ' + str(int(testdata[str(440)][1]) / 100) + ' ----- ' +
        #       str(int(testdata[str(446)][1]) / 100) + ' ----- ' + str(int(testdata[str(452)][1]) / 100))
        # print('[LOAD]: ' + ' ---------------> ' + str(int(testdata[str(712)][1]) * 3) + '+' + str(
        #     int(testdata[str(713)][1]) * 3) + 'i ' +
        #       '--- ' + str(int(testdata[str(718)][1]) * 3) + '+' + str(int(testdata[str(719)][1]) * 3) + 'i ' +
        #       '---- ' + str(int(testdata[str(724)][1]) * 3) + '+' + str(int(testdata[str(725)][1]) * 3) + 'i ')