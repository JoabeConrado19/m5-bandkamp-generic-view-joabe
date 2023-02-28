from rest_framework.views import APIView, Response, status, Request
from rest_framework.pagination import PageNumberPagination


class GetCommonView(APIView, PageNumberPagination):
    def list(self, request):

        queryset = self.view_queryset.all()

        result_page = self.paginate_queryset(queryset, request)
        serializer = self.view_serializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


class PostCommonView(APIView):

    def create(self, request: Request) -> Response:

        serializer = self.view_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class GetPostCommonView(GetCommonView, PostCommonView, APIView, PageNumberPagination):
    def get(self, request: Request) -> Response:
        return super().list(request)

    def post(self, request: Request) -> Response:
        return super().create(request)

