class TLogElement:
    """Базовый класс для логического элемента."""
    def __init__(self):
        self.__in1 = 0
        self.__in2 = 0
        self._res = 0
        if hasattr(self, '_calk'):
            pass
        else:
            raise NotImplementedError('Невозжно создать такой объект!!!')

    def __setin1(self, newIn1):
        if newIn1 in (0, 1):
            self.__in1 = newIn1
            self._calk()

    def __setin2(self, newIn2):
        if newIn2 in (0, 1):
            self.__in2 = newIn2
            self._calk()

    In1 = property(lambda x: x.__in1, __setin1)
    In2 = property(lambda x: x.__in2, __setin2)
    Res = property(lambda x: x._res)


class Tnot(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calk(self):
        self._res = int(not(self.In1))


class Tand(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calk(self):
        self._res = self.In1 * self.In2


class Tor(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calk(self):
        if self.In1 + self.In2 == 0:
            self._res = 0
        else:
            self._res = 1


class Tequalence(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calk(self):
        if self.In1 == self.In2:
            self._res = 1
        else:
            self._res = 0


class TNand(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calk(self):
        self._res = int(not(self.In1 * self.In2))


class TNor(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calk(self):
        if self.In1 + self.In2 == 0: self._res = 1
        else: self._res = 0


class Txor(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calk(self):
        if self.In1 == self.In2:
            self._res = 0
        else:
            self._res = 1

class Timp(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calk(self):
        if self.In1 <= self.In2: self._res = 1
        else: self._res = 0


class TTrigger(TLogElement):
    def __init__(self, q):
        TLogElement.__init__(self)
        self.q = q


# print('IN1 In2 Res')
# trigger = Tor()
# for i in 0, 1:
#     for j in 0, 1:
#         trigger.In1 = i
#         trigger.In2 = j
#         print(i, j, trigger.Res, sep='   ')

