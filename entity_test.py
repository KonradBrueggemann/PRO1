from entity import Physical_Entity, Machine, MilkingMachine, Zamboni

Toaster = Physical_Entity(age= 1, function= True, invention= 1905, maxAge= 5)

Train = Machine(age= 10, function= False, invention= 1804, maxAge= 50, difficulties= True)

Melkeimer = MilkingMachine(age= 10, function= True, invention= 1990, maxAge= 20, difficulties= False, milk= 100)

Eisbär = Zamboni(age= 15, function= True, invention= 1949, maxAge= 30, difficulties= False, smoothness= False)

if __name__ == "__main__":
    #print(Toaster.age)
    #Toaster.aging(5)
    #print(Toaster.age)
    #print(Train.function)
    #Train.repair()
    #print(Train.function)
    #print(Melkeimer.milk)
    #Melkeimer.milking(500)
    #print(Melkeimer.milk)
    print(Eisbär.smoothness)
    Eisbär.smoothing()
    print(Eisbär.smoothness)


