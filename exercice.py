#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_even_keys(dictionary):
	return {n for n in dictionary.keys() if n % 2 == 0}

def join_dictionaries(dictionaries):
	return {k: v for d in dictionaries for k, v in d.items()}

def dictionary_from_lists(keys, values):
	return dict(zip(keys, values))

def get_greatest_values(dictionnary, num_values):
	max_values = []
	copy_dict = copy.deepcopy(dictionnary)

	for _ in range(0, num_values):
		max_value = max(copy_dict.items(), key = lambda x: x[1])
		max_values.append(max_value[1])
		del copy_dict[max_value[0]]

	return max_values



def get_sum_values_from_key(dictionnaries, key):
	sum = 0

	for dictionnary in dictionnaries:
		if key in dictionnary:
			sum += dictionnary[key]

	return sum


if __name__ == "__main__":
	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	print(get_even_keys(yeet))
	print()

	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	doot = {
		0xBEEF: "doot",
		0xDEAD: "DOOT",
		0xBABE: "dOoT"
	}
	print(join_dictionaries([yeet, doot]))
	print()
	
	doh = [
		"D'OH!",
		"d'oh",
		"DOH!"
	]
	nice = [
		"NICE!",
		"nice",
		"nIcE",
		"NAIIIIICE!"
	]
	print(dictionary_from_lists(doh, nice))
	print()
	
	nums = {
		"nice": 69,
		"nice bro": 69420,
		"AGH!": 9000,
		"dude": 420,
		"git gud": 1337
	}
	print(get_greatest_values(nums, 1))
	print(get_greatest_values(nums, 3))
	print()

	bro1 = {
		"money": 12,
		"problems": 14,
		"trivago": 1
	}
	bro2 = {
		"money": 56,
		"problems": 406
	}
	bro3 = {
		"money": 1,
		"chichis": 1,
		"power-level": 9000
	}
	print(get_sum_values_from_key([bro1, bro2, bro3], "problems"))
	print(get_sum_values_from_key([bro1, bro2, bro3], "money"))
	print()
