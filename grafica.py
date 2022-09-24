import math

class calc:
    def __init__(self, num, num2):
        self.num  = float(num)
        self.num2 = float(num2)
        
    def sum_numbs(self):
        res = self.num + self.num2
        print('res: ', res)
    
    
class cadv(calc):
    def __init__(self, num, num2):
        super().__init__(num, num2)
    
    def sum_numbs(self):
        pass
    
    def ssqrt(self):
        res = math.sqrt(self.num)
        print('raiz: ', res)


op  = calc(3,4)
op2 = cadv(7,4)
op.sum_numbs()

op2.sum_numbs()
op2.ssqrt()
