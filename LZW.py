def encodeLZW(S):
    S = input()
    A = []
    B = []
    for i in range(0, len(S)):
        if S[i] not in A:
            A.append(S[i])
            B.append(S[i])
    ans = []
    st = ''
    for i in range(0, len(S)):
        st += S[i]
        if st not in A:
            A.append(st)
            a = len(st)
            ans.append(A.index(st[:-1]))
            st = st[-1]
    ans.append(A.index(st))
    print(ans)    
def decodeLZW(A,ans):
    dec = ''
    st = ''
    for i in range(0, len(ans)):
        if len(A[ans[i]]) == 1:
            dec += A[ans[i]]
            if dec not in A:
                A.append(dec)
                st += dec[:-1]
                print(dec)
                dec = dec[-1]        
        else:
            for j in range(0, len(A[ans[i]])):
                dec += A[ans[i]][j]
                if dec not in A:
                    A.append(dec)
                    st += dec[:-1]
                    print(dec)
                    dec = dec[-1]            
    st+=dec
    print(st)    