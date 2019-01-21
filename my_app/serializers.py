from rest_framework import serializers
from my_app.models import Review

from django.contrib.auth.models import User


class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password']

	def create(self, validated_data):
		user = validated_data['username']
		_pass = validated_data['password']
		new_user = User(username = user)
		new_user.set_password(_pass)
		new_user.save()
		return validated_data


class ReviewListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = 'detail',
		lookup_field = 'id',
		lookup_url_kwarg = 'detail_id'
		)

	created_by = serializers.SerializerMethodField()

	class Meta:
		model = Review
		fields = ['title', 'author', 'detail', 'created_by']

	def get_created_by(self, obj):
		return "created by the awesemeness of django!"

class ReviewDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = '__all__'

class ReviewCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		exclude = ['author']
