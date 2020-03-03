from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


DEFAULT_PAGE = 1


class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 10
    page_size_query_param = 'page_size'

    def exist_next(self):
        if self.get_next_link() is None:
            return False
        return True

    def get_paginated_response(self, data):
        return Response({
            'next': self.exist_next(),
            'total': self.page.paginator.count,
            # 'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'results': data
        })
