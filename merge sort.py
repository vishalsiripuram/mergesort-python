def merge(arr):
    print('split:',arr)
    if len(arr)>1:
        mid=len(arr)//2
        leftarr=arr[:mid]
        rightarr=arr[mid:]
        merge(leftarr)
        merge(rightarr)
        i=j=k=0
        while i<len(leftarr) and j<len(rightarr):
            if leftarr[i]<rightarr[j]:
                arr[k]=leftarr[i]
                k+=1
                i+=1
            else:
                arr[k]=rightarr[j]
                k+=1
                j+=1
        while i<len(leftarr):
            arr[k]=leftarr[i]
            k+=1
            i+=1
        while j<len(rightarr):
            arr[k]=rightarr[j]
            k+=1
            j+=1
    print("sorted :",arr)
arr=[23,45,21,5,6]
merge(arr)
