from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.authtoken.models import Token
from accounts.serializers import RegisterSerializer

class RegisterView(APIView): #CustomerRegistrationView
    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            serializer = RegisterSerializer(data=data)

            if serializer.is_valid():
                user = serializer.save()
                token, _ = Token.objects.get_or_create(user=user)
            else:
                return Response({'status': 'error', 'message': serializer.errors}, status=400)
            return Response({'status': 'success', 'token': token.key}, status=201)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=400)

class Login(ObtainAuthToken):
    def post(self,  request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data, context={'request': request})
            if serializer.is_valid():
                user = serializer.validated_data['user']
                token, _ = Token.objects.get_or_create(user=user)
            else:
                return Response({'status': 'error', 'message': serializer.errors}, status=400)
            return Response({'status': 'success', 'token': token.key, 'email': user.email}, status=200)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=400)

        
            