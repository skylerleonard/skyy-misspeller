#!/usr/bin/env python
# encoding: utf-8
"""
    misspeller.py
    Copyright (C) 2011  Skyler Leonard

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys, os, random, string

def random_sort(l):
	"""Sort a list randomly"""
	nl = []
	length = len(l)
	for i in range(length):
		nl.append(l.pop(random.randrange(len(l))))
	return nl

def misspellword(word):
	"""Legibly misspell a word by changing the interior letters around"""
	if len(word) in (0,1,2,3): return word
	if len(word) in (4,): return word[::2] + word[1::2]
	word_list = list(word)
	first , last = word_list.pop(0) , word_list.pop(-1)
	scr_word_list = random_sort(word_list)
	wrong_word = first + "".join(scr_word_list) + last
	return wrong_word

def remove_punctuation(text):
	punctuation = []
	just_letters = ""
	for i in range(len(text)):
		if text[i] not in string.ascii_letters + " ":
			punctuation.append((i,text[i]))
		else:
			just_letters += text[i]
	return just_letters, punctuation

def add_punctuation(text, punct):
	for index, char in punct:
		text = text[:index] + char + text[index:]
	return text

def main(text):
	text, punct = remove_punctuation(text)
	text_word_list = text.split()
	wrong_word_list = [misspellword(word) for word in text_word_list]
	wrong_without_punct = " ".join(wrong_word_list)
	wrong = add_punctuation(wrong_without_punct, punct)
	print(wrong)
	return 0

if __name__ == '__main__':
	sys.exit(main(input("Paragraph: ")))

