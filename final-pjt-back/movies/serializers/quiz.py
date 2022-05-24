from django.shortcuts import get_object_or_404
from rest_framework import serializers
from ..models import Question, Value

class QuestionSerializer(serializers.ModelSerializer):

    # value_set = ValueSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('__all__')

class ValueSerializer(serializers.ModelSerializer):

    question = QuestionSerializer()

    class Meta:
        model = Value
        fields = ('__all__')
        read_only_fields = ('value_id', 'content', 'director', 'question',)


