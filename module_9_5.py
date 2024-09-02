print('\033[30m\033[47mДомашнее задание по теме "Итераторы""\033[0m')
print('\033[30m\033[47mЗадача "Range - это просто":\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()


class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step > 0 and self.pointer > self.stop or self.step < 0 and self.pointer < self.stop:
            raise StopIteration
        set_pointer = self.pointer
        self.pointer += self.step
        return set_pointer


# Пример выполняемого кода:
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
print(thanks)
