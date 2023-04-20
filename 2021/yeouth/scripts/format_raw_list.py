import ast
import pathlib
import random

HERE = pathlib.Path(__file__).parent


def limit_country_entries(limit: int):
    country_names_list = [x.lower().strip() for x in
                          open(HERE / "servers" / "server_names_raw_list.txt", 'r').readlines()]
    outfile = open(HERE / "servers" / "server_names_formatted_list_by_20s.txt", "w")
    for country in country_names_list:
        # for x in range(1):
        # country = country_names_list[x]
        name = country.split(': ')[0]
        # outfile.write('\n' + name)
        print(name)
        servers = country.split(': ')[1]
        server_list = ast.literal_eval(servers)

        for server in server_list:
            if server.find(" - ") != -1 or server.find("socks") != -1:
                continue
            outfile.write('\n' + server)
            print(server.split(' #')[1])
            limit -= 1
            if limit == 0:
                break

    outfile.close()


def create_country_list():
    server_names_list = [x.lower().strip() for x in
                         open(HERE / "servers" / "country_and_code_raw.txt", 'r').readlines()]
    outfile = open(HERE / "servers" / "country_list.txt", "w")
    countries_dict = {}
    for server in server_names_list:
        if not server:
            continue
        if 'onion' in server:
            continue
        if 'socks' in server:
            continue
        if ' - ' in server:
            continue
        # print(f'server= {server}')
        name_and_domain = server.split(':')
        name = name_and_domain[0].strip()
        name = name.split('#')[0].strip()
        domain = name_and_domain[1].strip()
        if name not in countries_dict:
            print(f'name= {name}, domain: {domain}')
            country_code = domain[0:2]
            print(f'cc= {country_code}')
            countries_dict[name] = domain
            outfile.write(f'{name}\n')

        '''else:
            countries_dict[name].append(server)
            print('added: ' + server)


    if country in countries_dict:
        print(random.choice(countries_dict[country]))
    else:
        print('not found')
        '''
    outfile.close()


def clean_server_names():
    server_names_list = [x.lower().strip() for x in
                         open(HERE / "servers" / "filtered_results_from_by_20s.txt", 'r').readlines()]
    outfile = open(HERE / "servers" / "server_names_cleaned_list.txt", "w")
    for server in server_names_list:
        # for x in range(1):
        # country = country_names_list[x]
        name = server.split('=')[1].strip()
        print(name)
        outfile.write(name + '\n')
    outfile.close()



create_country_list()
#create_country_codes()
#pick_a_server('albania')
# limit_country_entries(20)

# clean_server_names()
