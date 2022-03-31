#エラトスメネスで先に素数とって、それで素因数分解するだけ
#O(√N)よりかは定数倍程度早い
class little_fast_prime_factorize:
    def __init__(self,MAX = 10**6):
        self.Prime = [True for i in range(MAX)]
        self.Prime[0] = False
        self.Prime[1] = False
        for i in range(2, MAX):
            if (self.Prime[i]):
                for j in range(2 * i, MAX, i):
                    self.Prime[j] = False
        self.PrimeNum = []
        for i in range(2, MAX):
            if (self.Prime[i]):
                self.PrimeNum.append(i)
    def prime_factorize(self,num):
        a = []
        while num % 2 == 0:
            a.append(2)
            num //= 2
        f = self.PrimeNum[0]
        Index = 1
        while f * f <= num:
            if num % f == 0:
                a.append(f)
                num //= f
            else:
                f = self.PrimeNum[Index]
                Index += 1
        if num != 1:
            a.append(num)
        return a
#AC例：https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=6443891