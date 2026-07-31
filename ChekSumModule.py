import hashlib

def CalculateCheckSum(FilName):
    fobj = open(FilName,"rb")# any type of file can be handle  # read mode with binary format 

    hobj = hashlib.md5() # md5 obj frommdf class

    Buffer = fobj.read(1024) # byte

    while (len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    
    fobj.close()

    return hobj.hexdigest() # checksum return by this algorithm 



