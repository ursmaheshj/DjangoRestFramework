from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 4