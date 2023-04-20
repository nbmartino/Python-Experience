import sys
import random
import pathlib
import platform

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
        log(f'country_code: {country_code}')
        country_and_code = country_code.split(' ')
        country = country_and_code[0].strip()
        code = country_and_code[1].strip()

        if country not in country_code_dict:
            log(f'new country code: {country} {code}')
            country_code_dict[country]=[code]
    return country_code_dict

def pick_a_server(country):
    country = country.lower()
    countries_dict = {}
    server_names_list = [x.lower().strip() for x in open(HERE / "servers" / "server_names_cleaned_list.txt", 'r').readlines()]
    for server in server_names_list:
        name = server.split(' #')[0].strip()
        log(name)
        if name not in countries_dict:
            log('new name:' + name)
            countries_dict[name]=[]
        else:
            countries_dict[name].append(server)
            log('added: ' + server)
            
    if country in countries_dict:
        c_server = random.choice(countries_dict[country])
        opsys = platform.system()
        if opsys == 'Windows':
            log(c_server)
        elif opsys == 'Linux':
            country_code_dict = get_country_codes()
            if country in country_code_dict:
                code = country_code_dict[country]
                server_id = c_server.split('#')[1].strip()
                log(f'{code[0]}{server_id}')
            else:
                log('not found') # not found - in linux
    else:
        log('not found') # not found  - in windows
            
pick_a_server('vietnam')

#pick_a_server(sys.argv[1])  