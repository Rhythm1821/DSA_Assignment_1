def push_zero_back(arr):
    for num in arr:
        if num==0:
            arr.remove(num)
            arr.append(0)
        else:
            continue
    return arr

print(push_zero_back([0,1,0,3,12]))