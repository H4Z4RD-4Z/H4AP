#!/usr/bin/python3

import time
import os

for i in range(10):
    time.sleep(5)
    os.system('ettercap -p -u -T -q -i at0')
