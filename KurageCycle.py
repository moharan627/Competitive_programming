class KurageCylce:
    def __init__(self,op,_StateNum=10**6):
        self.op = op
        _StateNum += 1
        self.StateNum = _StateNum
    def getitem(self,x):#最大計算量はO(状態数)
        Flag = [0]*self.StateNum
        Leg_Body = []
        while(1):
            if Flag[x]:
                Body_1 = x
                break
            Flag[x] = 1
            Leg_Body.append(x)
            x = self.op(x)
        Leg_Len = 0
        Body_Len = 0
        for s in Leg_Body:
            if s == Body_1:
                BodyLen = len(Leg_Body)-Leg_Len
                break
            else:
                Leg_Len += 1
        Leg = Leg_Body[:Leg_Len]
        Body = Leg_Body[Leg_Len:]
        return Leg,Body
"""
kurage = KurageCylce(op)
leg,body = kurage.getitem(x)#xは初期状態
if K< len(leg):#Kが足より少ない場合

else:
    K-=len(leg)
    if K < len(body):#Kが胴体一周より少ない場合
        
    else:#Kが胴体一周より多い場合
        K %= len(body)
#AC例:https://atcoder.jp/contests/abc241/submissions/30562966
#https://atcoder.jp/contests/abc167/submissions/30562713
"""
