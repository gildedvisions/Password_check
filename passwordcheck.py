def passwordcheck(password):

    pwd = password

    # create am empty list to store the pwd fail conditioins. the conditionals will be appeneded and then joined to form a single result statment 
    ans = []
    ans1 = []
    coll = []

    J, K, L, M, N, O= 0, 0, 0, 0, 0, 0

    if len(pwd) < 7:
        N = "Password length must be greater than 7 characters. "
        ans1.append(N)
    for i in pwd:
        if ('A' <= i ) and (i <= 'Z'):
            K =+ 1
    for i in pwd:
        if ('a' <= i ) and (i <= 'z'):
            J =+ 1
    for i in pwd:
        if ('0' <= i) and (i <= "9"):
            L =+ 1
    for i in pwd:
        if ('!' <= i) and (i <= "/") or (':' <= i) and (i <= "@"):
            M =+ 1

    
    if (J == 0) or (K == 0) or (L == 0) or (M == 0):
        O = 'Password must contain atleast'
        coll.append(O)

    if J == 0:
        J = ' 1 uppercase character'
        ans.append(J)
        
    if K == 0:
        K = '1 lowercase character'
        ans.append(K)        
    if L == 0:
        L = ' 1 number'
        ans.append(L)
    if M == 0:
        M = ' 1 special charcater.'
        ans.append(M)
    # add commas between each fail condition 
    
    for i in range(len(ans)-2,0,-1):
        ans[i:i] = ','
    if len(ans) > 1:
        ans.insert(len(ans)-1, 'and')  

    if len(pwd) < 7:
        ans = ans1 + coll + ans
        ans = " ".join([str(item) for item in ans])
        return ans
    else:  
        ans = coll + ans
        ans = " ".join([str(item) for item in ans])
        return ans
    
    


    #if (J>0 and K>0 and L>0 and M>0):
    #   return('Success')    
    
        
