import os
os.system("")

class Highlight():
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    RED = '\033[31m'
    WHITE = '\033[37m'

class Replace():

    def replace_to_ascii(cipher_text):
        cipher_text = cipher_text.replace("\\x00", "\x00")
        cipher_text = cipher_text.replace("\\x01", "\x01")
        cipher_text = cipher_text.replace("\\x02", "\x02")
        cipher_text = cipher_text.replace("\\x03", "\x03")
        cipher_text = cipher_text.replace("\\x04", "\x04")
        cipher_text = cipher_text.replace("\\x05", "\x05")
        cipher_text = cipher_text.replace("\\x06", "\x06")
        cipher_text = cipher_text.replace("\\x07", "\x07")
        cipher_text = cipher_text.replace("\\x08", "\x08")
        cipher_text = cipher_text.replace("\\t", "\t")
        cipher_text = cipher_text.replace("\\n", "\n")
        cipher_text = cipher_text.replace("\\x0b", "\x0b")
        cipher_text = cipher_text.replace("\\x0c", "\x0c")
        cipher_text = cipher_text.replace("\\r", "\r")
        cipher_text = cipher_text.replace("\\x0e", "\x0e")
        cipher_text = cipher_text.replace("\\x0f", "\x0f")
        cipher_text = cipher_text.replace("\\x10", "\x10")
        cipher_text = cipher_text.replace("\\x11", "\x11")
        cipher_text = cipher_text.replace("\\x12", "\x12")
        cipher_text = cipher_text.replace("\\x13", "\x13")
        cipher_text = cipher_text.replace("\\x14", "\x14")
        cipher_text = cipher_text.replace("\\x15", "\x15")
        cipher_text = cipher_text.replace("\\x16", "\x16")
        cipher_text = cipher_text.replace("\\x17", "\x17")
        cipher_text = cipher_text.replace("\\x18", "\x18")
        cipher_text = cipher_text.replace("\\x19", "\x19")
        cipher_text = cipher_text.replace("\\x1a", "\x1a")
        cipher_text = cipher_text.replace("\\x1b", "\x1b")
        cipher_text = cipher_text.replace("\\x1c", "\x1c")
        cipher_text = cipher_text.replace("\\x1d", "\x1d")
        cipher_text = cipher_text.replace("\\x1e", "\x1e")
        cipher_text = cipher_text.replace("\\x1f", "\x1f")
        cipher_text = cipher_text.replace("\\x7f", "\x7f")
        cipher_text = cipher_text.strip("''")
        return cipher_text