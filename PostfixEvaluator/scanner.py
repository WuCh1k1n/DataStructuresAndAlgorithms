from tokens import Token


class Scanner(object):

    def __init__(self, sourceStr):
        self._str = sourceStr
        self._position = 0

    def hasNext(self):
        if self._position < len(self._str):
            return True
        else:
            return False

    def next(self):
        if not self.hasNext():
            raise AttributeError("The string doesn't contain another token.")
        nextToken = Token(self._str[self._position])
        self._position += 1
        return nextToken
