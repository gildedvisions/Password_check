def passwordcheck(password):

    pwd = password

    J, K, L, M = 0, 0, 0, 0

    if len(pwd) < 5:
        return("Password length must be greater than 4 characters")
    for i in pwd: 
        if ('a' <= i ) and (i <= 'z'):
            J =+ 1
    for i in pwd:
        if ('A' <= i ) and (i <= 'Z'):
            K =+ 1
    for i in pwd:
        if ('0' <= i) and (i <= "9"):
            L =+ 1
    for i in pwd:
        if ('!' <= i) and (i <= "/") or (':' <= i) and (i <= "@"):
            M =+ 1

    if J == 0:
        return('Password requires atleast 1 lowercase Character')
    if K == 0:
        return('Password requires atleast 1 Capital letter')
    if L == 0:
        return('Password requires atleast 1 number number')
    if M == 0:
        return('Password requires atleast 1 special charcater')
    if (J>0 and K>0 and L>0 and M>0):
        return('Success')    
    
        
