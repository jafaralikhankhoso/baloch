import os, sys

try:

    __import__("baloch").bnsbuy()

except Exception as e:

    exit(str(e))

