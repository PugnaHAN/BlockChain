from Code.CodeBase import CodeBase

class Caesar(CodeBase):

    @staticmethod
    def encryption(message, key = 3):
        if isinstance(message, str):
            message = message.lower()
            for i in range(len(message)):
                ch = ord(message[i]) + key
                if ch <= ord('z') and message[i] != ' ':
                    c = chr(ch)
                elif message[i] != ' ':
                    c = chr(ch - 26)
                else:
                    c = ' '
                message = message[:i] + c + message[i + 1:]
            return message
        else:
            raise TypeError("Plain text is not a string!")

    @staticmethod
    def decryption(cipher, key = 3):
        message = cipher
        if isinstance(message, str):
            for i in range(len(message)):
                ch = ord(message[i]) - key
                if message[i] != ' ':
                    if ch >= ord('a'):
                        c = chr(ch)
                    else:
                        c = chr(ch + 26)
                else:
                    c = ' '
                message = message[:i] + c + message[i+1:]
            return message
        else:
            raise TypeError("Cipher is not a string!")


if __name__ == "__main__":
    for i in range(26):
        print("cipher is {}".format(Caesar.encryption('PELCGBTENCUL', i)))