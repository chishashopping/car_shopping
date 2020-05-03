from rest_framework import pagination


class LimitSet(pagination.LimitOffsetPagination):
    default_limit = 3           # 默认条数
    page_query_param = 'count'  # 页数
    limit_query_param = 'limit' # 条数
    max_limit = None            # 最大每页显示数


