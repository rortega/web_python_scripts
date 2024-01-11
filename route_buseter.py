#!/usr/bin/env python3

import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument('-a','--actionlist', help='actionlist to use')
parser.add_argument('-t','--target',help='host/ip to target',required=True)
parser.add_argument('-w','--wordlist',help='wordlist to use')
args = parser.parse_args()

actions = []

with open(args.actionlist,'r') as a:
    for line in a:
        try:
            actions.append(line.strip())
        except:
            print("Excepttion Occured")

print(actions)
