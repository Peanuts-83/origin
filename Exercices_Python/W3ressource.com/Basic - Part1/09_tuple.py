# -*-coding:latin-1 -*
import os # On importe le module os

exam_st_date = (11,12,2014)
print( "The examination will start from : %i/%i/%i"%exam_st_date)
print( f"The examination will start from : {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}")
t = exam_st_date
print(t)
print( "The examination will start from : ",t[0],t[1],t[2], sep = '/')



# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
