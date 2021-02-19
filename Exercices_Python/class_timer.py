class Timer:
    def __init__(self, h=0, m=0, s=0 ):
        self.hour = h
        self.min = m
        self.sec = s

    def __str__(self):
        if self.hour < 10:
            hh = '0'+str(self.hour)
        else:
            hh = str(self.hour)
        if self.min < 10:
            mm = '0'+str(self.min)
        else:
            mm = str(self.min)
        if self.sec < 10:
            ss = '0'+str(self.sec)
        else:
            ss = str(self.sec)
        return hh+':'+mm+':'+ss
        
    def next_second(self):
        self.sec += 1
        if self.sec > 59:
            self.sec = 0
            self.min += 1
        if self.min > 59:
            self.min = 0
            self.hour += 1
        if self.hour > 23:
            self.hour = 0

    def prev_second(self):
        if self.sec == 0:
            self.sec = 59
            if self.min == 0:
                self.min = 59
                if self.hour ==0:
                    self.hour = 23
                else:
                    self.hour -= 1
            else:
                self.min -=1
        else:
            self.sec -= 1
        

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
