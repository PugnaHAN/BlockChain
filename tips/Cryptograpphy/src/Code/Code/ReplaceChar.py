from Code.CodeBase import CodeBase

class ReplaceChar(CodeBase):
    __key__ = {'a': 'c', 'b': 'e', 'c': 'g', 'd': 'i', 'e': 'k', 'f': 'm', 'g': 'o',
               'h': 'q', 'i': 's', 'j': 'u', 'k': 'w', 'l': 'y', 'm': 'a', 'n': 'b',
               'o': 'z', 'p': 'x', 'q': 'v', 'r': 'd', 's': 'f', 't': 'h',
               'u': 'j', 'v': 'l', 'w': 'n', 'x': 'o', 'y': 'p', 'z': 't', ' ': ' '}

    @staticmethod
    def encryption(plain, key = __key__):
        message = list()
        if isinstance(key, dict):
            for c in plain.lower():
                message.append(key[c])
            return "".join(message)
        else:
            raise TypeError("Key is not a table!")

    @staticmethod
    def decryption(cipher, key = __key__):
        message = list()
        if isinstance(key, dict):
            for c in cipher.lower():
                for k in key:
                    if key[k] == c:
                        message.append(k)
                        break
            return "".join(message)
        else:
            raise TypeError("Key is not a table!")

    @staticmethod
    def statistical(message):
        message = str(message).lower()
        counter = dict()
        for c in message:
            if c in counter.keys():
                counter[c] += 1
            else:
                counter[c] = 1
        for ch in counter.keys():
            counter[ch] = (counter[ch], float("%.3f"%(counter[ch] / len(message))))
        return counter

if __name__ == "__main__":
    key = {
        'a': 'w', 'b': 'y', 'c': 'h', 'd': 'f', 'e': 'x', 'f': 'u', 'g': 'm',
        'h': 't', 'i': 'j', 'j': 'v', 'k': 's', 'l': 'g', 'm': 'e', 'n': 'n',
        'o': 'b', 'p': 'r', 'q': 'd' ,'r': 'z', 's': 'l', 't': 'q',
        'u': 'a', 'v': 'p', 'w': 'c', 'x': 'o', 'y': 'k', 'z': 'i'
    }
    print("cipher of {} is {}".format('yoshiko',
                                      ReplaceChar.encryption('yoshiko', key)))
    message = \
    """
    MEYLGVIWAMEYOPINYZGWYEGMZRUUYPZAIXILGVSIZZMPGKKDWOMEPGROEIWGPCEIPAMDKKEYCIUYMGIF
    RWCEGLOPINYZHRZMPDNYWDWOGWITDWYSEDCEEIAFYYWMPIDWYAGTYPIKGLMXFPIWCEHRZMMEYMEDWOMG
    QRYWCEUXMEDPZMQRGMEEYAPISDWOFICJILYSNICYZEYMGGJIPRWIWAIHRUNIWAHRZMUDZZYAMEYFRWCE
    MRPWDWOPGRWAIOIDWSDMEIGWYMSGMEPYYEYHRUNYARNFRMSDMEWGOPYIMYPZRCCYZZIOIDWIWAIOIDWE
    YMPDYAILMYPMEYMYUNMDWOUGPZYKFRMIMKIZMEIAMGODTYDMRNIWASIKJYAISIXSDMEEDZWGZYDWMEYI
    DPZIXDWODIUZRPYMEYXIPYZGRPDMDZYIZXMGAYZNDZYSEIMXGRCIWWGMOYM
    """
    print(ReplaceChar.statistical(message))