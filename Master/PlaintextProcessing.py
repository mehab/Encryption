def processedText(dictionary,plainText,flag):
    zeroString=''
    binary=''
    binaryFinal=''
    zeros=''
    if flag==1:
        # conversion into binary string
        for character in plainText:
            digit=dictionary[character]
            while digit>0:
                binary+=str(digit%2)
                digit=digit//2
            if(len(binary)!=6):
                while(len(binary)!=6):
                    binary+='0'
            start=stop=None
            step=-1
            reverse_slice=slice(start,stop,step)
            binaryFinal+=binary [reverse_slice]
            binary=''
        print(binaryFinal)
        if len(binaryFinal)%12==0:
            print("perfect ")
        else:
            print("Padding with zeros")
            x=len(binaryFinal)
            print(x)
            while x%12!=0:
                zeroString=zeroString+'0'
                x=x+1
        zeroString+=binaryFinal
        print("The required plain text is :"+zeroString)
        print("The length of the plain text is:"+str(len(zeroString)))
    else:
        z=len(plainText)
        if(z%12!=0):
            while (z%12!=0):
                zeros+='0'
                z=z+1
        zeros+=plainText
        zeroString=zeros
    return zeroString
