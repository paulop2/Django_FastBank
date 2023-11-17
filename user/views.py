from rest_framework.response import Response
from rest_framework import (
    status,
    generics,
)
from rest_framework_simplejwt import authentication as authenticationJWT
from user.serializers import UserSerializer
from user.permissions import IsCreationOrIsAthenticated
