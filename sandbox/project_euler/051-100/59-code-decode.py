###############################################################################
# 59-code-decode.py
#
# Each character on a computer is assigned a unique code and the preferred
# standard is ASCII (American Standard Code for Information Interchange). For
# example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII
# then XOR each byte with a given value, taken from a secret key. The advantage
# with the XOR function is that using the same encryption key on the cipher text
# restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text
# message, and the key is made up of random bytes. The user would keep the
# encrypted message and the encryption key in different locations, and without
# both "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified
# method is to use a password as a key. If the password is shorter than the
# message, which is likely, the key is repeated cyclically throughout the
# message. The balance for this method is using a sufficiently long password
# key for security, but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower
# case characters. Using 59-cipher.txt, a file containing the encrypted ASCII
# codes, and the knowledge that the plain text must contain common English
# words, decrypt the message and find the sum of the ASCII values in the
# original text.
###############################################################################
decimalList = []
charList = []
binaryList = []
decodedBinaryList = []
decodedCharList = []
###############################################################################
def readFile():
    with open("59-cipher.txt",'r') as secretStuff:
        for everyThing in secretStuff:
            temp = everyThing.split(',')
            
    for i in range(len(temp)):
        decimalList.append(temp[i])
        charList.append(chr(int(temp[i])))
        binary = charToBinary(chr(int(temp[i])))
        binaryList.append(binary)
                        
################################################################################
def xOR(binary,key):
    newByte = ''
    for i in range(8):
        if binary[i] == key[i]:
            newByte += '0'
        else:
            newByte += '1'           
    return(newByte)   
################################################################################
def charToBinary(char):   
    decimal = ord(char)
    binary = ''   
    while True:
        if decimal == 0:
            break
        elif (decimal % 2) == 0:
            decimal = decimal // 2
            binary = '0' + binary
        else:
            decimal = decimal // 2
            binary = '1' + binary
    while len(binary) < 8:
        binary = '0' + binary       
    return binary
################################################################################
def binaryToCharacter(binary):   
    binary = binary[::-1]
    decimal = 0
    power = 0 
    for i in binary:
        decimal += int(i) * (2 ** power)
        power +=1       
    return chr(decimal) 
################################################################################
readFile()

for c0 in 'abcdefghijklmnopqrstuvwxyz':
    for c1 in 'abcdefghijklmnopqrstuvwxyz':
        for c2 in 'abcdefghijklmnopqrstuvwxyz':
            decodedBinaryList.clear()
            decodedCharList.clear()
            for index in range(len(binaryList)):
                if index % 3 == 0:
                    temp = xOR(binaryList[index],charToBinary(c0))
                elif index % 3 == 1:
                    temp = xOR(binaryList[index],charToBinary(c1))
                else:
                    temp = xOR(binaryList[index],charToBinary(c2))
                    
                decodedBinaryList.append(temp)
                decodedCharList.append(binaryToCharacter(temp))

            temp = ''.join(decodedCharList)   
            if 'the' in temp and 'and' in temp and 'of' in temp:
                print('--------------record start-------------',c0,c1,c2)
                print(temp)
    
###############################################################################
# solution: 129448
###############################################################################
