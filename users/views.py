from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner
from utils.common_views import PostCommonView, GetPostCommonView
from utils.details_views import GetDetailView, OnlyGetDetailView, OnlyPatchDetailView, OnlyDeleteDetailView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView



class UserView(ListAPIView, CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer


    
