import random
from .models import Code
from account.models import User


def generate_code_string(canape, quantity):
    code_strings = []
    for _ in range(quantity):
        while(True):
            try:
                code_string = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
                Code.objects.get(code=code_string)
            except:
                code_strings.append(code_string)
                break
    return code_strings


def generate_code(canape, quantity):
    code_string = generate_code_string(canape, quantity)
    next_serial = Code.objects.filter(canape=canape).count()
    for serial, code_string in enumerate(code_string):
        serial += next_serial + 1
        Code.objects.create(canape=canape, code=code_string, serial=serial)


def distribute_code(canape, emails):
    if canape.is_limit:
        codes = Code.objects.filter(canape=canape, gainer=None)
        if len(emails) > codes.count():
            raise   # 개수보다 많은 이메일이 입력됨.
    else:
        generate_code(canape, len(emails))
        codes = Code.objects.filter(canape=canape, gainer=None)

    for email in emails:
        try:
            user = User.objects.get(email=email)
            code = codes.order_by("?").first()
            code.gainer = user
            code.save()
            codes = codes.filter(gainer=None)
        except:
            # email 전송
            continue
