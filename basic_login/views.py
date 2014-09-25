from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer

class UserRegistrationView(APIView):
    def post(self, request, **extra):
        print request.DATA
        serializer = UserRegistrationSerializer(data=request.DATA)
        if serializer.is_valid():
            print 'valid hai'
        else:
            return Response(serializer.errors)
        return Response(serializer.data)


