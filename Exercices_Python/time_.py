

class Time:

    def __init__(self, hour, mn, sec):
        try:
            if hour<0: raise ValueError
            if mn<0: raise ValueError
            if sec<0: raise ValueError
        except ValueError:
            print('Time values shall not be negative.')
            #exit()
        mn_add = sec //60
        self.sec = sec %60
        hour_add = (mn + mn_add) //60
        self.mn = (mn + mn_add) %60
        self.hour = (hour + hour_add) %24
        
    def __str__(self):
        if self.hour < 10: HH = '0'+str(self.hour)
        else:  HH = str(self.hour)
        if self.mn < 10: MM = '0'+str(self.mn) 
        else: MM = str(self.mn)
        if self.sec < 10: SS = '0'+str(self.sec)
        else: SS = str(self.sec)
        return HH + ':' + MM + ':' + SS

    def __add__(self, t2):
        if isinstance(t2,Time):
            MM_add = (self.sec + t2.sec) //60
            self.sec = (self.sec + t2.sec) %60
            HH_add = (self.mn + t2.mn + MM_add) //60
            self.mn = (self.mn + t2.mn + MM_add) %60 
            self.hour = (self.hour + t2.hour + HH_add)
            return self.__str__()
        elif isinstance(t2, int):
            MM_add = (self.sec + t2) //60
            self.sec = (self.sec + t2) %60
            HH_add = (self.mn + MM_add) //60
            self.mn = (self.mn + MM_add) %60 
            self.hour = (self.hour + HH_add)
            return self.__str__()
    
    def __sub__(self, t2):
        if isinstance(t2,Time):
            if (self.sec - t2.sec) < 0: MM_sub = 1; self.sec = 60 - abs(self.sec - t2.sec)
            else: MM_sub = 0; self.sec = self.sec - t2.sec
            if (self.mn - t2.mn) < 0: HH_sub = 1; self.mn = 60 - abs(self.mn - t2.mn - MM_sub)
            else: HH_sub = 0; self.mn = self.mn - t2.mn - MM_sub
            if (self.hour - t2.hour) < 0: self.hour = 24 - abs(self.hour - t2.hour - HH_sub)
            else: self.hour = self.hour - t2.hour - HH_sub
            return self.__str__()
        elif isinstance(t2, int):
            if t2 > 60: MM_sub = t2 //60; self.sec = 60 - abs(self.sec - t2) %60
            else: MM_sub = 0; self.sec = self.sec - t2
            if (self.mn - MM_sub) < 0: HH_sub = abs(self.mn - MM_sub) //60; self.mn = 60 - abs(self.mn - MM_sub) %60
            else: HH_sub = 0; self.mn = self.mn - MM_sub
            self.hour = self.hour - HH_sub
            return self.__str__()

    def __mul__(self, x):
        if (self.sec * x) >= 60: MM_mul = (self.sec * x) //60; self.sec = (self.sec * x) %60
        else: MM_mul = 0; self.sec = (self.sec * x)
        if (self.mn * x) >= 60: HH_mul = ((self.mn * x) +MM_mul) //60; self.mn = ((self.mn * x) +MM_mul) %60
        else: HH_mul = 0; self.mn = (self.mn * x) +MM_mul 
        self.hour = (self.hour * x) +HH_mul 
        return self.__str__()



a = Time(21,58,50)
print(type(a))
b = Time(1,45,22)
print(a,' + ',b)
print('__add__',a+b)
a = Time(21,58,50)
print(a,' + ',62)
print('__add__',a+62)
a = Time(21,58,50)
print(a,' - ',b)
print('__sub__',a-b)
a = Time(21,58,50)
print(a,' - ',62)
print('__sub__',a-62)
a = Time(21,58,50)
print(a,' * ',3)
print('__mul__',a*2)
