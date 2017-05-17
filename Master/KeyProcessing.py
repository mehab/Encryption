def BitKey(key):
    bitKeyR=''
    bitKey=''
    start=stop=None
    step=-1
    reverse_slice=slice(start,stop,step)
    while key>0:
        bitKeyR+=str(key%2)
        key=key//2
    if(len(bitKeyR)!=9):
        while len(bitKeyR)!=9:
            bitKeyR+='0'
    bitKey=bitKeyR[reverse_slice]
    print("The required key is :"+bitKey)
    return bitKey
