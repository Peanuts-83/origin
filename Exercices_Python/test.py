import sys, os

print(sys.stdin,'\n', sys.stdout,'\n', sys.stderr)
sys.stdout.write('hello')
print('\n', os.getcwd())

file = open('temp_file.txt', 'w')
sys.stdout = file
print('I write in the file instead of stdout!')
file.close()

sys.stdout = sys.__stdout__
print('Now i can write on screen...')
