from rest_framework.pagination import PageNumberPagination

# Custom pagination class
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
