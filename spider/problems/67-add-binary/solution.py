class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def v1(a,b):
            ma =  a if len(a)>len(b) else b
            mi = b if len(a)>len(b) else a
            mi = '0'*(len(ma)-len(mi))+mi
            tli=['0' for i in range(len(ma)+1)]
            for i in range(1,len(mi)+1):
                su= sum([int(mi[-i]),int(ma[-i]),int(tli[-i])])
                tli[-i]=str(su%2)
                tli[-i-1]=str(su//2)
            r = (''.join(tli))
            if not r:return''
            while len(r)>1 and r[0]=='0':r=r[1:]
            return r
        
        def v2(a,b):
            tli,a,b =  ([0]*(len(b)+1),b,a.zfill(len(b))) if len(a)<len(b) else ([0]*(len(a)+1), a,b.zfill(len(a)))
            for i in range(1,len(b)+1):
                su= sum([int(b[-i]),int(a[-i]),tli[-i]])
                tli[-i],tli[-i-1]=su%2, su//2
            return (''.join(map(str,tli))).lstrip('0') if ''.join(map(str,tli))!='00' else '0'       

        return "1" if {a, b} in [{"1", "0"}, {"1", ""}] else ("0" if {a, b} in [{"0", "0"}, {"0", ""}, {"", ""}] else ("10" if [a, b] == ["1", "1"] else self.addBinary(a[:-1], self.addBinary(b[:-1], "1" if a and b and [a[-1], b[-1]] == ["1", "1"] else "0")) + self.addBinary(a[-1] if a else "", b[-1] if b else "")[-1]))

        # plusone = lambda d:[1,0] if d==[1] else  plusone(d[:-1]) + [0] if d[-1]==1 else d[:-1] + [d[-1] + 1]
        # a=list(map(int,a))
        # for i,bit in enumerate(b[::-1]): 
        #     a= plusone(a[:len(a)-i])+a[len(a)-i:] if bit else a
        # return ''.join(map(str,a))

        #return v2(a,b)