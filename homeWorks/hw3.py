class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        mv = int(input('add money')) + self._balance
        return mv

    def _kill(self):
        zm = input('do you want to reset your money? type yes or no: ')
        if zm == 'yes':
            return f'your balance is {self._balance - self._balance}'
        elif zm == 'no':
            return 'good choice'
        else:
            return 'type only yes or no'


    def __jackpot(self):
        return f'your balance is {self._balance * 10}'

    def acj(self):
        return self.__jackpot()


    def _steal(self):
        return f'{self._name} stole your money and now has: {self._balance + akcha._balance}'



akcha = Bank('aizhan', 9999)
akcha2 = Bank('gru', 10)
print(akcha.moneyX())
print(akcha._kill())
print(akcha.acj())
print(akcha2._steal())