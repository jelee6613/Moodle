from django.forms import CharField
from django.shortcuts import get_object_or_404
from executing import Source
from rest_framework import serializers
from ..models import Question, Value

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('__all__')

class ValueSerializer(serializers.ModelSerializer):

    question_content = serializers.CharField(source='question.content')
    class Meta:
        model = Value
        fields = ('__all__')


