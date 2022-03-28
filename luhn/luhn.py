import re
import math

class Luhn:
    min_lenght = 2
    
    def __init__(self, card_num):
        self.card_num = card_num
        # add and save total to avoid wrong secuencial call response
        self.total = self.sum_num(self.card_num)
    
    def valid(self):
        number = self.card_num.replace(' ','')
        if len(number) < self.min_lenght:
            return False
        if not number.isdigit():
            return False
        return self.total % 10 == 0
        

    def sum_num(self, number):
        number = re.sub('[^0-9]', '', self.card_num)
        numlist = [int(n) for n in reversed(str(number))]
        for n in range(1, len(numlist), 2):
            if (numlist[n] * 2) > 9:
                numlist[n] = numlist[n] * 2 - 9
            else:
                numlist[n] = numlist[n] * 2

        return sum(numlist)