class Scan():
    def scan(self):
        print('scan() from Scan class')

class Print():
    def print(self):
        print('print() from Print class')

class Fax():
    def print(self):
        print('print() from Fax class')

    def send(self):
        print('send() from Fax class')

class MFD(Scan, Print, Fax):
    def __str__(self):
        print(self.__main())

MFD_SPF = MFD()
print(MFD_SPF.scan(), MFD_SPF.print(), MFD_SPF.send())



class Scan:
    def scan(self):
        print('scan() from Scan class')

class Print:
    def print(self):
        print('print() from Print class')

class Fax:
    def print(self):
        print('print() from Fax class')

    def send(self):
        print('send() from Fax class')

class MFD(Scan, Fax, Print):
    def __str__(self):
        print(self.__main())

MFD_SFP = MFD()
print(MFD_SFP.scan(), MFD_SFP.print(), MFD_SFP.send())
