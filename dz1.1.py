# -*- coding: utf-8 -*-

import sys
def env_print(*values, sep=' ', end='\n', file=sys.stdout, start='', max_line=40, in_file=False):
    result = ''
    is_first_value = True
    for value in values:
        result += (start if is_first_value else '') + ('' if is_first_value else sep) + str(value)
        is_first_value = False
    result = result + end
    if len(result) > max_line:
        list_for_result = []
        for index in range(0, len(result), max_line):
            list_for_result.append(result[index:index + max_line] + '\n')
        result = ''.join(list_for_result)
    if in_file == True:
        with open('result.txt', 'a') as file_to_write:
            file_to_write.write(result)
    return file.write(result)

env_print('hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo', 'mad', 'world', end=' !!!', sep='*', start='!!! ', max_line=30)
