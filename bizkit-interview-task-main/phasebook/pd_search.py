import pandas as pd

import json as json

from .data.search_data import USERS


def pd_search_users(args, data):

    df = pd.DataFrame(data)

    query_param = ""
    
    # compose our filter
    for criteria in args:
        args_criteria = args[criteria]
        if(len(query_param)):
            query_param += " | "
        if criteria == 'id':
            query_param += '( id.str.match("%s") )' % (args_criteria)
        if criteria == 'age':
            age = int(args_criteria)
            query_param += '( age.between(%d,%d) )'  % (age - 1, age + 1)
        if criteria == 'name':
            query_param += '( name.str.contains("%s") )' % (args_criteria)
        if criteria == 'occupation':
            query_param += '( occupation.str.contains("%s") )' % (args_criteria)

    if (len(query_param)):
        sdf = df.loc[df.query(query_param, engine='python').index]
        return sdf.to_dict(orient='records')
    else:
        return df.to_dict(orient='records')


def pd_sorted_search_users(args, data):
    
    df = pd.DataFrame(data)
    
    result = []

    # compose our result list
    for criteria in args:
        lst = []
        args_criteria = args[criteria]
        if criteria == 'id':
            lst = df[df['id'].str.match(pat=args_criteria)].to_dict(orient='records')
        if criteria == 'age':
            age = int(args_criteria)
            lst = df[df['age'].between(age-1, age+1)].to_dict(orient='records')
        if criteria == 'name':
            lst = df[df['name'].str.contains(pat=args_criteria)].to_dict(orient='records')
        if criteria == 'occupation':
            lst = df[df['occupation'].str.contains(pat=args_criteria)].to_dict(orient='records')
        
        #append partial list to final result list 
        for res in lst:
            if res not in result:
                result.append(res)

    if (len(args) != 0):
        return result
    else:
        return df.to_dict(orient='records')
    