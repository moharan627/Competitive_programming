class Comb(limit = 200_020,_mod = 10**9+7):
    def __init__(self, limit:int,_mod:int):
        self.mod = _mod
        self.Fact = [0] * limit
        self.Fact[0] = 1
        self.Fact[1] = 1
        for n in range(2, limit):
            self.Fact[n] = (n * (self.Fact[n - 1])) % self.mod
    def __modinv__(self,x):
        return pow(x, self.mod - 2, self.mod)
    def nCk(self,n:int,k:int):
        return self.Fact[n] * self.modinv(self.Fact[n-k] * self.Fact[k])
"""
使用例
comb = Comb(200020, 998244353)
comb.nCk(N,k)
"""
