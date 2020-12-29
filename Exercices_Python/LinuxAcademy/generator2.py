file_name = 'LinuxAcademy/funds.txt'
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(',') for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)
funding = (int(raised_dict['raisedAmt']) 
for raised_dict in company_dicts 
if raised_dict['round'] == 'a')
total_a = sum(funding)

print(f'Total series A fundraising is ${total_a}.')
