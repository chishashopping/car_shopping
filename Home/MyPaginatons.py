from _collections import OrderedDict

from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response


class StoreListPager(PageNumberPagination):

    page_size_query_param = 'limit'     # 每页记录数的参数名字
    page_query_param = 'count'

    # 自定义分页形式
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page_range', list(self.page.paginator.page_range)),  # 页码范围
            ('has_next', self.page.has_next()),
            ('has_prious', self.page.has_previous()),
            ('next_page_number', self.page.next_page_number()),
            ('results', data)
        ]))
