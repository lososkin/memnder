
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.contrib.auth.models import User

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def signup(request):
	try:
	    username = request.data.get("username")
	    password = request.data.get("password")
	    password2 = request.data.get("password2")
	    if username is None or password is None or password2 is None:
	        return Response({'error': 'Please provide both username and password'},
	                        status=HTTP_400_BAD_REQUEST)

	    if password!=password2:
	        return Response({'error': 'password != password2'},
	                        status=HTTP_400_BAD_REQUEST)


	    username_in_system=User.objects.filter(username=username)
	    if username_in_system:
	        return Response({'error': 'Такой логоин уже существует'},
	                        status=HTTP_400_BAD_REQUEST)

	    user=User.objects.create_user(username, ' ', password)
	    user.save()
	    token, _ = Token.objects.get_or_create(user=user)
	    return Response({'token': token.key},
	                    status=HTTP_200_OK)
	except:
		return Response({'error': 'Что-то пошло не так..'},
	                        status=HTTP_400_BAD_REQUEST)

