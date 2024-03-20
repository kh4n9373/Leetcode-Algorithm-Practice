arr = [5,5,4]
k = 1
dic = {n:0 for n in set(arr)}
for i in range(len(arr)):
    dic[arr[i]] += 1
queue = sorted(dic,key=lambda x:dic[x])
while k > 0:
    v = queue.pop(0)
    k -= dic[v]
if k < 0:
    print(len(queue)+1)
else:
    print(len(queue))