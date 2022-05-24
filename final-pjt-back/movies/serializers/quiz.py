from rest_framework import serializers
from ..models import Question, Value

class ValueSerializer(serializers.ModelSerializer):

    # question_content = serializers.CharField(source='question.content')
    class Meta:
        model = Value
        fields = ('__all__')


class QuestionSerializer(serializers.ModelSerializer):

    value_set = ValueSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('__all__')



