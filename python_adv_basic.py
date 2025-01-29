# list compherension
list_range=list(range(0,10,2))
print(list_range)
a=[i if i%2==0 else 'odd' for i in range(0,10)]
print(a)

#generator
lis_gen=(i**2 for i in range(10) if i%2 == 0) #generator can be used only ones
print(lis_gen)
b=[i+4 for i in lis_gen]
print (b)

# lamba, expression map and zip function

# filter
def mul_3(x):
    return x%3==0

l=range(10)
a=list(filter(mul_3,l))
print(a)

# lambda
afunc= lambda x:x+1
print(afunc(1))

af=list(filter(lambda x:x%3==0,l))

print(af)

mf=list(map(lambda x:x**2,l))

print(mf)

players=['teja','anu','Raghu','sunitha']

score=[25,21,56,46,8]

for i,j in zip(players,score):
    print(i,j)
# enumuerate
el=list(enumerate(players))
et=list(enumerate(players))

print(el)
print(et)

for i,k in enumerate(players):
    print(i,k)
#High order function
def hf(func,a):
    return func(a)

print(hf(lambda x:x**2,8))