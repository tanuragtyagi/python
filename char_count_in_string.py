#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 08:21:11 2020

@author: tanuragtyagi
"""

user_input = input("enter any string = ")

uniq_char = list(set(user_input))

print(uniq_char.sort(reverse = 1))

for value in uniq_char:
    print(value, user_input.count(value), sep = "", end = "")