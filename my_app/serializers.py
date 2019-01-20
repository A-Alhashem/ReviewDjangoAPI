from rest_framework import serializers
from my_app.models import Review

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title', 'author',]

class ReviewDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = '__all__'

class ReviewCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = '__all__'
