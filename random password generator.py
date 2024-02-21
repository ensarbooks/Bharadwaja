import random
# up_case=['A','B','C','D']
# low_case=['a','b','c','d']
# numbers=['1','2','3','4']
# special_char=['@','$','%','#']

# pwd=random.choice(up_case)+random.choice(low_case)+random.choice(numbers)+random.choice(special_char)

# print("My pwd is \n",pwd)


strng='hello ensar this is bharadwaja iam generating Readable password generator program using python langauage.so please generate my new password '
l=[]
for i in strng.split():
    if len(i)>4:
        l.append(i.capitalize())
word=random.choice(l)
sp_ch=random.choice(['@','#','$','&'])
nos=random.randint(1,10)
passwd=word+sp_ch+str(nos)
print('Readable password is \n',passwd)