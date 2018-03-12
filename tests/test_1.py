import pytest
import sys
sys.path.append('/Users/m_631675/ethereum/cryptopals')

from cryptopals.one import (
    convert_hex_to_base64,
    fixed_xor,
    single_byte_xor,
    detect_single_byte_xor,
    repeating_key_xor,
    get_hamming_distance,
    keysize,
)

def test_convert_hex_to_base64():
    hexstr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    actual = convert_hex_to_base64(hexstr) 
    assert actual == expected

def test_fixed_xor():
    feeder = '1c0111001f010100061a024b53535009181c'
    against = '686974207468652062756c6c277320657965'
    expected = '746865206b696420646f6e277420706c6179'
    actual = fixed_xor(feeder, against)
    assert actual == expected

def test_single_byte_xor():
    hexstr = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    expected = "Cooking MC's like a pound of bacon"
    actual = single_byte_xor(hexstr)
    assert actual == expected

def test_detect_single_byte_xor():
    path = 'cryptopals/resources/single_char_xor.txt'
    actual = detect_single_byte_xor(path)
    expected = "Now that the party is jumping\n"
    assert actual == expected

def test_repeating_key_xor():
    str1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    actual = repeating_key_xor(str1, key)
    assert actual == expected


def test_get_hamming_distance():
    first = 'this is a test'
    second = 'wokka wokka!!!'
    assert get_hamming_distance(first, second) == 37

def test_keysize():
    assert keysize() is 1

