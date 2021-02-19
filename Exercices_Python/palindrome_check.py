say = input("Enter a palindrome : ")
say = ''.join(say.split())
if len(say)%2 == 0:
    print("Not a Pal")
for i in range(len(say)//2):
    print(say[i],say[-i-1])
    if say[i] != say[-i-1]:
        print("Not at all!!!")
        exit()
print("Yes it is")
exit()