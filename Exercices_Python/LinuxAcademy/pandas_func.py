import pandas as pd

data = [
     ("Dexter","Johnsons","dog","shiba inu","red sesame",1.5,35,"m",False,"both",True),
     ("Alfred","Johnsons","cat","mix","tuxedo",4,12,"m",True,"indoor",True),
     ("Petra","Smith","cat","ragdoll","calico",None,10,"f",False,"both",True),
     ("Ava","Smith","dog","mix","blk/wht",12,32,"f",True,"both",False),
     ("Schroder","Brown","cat","mix","orange",13,15,"m",False,"indoor",True),
     ("Blackbeard","Brown","bird","parrot","multi",5,3,"f",False,"indoor",),
 ]
labels = ["name","owner","type","breed","color","age","weight","gender","health issues","indoor/outboor","vaccinated"]

# Construction et analyse
vet_records = pd.DataFrame.from_records(data, columns=labels)
# >>> print(vet_records)
#          name     owner  type      breed       color   age  weight gender  health issues indoor/outboor vaccinated
# 0      Dexter  Johnsons   dog  shiba inu  red sesame   1.5      35      m          False           both       True
# 1      Alfred  Johnsons   cat        mix      tuxedo   4.0      12      m           True         indoor       True
# 2       Petra     Smith   cat    ragdoll      calico   NaN      10      f          False           both       True
# 3         Ava     Smith   dog        mix     blk/wht  12.0      32      f           True           both      False
# 4    Schroder     Brown   cat        mix      orange  13.0      15      m          False         indoor       True
# 5  Blackbeard     Brown  bird     parrot       multi   5.0       3      f          False         indoor       None
vet_records.head() ; vet_records.tail()
vet_records.dtypes ; vet_records.type.count()
vet_records.vaccinated ; vet_records.vaccinated.count()
vet_records.groupby('type').count()
vet_records.type.value_counts()

# Slice & Dice
#sauvegarde! 
vet_records_archive = vet_records

weight = vet_records['weight'] ; dog_weight = vet_records.weight[vet_records.type=='dog']

# loc & iloc (label et index)
vet_records.loc[:,["name", "owner"]] ; vet_records.loc[2:3,["name", "owner"]]
vet_records.iloc[[2,3],[4,5]]

# isin (~ pour isnotin)
vet_records[vet_records.name.isin(['Dexter','Blackbeard'])] ; vet_records[~vet_records.name.isin(['Dexter','Blackbeard'])]

# Pivot table
table = pd.pivot_table(vet_records, values=['weight', 'age'], index=['type', 'breed'], aggfunc=sum)
import numpy as np
table2 = pd.pivot_table(vet_records, values=['weight', 'age'], index=['type', 'breed'], aggfunc=np.mean)

# Stats
vet_records.describe()
missing_data = vet_records.isna() # check for missing data
vet_records_value = vet_records.fillna(0) ; vet_records_value # replace md by value
values = {"age": 12, "vaccinated": False} ; vet_records_dict = vet_records.fillna(value=values) ; vet_records_dict # replace md by values in dict
