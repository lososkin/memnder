from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from rest_framework.response import Response
# Create your views here.
from . import models

from .serializers import MemSerializer

#http -f POST http://127.0.0.1:8000/memes/api/create/ 'Authorization: Token a42e9cd7e07ef3a896ff93f659f4c63d13deb45e' text=xyi img@~/1.jpg
#http GET http://127.0.0.1:8000/memes/api/get/ 'Authorization: Token a42e9cd7e07ef3a896ff93f659f4c63d13deb45e'
#http post http://127.0.0.1:8000/signin_and_signup/api/login/ username=lososka password=kek
#http post http://127.0.0.1:8000/signin_and_signup/api/signup/ username=lososka password=kek password2=kek

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_mem(request):
	try:
		user = request.user
		mem = models.Mem(user_ForeignKey=user)
		mem_serializer = MemSerializer(mem,data=request.data)
		if mem_serializer.is_valid():
			mem_serializer.save()
			return Response(mem_serializer.data, status=HTTP_201_CREATED)
		else:
			return Response(mem_serializer.errors, status=HTTP_400_BAD_REQUEST)
		return Response("OK", status=HTTP_200_OK)
	except:
		return Response({'error': 'Что-то пошло не так..'},status=HTTP_400_BAD_REQUEST)


def rand_mem(user):
	id_mem = [] # тут кароче будут айдишники мемов которые юзер видел уже, хз как назвать
	for u_likes_m in models.User_likes_mem.objects.filter(user_ForeignKey=user).select_related('mem_ForeignKey'):
		id_mem.append(u_likes_m.mem_ForeignKey.id)
	memes = models.Mem.objects.all().difference(models.Mem.objects.filter(id__in=id_mem))
	if len(memes)==0:
		return None
	#memes <--- мемчики которые юзер еще не видел
	mem = memes[0]
	return mem #<---------Вот тут крутой алгоритм придумать нужно, тут кароче нужно проверку еще сделать что этот мемчик еще не давали юзеру

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_mem(request):
	try:
		user = request.user
		mem_in_queue=models.Mem_in_q.objects.filter(user_ForeignKey=user)
		if mem_in_queue:
			mem=mem_in_queue[0].mem_ForeignKey
			return Response({'text':mem.text,'img':mem.img.url}, status=HTTP_200_OK)
		else:
			mem = rand_mem(user)
			if mem is None:
				return Response("Нет мемчиков больше", status=HTTP_404_NOT_FOUND) #????????
			mem_in_queue=models.Mem_in_q.objects.create(user_ForeignKey=user,mem_ForeignKey=mem)
			mem_in_queue.save()
			return Response({'text':mem.text,'img':mem.img.urls}, status=HTTP_200_OK)
	except:
		return Response({'error': 'Что-то пошло не так..'},status=HTTP_400_BAD_REQUEST)
	

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def like_mem(request):
	try:
		user = request.user
		mem_in_queue=models.Mem_in_q.objects.get(user_ForeignKey=user)
		# mem_id = request.data.get('mem_id')
		# if str(mem_in_queue.mem_ForeignKey.id)!=mem_id:
		# 	print(mem_in_queue.mem_ForeignKey.id,mem_id)
		# 	return Response('error1', status=HTTP_400_BAD_REQUEST)
		like = int(request.data.get('like'))
		if not(like==1 or like==-1):
			return Response({'error':'like is not 1 or -1'}, status=HTTP_400_BAD_REQUEST)
		user_likes= models.User_likes_mem.objects.create(user_ForeignKey=user,mem_ForeignKey=mem_in_queue.mem_ForeignKey,value=like)
		user_likes.save()
		mem_in_queue.delete()
		return Response("OK", status=HTTP_200_OK)
	except:
			return Response({'error': 'Что-то пошло не так..'},status=HTTP_400_BAD_REQUEST)
