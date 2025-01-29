a=5 

if a==5:
   print('hello world')
else:
   print('a is not equal to 5')

a=10

if a<5:
   print('a is less than 5')
elif a==10:
   print('a is 10')
else:
   print('a is greater than 5')

a=5
# ternary operator
res= 'a<10' if a<10 else 'a>10' 

print(res)

# greet function

def greet():
   print('greet')
   return 'this is greet function'


def wish():
   return 'wish'


res=greet() if a<10 else wish()

greet() if a<10 else wish()

print(res)

i=0
while i<5:
    #print(i)
    i=i+1

i=5

while True:
   print(i)
   if i<=5:
      break
   
# use of loops

#loop with else statement
i=0
while i<10:
   print(i)
   i+=1
else:
   print('loop is completed')   

l=[1,2,3,4,5]
val=10
found=False
i=0
while i<len(l):
   if l[i]==val:
      found=True
      break
   i+=1

"""
if not found:
   print('not found')
else:
   print('found')
"""
i=0

while(i<len(l)):
   if(l[i]==val):
      #found=True
      break
   i+=1
else:
  l.append(val)

# for loop

for i in range(5,0,-1):
   print(i)

for c in "hello":
   print(c)
for i in l:
   print(i,end=' ')   
print()
for i,*j in [(1,12),(2,9,8),(3,9)]:
   print(i,j)