from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializers import *

class TodosAPIView(APIView): 
    def get(self, request): # GET 방식으로 요청 처리
        todos = Todo.objects.filter(complete=False)
        serializer = TodoSimpleSerializer(todos, many=True) # 시리얼라이저 통과시켜 보낼 수 있는 형태로 변환하는 것
        return Response(serializer.data, status=status.HTTP_200_OK) # 변환 후 Responser 객체 형태로 전달
    
    def post(self, request): # POST 방식으로 요청 처리
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid(): # 유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoAPIView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk): # 특정 Todo에 대해 이뤄지는 작업이므로
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoCreateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

class DoneTodosAPIView(APIView):
    def get(self, request):
        dones = Todo.objects.filter(complete=True)
        serializer = TodoSimpleSerializer(dones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DoneTodoAPIView(APIView):
    def get(self, request, pk):
        done = get_object_or_404(Todo, id=pk)
        done.complete = True
        done.save()
        serializer = TodoDetailSerializer(done)
        return Response(status=status.HTTP_200_OK)