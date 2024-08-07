from flask import Blueprint, request

from .data.search_data import USERS

from .pd_search import pd_search_users,pd_sorted_search_users


bp = Blueprint("search", __name__)


@bp.route("/search")
def search():
    return search_users(request.args.to_dict()), 200

@bp.route("/search_v2")
def sorted_search():
    return sorted_search_users(request.args.to_dict()), 200

def search_users(args):    
    return pd_search_users(args,USERS)

def sorted_search_users(args):
    return pd_sorted_search_users(args, USERS)
 