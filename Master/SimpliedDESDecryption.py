
import string
import SimplifiedDES
import PlaintextProcessing
import KeyProcessing
import PlainTextInput
def SimpleDESDecrypt(rounds,cipherText,bitKey,S1,S2,reverse_slice):
    #region declaration
    output=''
    binaryxor=''
    binaryRight=''
    finalDecryptedString=''
    dictionary={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',\
            9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',\
            19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z',27:'0',28:'1',29:'2',30:'3',31:'4' \
            ,32:'5',33:'6',34:'7',35:'8',36:'9',37:' ',38:'.'}
     #endregion
    i=0
    r=int(rounds)-1
    while i<len(cipherText):
        pt=cipherText[i:i+12]
        i=i+12
        left=pt[:6]
        right=pt[6:]
        while(r>=0):
            if(r<2):
                uKey=bitKey[r:r+8]
            else:
                uKey=bitKey[r:]+bitKey[0:(8-len(bitKey[r:]))] #round key generation
            eOfR=right[0:2]+right[3]+right[2]+right[3]+right[2]+right[4:] #expansion of right part 
            eOfRXorKey=int(eOfR,2)^int(uKey,2) #xor of key and expanded right part
            #convert xor into bit string
            while eOfRXorKey>0:
                binaryxor+=str(eOfRXorKey%2)
                eOfRXorKey=eOfRXorKey//2
            if len(binaryxor)<8:
                while len(binaryxor)<8:
                    binaryxor+='0'
            binaryxorFinal=binaryxor [reverse_slice]
            nibbleL=binaryxorFinal[:4]
            nibbleR=binaryxorFinal[4:]
            #Computation of S box output
            S1Output=S1[nibbleL]
            S2Output=S2[nibbleR]
            SBoxOutput=S1Output+S2Output
            rightNextRound=int(SBoxOutput,2)^int(left,2)
            #convert right next round into bit string
            while rightNextRound>0:
                binaryRight+=str(rightNextRound%2)
                rightNextRound=rightNextRound//2
            if len(binaryRight)<6:
                while len(binaryRight)<6:
                    binaryRight+='0'
            binaryRightFinal=binaryRight [reverse_slice]
            left=right
            right=binaryRightFinal
            binaryxor=''
            binaryRight=''
            r=r-1
        finalDecryptedString+=right+left
        r=int(rounds)-1
    print("The final decrypted string is:"+finalDecryptedString)
    i=0
    while i<len(finalDecryptedString):
        current=finalDecryptedString[i:i+6]
        print("current part of the plain text is:"+current)
        output+=dictionary[int(current,2)]
        print("the current output string is:"+output)
        i=i+6
    return output

            
            
        


