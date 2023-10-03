#!/usr/bin/python3
# 2-print_alphabet.py

"""Print the lowercase alphabet without a newline character"""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
