from __future__ import print_function, division
from thinkbayes2 import Pmf

# 曲奇饼问题
# 有两碗曲奇饼
# 碗一包含30个香草曲奇饼和10个巧克力曲奇饼
# 碗二有上述两种饼干各20个
# 随机的挑一个碗拿一块饼，得到了一块香草曲奇饼。
# 从碗一取到香草曲奇饼的概率是多少？
'''
pmf = Pmf()
# 先验分布，取碗的概率各是0.5
pmf.Set('Bowl 1', 0.5)
pmf.Set('Bowl 2', 0.5)

# 似然度
# 从碗一拿到香草曲奇饼的概率是3/4
# 从碗二拿到香草曲奇饼的概率是1/2
pmf.Mult('Bowl 1', 0.75)
pmf.Mult('Bowl 2', 0.5)

# 归一化
pmf.Normalize()

print(pmf.Prob('Bowl 1'))
'''


# 贝叶斯框架
class Cookie(Pmf):
    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            # print(like, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    mixes = {
        'Bowl 1': dict(vanilla=0.75, chocolate=0.25),
        'Bowl 2': dict(vanilla=0.5, chocolate=0.5),
    }

    def Likelihood(self, date, hypo):
        mix = self.mixes[hypo]
        like = mix[date]
        return like


hypos = ['Bowl 1', 'Bowl 2']
mypmf = Cookie(hypos)
mypmf.Update('vanilla')

for hypo, prob in mypmf.Items():
    print(hypo, prob)