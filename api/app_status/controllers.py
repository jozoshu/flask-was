from flask import Blueprint, request

from common.response import APIResponse
from common.response.success import Http2XX
from common.decorators import exception_format, login_required
from .services import GetLastCrawl, GetCollecionStatus

bp_status = Blueprint('status', __name__, url_prefix='/status')


@bp_status.route('/last-crawl', methods=['GET'])
@exception_format
@login_required
def get_last_crawl():
    params = request.args.to_dict()
    service = GetLastCrawl(params)
    res = service.run()
    return APIResponse(Http2XX.SUCCESS, res)


@bp_status.route('/collections', methods=['GET'])
@exception_format
@login_required
def get_collection_status():
    params = request.args.to_dict()
    service = GetCollecionStatus(params)
    res = service.run()
    return APIResponse(Http2XX.SUCCESS, res)
