def priority(arr):
    priority_map={}
    result=[]
    priority=1

    for num in arr:
        if num not in priority_map:
            priority_map[num]=priority
            priority+=1
           
        result.append(priority_map[num])
    print(priority_map)
    return result
N=10
arr=[1,2,7,3,4,5,6,3,7,1]
o=priority(arr)
print(o)



    