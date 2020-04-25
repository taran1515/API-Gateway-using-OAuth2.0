from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import generics

import requests
from .models import UserProfile
from .serializers import CreateUserSerializer

#Client id and Client Secret obtained 
# while registering to the Authorization Server.

CLIENT_ID = 'hQ2vwrgPjEi21s8idlpPuJ5ajAi5Bz5WxK59Y7X9'
CLIENT_SECRET = 'Wx6l5uQwmHIedM7MOxUdYVOG9sMLmSoxdzwSxLSxKtB6Gr4RVCmohcHgh7smAF1fQ2y312TEjNuuqfaJF06lIkD8uDvzSOmQPy18FTJbmkOMLxre8xw9hCP81yTLyDM4'


class RegisterView(generics.CreateAPIView):
    """
    View to allow user to get registered using 
    email, name and password.
    """
    permission_classes = [AllowAny]
    serializer_class = CreateUserSerializer
    queryset = UserProfile.objects.all()



@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"email": "email@gmail.com",
    "password": "1234abcd"}
    '''
    r = requests.post(
    'http://127.0.0.1:8000/o/token/', 
        data={
            'grant_type': 'password',
            'username': request.data['email'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())