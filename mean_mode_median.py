#Find Out Mean and Median and mode 


#mean
list1=[22,14,34,56,76,99,12,16,19]
mean=sum(list1)/len(list1)
print(mean)

#median
list2=[22,14,34,56,76,99,12,16,19]
list2.sort()

if len(list2) % 2==0:
    m1=list2[len(list2)//2]
    m2=list2[len(list2)//2-1]
    median=(m1+m2)/2
else:
    median=list2[len(list2)//2]
print(median)

#mode
list3=[22,14,34,56,76,99,12,16,19]
frequency={}

for i in list3:
    frequency.setdefault(i,0)
    frequency[i]+=1

frequent=max(frequency.values())
for i ,j in frequency.items():
    if j ==frequent:
        mode=i
print(mode)
