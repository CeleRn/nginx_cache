# -*- coding: utf-8 -*-

import hashlib

cache_main_dir = '/home/odoo/scplex/cache/from_odoo/'
length_dirs_list_str = '2:2'
cache_key = 'GET|||subdomain.scplex.ru|/service/10/'

def cache_key_to_path_cache_file(cache_main_dir, length_dirs_list_str, cache_key):

    length_dirs_list = tuple(length_dirs_list_str.split(':'))
    cache_hash = hashlib.md5(cache_key.encode())
    file_name = cache_hash.hexdigest()

    path_to_cache_file = ''

    i = 0
    for length_dir in length_dirs_list:
        if i == 0:
            dir_path = file_name[0 - int(length_dir):]
        else:
            dir_path = file_name[0 - int(length_dir) - i:0 - i]
        i += int(length_dir)
        path_to_cache_file +=  dir_path + '/'

    path_to_cache_file = cache_main_dir + path_to_cache_file + file_name
    return path_to_cache_file

print ('Path to nginx cache file: ' + cache_key_to_path_cache_file(cache_main_dir,length_dirs_list_str,cache_key))