from rest_framework import generics, status, serializers
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import User, Country
from .serializers import UserSerializer, CountrySerializer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # print(request.POST.items())
        # return HttpResponse(request.POST.items())
        try:
            return super().create(request, *args, **kwargs)
        except serializers.ValidationError as error:
            return Response({'errors': error.detail}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        user = User.objects.filter(email=email, password=password).first()
        if user:
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


    def countries(request):
        queryset = Country.objects.all()

        serializer = CountrySerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data, safe=False)