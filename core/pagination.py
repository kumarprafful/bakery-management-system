from rest_framework.pagination import CursorPagination as CPagination

class CursorPagination(CPagination):
    ordering = '-created'
    page_size = 100