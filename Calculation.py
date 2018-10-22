# -*- coding: UTF-8 -*-
import json
import logging
import math
import os
import time
from sympy import solve
from sympy import sqrt
from sympy import Symbol
from sympy import pi


def main():
    logging.basicConfig(filename='logger.log', level=logging.INFO)
    current_time = time.strftime('%Y-%m%d %H:%M:%S', time.localtime())
    start_msg = ('Start: %s' % current_time)
    logging.info(start_msg)
    input_data = read_json_file('input.json')
    properties_data = read_json_file('properties.json')
    init_args(input_data, properties_data)


def read_json_file(file_name):
    directory = os.getcwd()
    with open(
            os.path.join(directory, file_name), 'r',
            encoding='UTF-8') as json_file:
        data = json.load(json_file)
        return data


def init_args(input_data, properties_data):
    quantities = input_data['quantities']
    q = []
    for quantity in quantities:
        q.append(quantity['quantity'])
        if len(q) != 1:
            q.append(None)
    q.pop()
    tubes_num = len(q)

    quantities_sum = 0
    for i in range(1, tubes_num, 2):
        quantities_sum += q[i]
    if not math.isclose(quantities_sum, q[0]):
        logging.error('Invalid quantities.')


def cal_violity(q, d):
    v = Symbol('v')
    return solve(q - pi * pow(d, 2) * v / 4, v)


if __name__ == '__main__':
    main()
