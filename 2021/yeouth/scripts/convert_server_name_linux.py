import ast
import pathlib
import random

HERE = pathlib.Path(__file__).parent

DEBUG = False

def log( message):
    if DEBUG:
        print(message)

def get_country_codes():
    country_code_list = [x.lower().strip() for x in
                         open(HERE / "servers" / "country_code_list.txt", 'r').readlines()]
    country_code_dict = {}
    for country_code in country_code_list:
        country_code = country_code.strip()
        log(f'country_code: {country_code}')
        country = country_code[:-2]
        code=country_code[-2:]
        #if country not in country_code_dict:
        log(f'new country code: {country} {code}')
        country_code_dict[country]=[code]
    return country_code_dict

def convert(server_name):
    log(f'server_name: {server_name}')
    c_and_c = server_name.split(' #')

    if len(c_and_c) < 2:
        if DEBUG:
            log('not found')
        return 'not found'

    country = c_and_c[0].strip().lower()
    server_id = c_and_c[1].strip()
    country_code_dict = get_country_codes()
    log(f'country: {country}')
    for key, value in country_code_dict.items():
        log(f'key: {key} country: {country} ')
        if key.strip() == country.strip():
            code = value[0]
            server_name = f'{code}{server_id}'
            log(server_name)
            return server_name

    log('not found')  # not found - in linux
    return 'not found'

convert('Bulgaria #46')