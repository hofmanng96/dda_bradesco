#!/usr/bin/python
# -*- coding: utf-8 -*-

import fileinput
import glob
import sys


    # IVO KNORST

for line in fileinput.input(glob.glob(r'\\192.168.4.100\Skyline\inbox\PAG_*.ret'),
                            inplace=True):
        sys.stdout.write(line.replace('496599520000015', '000049659952015'))

    # FILLER ALIMENTOS E BEBIDAS LTDA

for line in fileinput.input(glob.glob(r'\\192.168.4.100\Skyline\inbox\PAG_*.ret'),
                            inplace=True):
        sys.stdout.write(line.replace('176513000158000', '000176513000158'))

    # CASSIANO ZANOL

for line in fileinput.input(glob.glob(r'\\192.168.4.100\Skyline\inbox\PAG_*.ret'),
                            inplace=True):
        sys.stdout.write(line.replace('959473100000015', '000095947310015'))

    # GEAZI NEVES DA SILVA

    for line in fileinput.input(glob.glob(r'\\192.168.4.100\Skyline\inbox\PAG_*.ret'),
                            inplace=True):
        sys.stdout.write(line.replace('017520160000092', '000001752016092'))

    # JAIME PONATH

    for line in fileinput.input(glob.glob(r'\\192.168.4.100\Skyline\inbox\PAG_*.ret'),
                            inplace=True):
        sys.stdout.write(line.replace('576045500000010', '000005760455001'))

    # ROBERTO EWALDO STRASSBURGER

    for line in fileinput.input(glob.glob(r'\\192.168.4.100\Skyline\inbox\PAG_*.ret'),
                            inplace=True):
        sys.stdout.write(line.replace('255725550000053', '000025572555053'))

    # NATANAEL NADIR NANTHAL

    for line in fileinput.input(glob.glob(r'\\192.168.4.100\Skyline\inbox\PAG_*.ret'),
                            inplace=True):
        sys.stdout.write(line.replace('561608870000068', '000056160887068'))

    # JOAO CARLOS GARCIA

    for line in fileinput.input(glob.glob(r'\\192.168.4.100\Skyline\inbox\PAG_*.ret'),
                            inplace=True):
        sys.stdout.write(line.replace('649598640000087', '000064959864087'))

    # ADELIO LUIZ SBARDELOTTO

    for line in fileinput.input(glob.glob(r'\\192.168.4.100\Skyline\inbox\PAG_*.ret'),
                            inplace=True):
        sys.stdout.write(line.replace('472206350000087', '000047220635087'))
