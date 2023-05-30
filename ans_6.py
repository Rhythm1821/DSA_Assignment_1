def arr_check(arr):
    for i in arr:
        if arr.count(i)>1:
            print(True)
            break
        else:
            if i!=arr[-1]:
                continue
            else:
                print(False)

arr_check([1,2,3,1])        