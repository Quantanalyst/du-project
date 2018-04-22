### Accidental Islanding Test



## attributes of the accidental islanding test:
## initial conditions: OPC, CB-F11, CB-F09, Tie, Load, CHP, PV, BESSs, Diesel
## test contingency: Open CB-F11 or Open CB-F09

class Accidental():

    ## class object attributes (true for the class in general)
    islanding = 'Accidental'

    ## attributes true to a certain instance of a class
    def __init__(self,OPC,CBF11,CBF09,Tie,Load,CHP,PV,BESSs,Diesel,Contingency):
        self.OPC = OPC
        self.CBF11 = CBF11
        self.CBF09 = CBF09
        self.Tie = Tie
        self.Load = Load
        self.CHP = CHP
        self.PV = PV
        self.BESSs = BESSs
        self.Diesel = Diesel
        self.Contingency = Contingency

    ## methods
    def initialcondition(self):
        print("This scenario has the following initial condition:\ninitial operating condition = {}\nThe status of CB-F11 switch = {}\n"
              "The status of CB-F09 switch = {}\nThe status of Tie switch = {}\nThe condition of Load = {}\nThe condition of CHP generator = {}\n"
              "The condition of PV cells = {}\nThe condition of batteries = {}\nThe condition of diesel generator = {}\nThe target contingency = {} ".format(self.OPC, self.CBF11,
        self.CBF09, self.Tie, self.Load, self.CHP, self.PV, self.BESSs, self.Diesel, self.Contingency))

    def __plot__(self):
        # perform some action
        print(self.device)


