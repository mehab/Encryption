import string
import SimplifiedDES
import PlaintextProcessing
import KeyProcessing
import PlainTextInput
import SimpliedDESDecryption
#region declaration
binaryxor=''
binaryRight=''
finalEncryptedString=''
key=324
start=stop=None
step=-1
reverse_slice=slice(start,stop,step)
dictionary={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,\
            'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,\
            'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26,'0':27,'1':28,'2':29,'3':30,'4':31 \
            ,'5':32,'6':33,'7':34,'8':35,'9':36,' ':37,'.':38}
S1={'0000':'101','0001':'010','0010':'001','0011':'110','0100':'011'\
    ,'0101':'100','0110':'111','0111':'000','1000':'001','1001':'100',\
    '1010':'110','1011':'010','1100':'000','1101':'111','1110':'101','1111':'011'}
S2={'0000':'100','0001':'000','0010':'110','0011':'101','0100':'111'\
    ,'0101':'001','0110':'011','0111':'010','1000':'101','1001':'011',\
    '1010':'000','1011':'111','1100':'110','1101':'010','1110':'001','1111':'100'}
#endregion
plainText=PlainTextInput.InputText()
zeroString=PlaintextProcessing.processedText(dictionary,plainText,1)
rounds=int(input("Enter the number of rounds"))
#conversion of key into bitstring
bitKey=KeyProcessing.BitKey(key)
#applying the des algorithm

#def DESEBC(rounds,zeroString):
finalEncryptedString=SimplifiedDES.DESEBC(rounds,zeroString,bitKey,S1,S2,dictionary,reverse_slice)
print("The final encrypted string is:"+finalEncryptedString)
output=SimpliedDESDecryption.SimpleDESDecrypt(rounds,finalEncryptedString,bitKey,S1,S2,reverse_slice)
print("The decrypted string is:"+output)
