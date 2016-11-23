class CodeBase:
    def __init__(self):
        self.__encryption__ = self.encryption
        self.__decryption__ = self.decryption

    @staticmethod
    def encryption(message, key):
        return ""

    @staticmethod
    def decryption(message, key):
        return ""