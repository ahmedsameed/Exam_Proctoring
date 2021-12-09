take=[]
recieve=[]
t=int(input("Press 1 after taking order "))
#while k<1000:
count=0
def first(l):
  global count
  if t==1:
    count+=1
    l.append(count)

  return(l)
#if t==1:
 #print(first(take))

r=int(input("Press 2 after delivering order "))
def rec():
   if r==2:
       recieve.append(take.pop())
   return(recieve)
#print(rec())
first(take);
#first(take) ;first(take) ; first(take) ;first(take) ;first(take)
#rec()

print("first:", first(take))
#print('recieve:',rec())
rec()
print("first:", take)
print('recieve:',rec())