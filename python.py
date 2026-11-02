# input: the boy is a good boy
# op:the boy is a good boy

# a='@the# @boy# #is# @a@ $good$ %Boy%'
# b=''
# s=a.lower().split()
# print(s)

# for i in range(len(s)):
#     if(s[i].lower() not in b):
#         b+=s[i].lower()
    
#         count=0
#         for j in range(0,len(s)):
       
        
#             if s[i].lower()==s[j].lower():
#                 count+=1
       
#         print(s[i],':',count)
        
            
# for i in a:
#     if i.isalpha() or  '':
#            b+=i
# print(b)


a='karthikra   ja'
b=''
for i in a:
    if i not in 'aeiouAEIOU@!%&':
        if i not in b:
            b+=i
print(b)


a=int(input('enter the num to find second largest'))
temp=a
lar=0
slar=0
while temp>0:
    l=temp%10
    if l>lar:
        lar=l
    if l>slar and l<lar:
        slar=l
    temp=temp//10
print(slar)


d={'karthik':24,'isham':22,'ragu':22,'praveen':22,'sanjay':25}
r={}
for i in d:
    if d[i] not in r:
        r[d[i]]=[i]
    else:
        r[d[i]]+=[i]
print(r)

def rev(a):
    b=''
    for i in a:
        b=i+b
    return b
a=input('enter a string to reverse')
print(rev(a))

m=[[1,2,3],[4,5,6],[7,8,9]]
def row(n):
    
    return m[n]

def col(n):
    l=[]
    for i in range(len(m)):
        l+=[m[i][n]]
        
    return l
print(row(2))
print(col(0))
    