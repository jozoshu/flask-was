from flask import Blueprint, request

from common.response import send_format
from .services import GetLastCrawl, GetCollecionStatus

main = Blueprint('status', __name__, url_prefix='/status')


@main.route('/last-crawl', methods=['GET'])
@send_format
def get_last_crawl():
    params = request.args.to_dict()
    service = GetLastCrawl(params)
    res = service.run()
    return res


@main.route('/collections', methods=['GET'])
@send_format
def get_collection_status():
    params = request.args.to_dict()
    service = GetCollecionStatus(params)
    res = service.run()
    return res
