from binascii import unhexlify, hexlify, b2a_base64
from collections import Counter
import math

keywords=['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us']


def convert_hex_to_base64(hexstr):
    raw_bytes = unhexlify(hexstr)
    encoded_bytes = b2a_base64(raw_bytes)
    to_string = encoded_bytes.decode("utf-8")
    return to_string.rstrip("\n")

def fixed_xor(feeder, against):
    decoded_feeder = unhexlify(feeder)
    decoded_against = unhexlify(against)
    xor = bytes_xor(decoded_feeder, decoded_against)
    xor_hex = hexlify(xor)
    xor_text = xor_hex.decode('utf-8').rstrip("\n")
    return xor_text

def bytes_xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def single_byte_xor(hexstr):
    raw_bytes = unhexlify(hexstr)
    strings = (''.join(chr(num ^ key) for num in raw_bytes) for key in range(256))
    return max(strings, key=lambda s: s.count(' '))

def detect_single_byte_xor(path):
    strings = []
    with open(path) as f:
        for line in list(f):
            strings.append(single_byte_xor(line.rstrip("\n")))
    return max(strings, key=lambda s: count_words(s))

def count_words(xx):
    counter = 0
    for word in keywords:
        if word in xx:
            counter += 1
    return counter
    
def repeating_key_xor(string, key):
    thing = repeat_xor(string, key)
    return thing

def repeat_xor(string, key):
    adj_key = (key * (math.floor(len(string) / len(key)) + 1))[:-1]
    adj_bytes = adj_key.encode('utf-8')
    adj_string = string.encode('utf-8')
    xor = bytes_xor(adj_string, adj_bytes)
    value = hexlify(xor).decode('utf-8').rstrip("\n")
    print(value)
    return value

def get_hamming_distance(first, second):
    one = bytearray(first.encode('utf-8'))
    two = bytearray(second.encode('utf-8'))
    return sum(bin(i^j).count("1") for i,j in zip(one, two))

def keysize():
    for size in range(2,41):
        print(size)
        
