from rest_framework import serializers
from .models import Todo

class TodoSimpleSerializer(serializers.ModelSerializer): # Todo List 전체 조회
    class Meta:
        model = Todo
        fields = ('id', 'title', 'complete', 'important')

class TodoDetailSerializer(serializers.ModelSerializer): # Todo List 상세 조회
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'created', 'complete', 'important')

class TodoCreateSerializer(serializers.ModelSerializer): # Todo List 생성
    class Meta:
        model = Todo
        fields = ('title', 'description', 'important')

