import sys
import random
import pathlib
import platform


HERE = pathlib.Path(__file__).parent
def get_country_codes():
    country_code_list = [x.lower().strip() for x in
                         open(HERE / "servers" / "country_code_list.txt", 'r').readlines()]
    country_code_dict = {}
    for country_code in country_code_list:
        #print(f'country_code: {country_code}')
        country_and_code = country_code.split(' ')
        country = country_and_code[0].strip()
        code = country_and_code[1].strip()

        if country not in country_code_dict:
            #print(f'new country code: {country} {code}')
            country_code_dict[country]=[code]
    return country_code_dict

def pick_a_server(country):
    country = country.lower()
    countries_dict = {}
    server_names_list = [x.lower().strip() for x in open(HERE / "servers" / "server_names_cleaned_list.txt", 'r').readlines()]
    for server in server_names_list:
        name = server.split(' #')[0].strip()
        #print(name)
        if name not in countries_dict:
            #print('new name:' + name)
            countries_dict[name]=[]
        else:
            countries_dict[name].append(server)
            #print('added: ' + server)
            
    if country in countries_dict:
        c_server = random.choice(countries_dict[country])
        opsys = platform.system()
        if opsys == 'Windows':
            #print(c_server)
            return c_server;
        elif opsys == 'Linux':
            country_code_dict = get_country_codes()
            if country in country_code_dict:
                code = country_code_dict[country]
                server_id = c_server.split('#')[1].strip()
                #print(f'{code[0]}{server_id}')
                return f'{code[0]}{server_id}'
            else:
                #print('') # not found - in linux
                return ''
    else:
        #print('') # not found  - in windows
        return
            
#pick_a_server('vietnam')

#pick_a_server(sys.argv[1])