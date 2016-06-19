import random
from .models import Code


def code_new(canape, quantity):
    code_nums = []
    for serial in range(quantity):
        while(True):
            try:
                code_num = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
                Code.objects.get(code=code_num)
            except:
                code_nums.append(code_num)
                break
    return code_nums
