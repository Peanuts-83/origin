from os import strerror

# samplefile.txt created

file = open('samplefile.txt', 'wt')
file.write('John	Smith	5\n\
Anna	Boleyn	4.5\n\
John	Smith	2\n\
Anna	Boleyn	11\n\
Andrew	Cox	1.5')
file.close()


class StudentsDataException(Exception):
    def __init__(self,message):
        super().__init__(message)


class BadLine(StudentsDataException):
    def __init__(self,message,line):
        super().__init__(message)
        self.line = line
    

class FileEmpty(StudentsDataException):
    def __init__(self,message,file):
        super().__init__(message)
        self.file = file


# Read and concatenate samplefile.txt

try:
    file = open('samplefile.txt', 'rt')
    dico = dict(); count = 0
    for line in file.readlines():
        if len(line) == 0:
            raise FileEmpty("is empty", file.name)
        count += 1
        name = ' '.join((line.split())[:-1])
        note = ''.join((line.split())[-1])
        try:
            note = float(note)
        except ValueError:
            raise BadLine(f"Line # {count}: invalid note", count)
        if name in dico.keys():
            dico[name] += float(note)
        else:
            dico[name] = float(note)
    for k,v in dico.items():
        print(k,':',v)
except BadLine as bd:
    print('Error processing data in line #', bd.line, "- bad digit value")
except FileEmpty as fe:
    print('Error getting data : ', fe.file, fe)
except FileNotFoundError as fnfe:
    print("Exception raised : ", fnfe)
    