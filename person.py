class Person:
    def __init__(self):
        self._full_name = None
        self._money = None
        self._sleepmood = None
        self._healthRate = None

#full_name attribute setter & getter
#----------------------------
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter   
    def full_name(self, full_name):
        self._full_name = full_name

#money attribute setter & getter
#---------------------------------
    @property
    def money(self):
        return self._money

    @money.setter   
    def money(self, money):
        self._money = money

#sleepmood attribute setter & getter
#----------------------------------
    @property
    def sleepmood(self):
        return self._sleepmood

    @sleepmood.setter   
    def sleepmood(self, sleepmood):
        self._sleepmood = sleepmood

#healthRate attribute setter & getter
#------------------------------------
    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter   
    def healthRate(self, healthRate):
        if healthRate >= 0 and healthRate <= 100:
            self._healthRate = healthRate
        else:
            raise ValueError("HealthRate must be in range 0 to 100")

#Person sleep method
#--------------------

    def sleep(self,hours):
        if hours == 7:
            self.sleepmood = "happy"
        elif hours > 0 and hours < 7:
            self.sleepmood = "tired"
        elif hours > 7 and hours <= 24:
            self.sleepmood = "lazy"
        else:
            self.sleepmood = "none"

#Person eat method
#--------------------

    def eat(self,meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

#Person buy method
#--------------------

    def buy(self,items):
        self.money = self.money - (10 * items)





