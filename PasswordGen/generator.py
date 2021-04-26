import string
from random import randint as e
import random as r


class Passgen:

    def __init__(self):
        self.gen = 0

    def generate_password(self):
        while len(passwordStore) < 16:
            for elem in nums_list:
                passwordStore.append(elem)
            for elem in passSymbs:
                passwordStore.append(elem)
            for elem in lwc_list:
                passwordStore.append(elem)
            for elem in upc_list:
                passwordStore.append(elem)

        r.shuffle(passwordStore)

    def generate_nums(self):
        pass_rand = [e(0, 9) for i in range(4)]

        for elem in pass_rand:
            nums_list.append(elem)

    def generate_sym(self):
        passwordSymbols = ['@', '#', '$', '%',
                           '&', '(', ')', '[', ']', '/', '^', '!']
        r.shuffle(passwordSymbols)

        for elem in range(4):
            new_pass_sym = passwordSymbols[elem]
            passSymbs.append(new_pass_sym)

    def generate_lower_case(self):
        lwc = string.ascii_lowercase

        lwc_2 = [i for i in lwc]
        r.shuffle(lwc_2)

        for elem in range(4):
            new_lwc = lwc_2[elem]
            lwc_list.append(new_lwc)

    def generate_upper_case(self):
        upc = string.ascii_uppercase

        upc_2 = [i for i in upc]
        r.shuffle(upc_2)

        for elem in range(4):
            new_upc = upc_2[elem]
            upc_list.append(new_upc)


passwordStore = []
nums_list = []
passSymbs = []
lwc_list = []
upc_list = []
Password = Passgen()
