from rest_framework import serializers
from .models import authors,books,orders

class authorSerializer(serializers.ModelSerializer):

    class Meta:
        model=authors
        fields='__all__'

class bookSerializer(serializers.ModelSerializer):

    class Meta:
        model=books
        fields='__all__'

class orderSerializer(serializers.ModelSerializer):

    class Meta:
        model=orders
        fields='__all__'