from django.shortcuts import render
from .forms import ReviewForm

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from my_app.models import Review
from .serializers import ReviewListSerializer, ReviewDetailSerializer, ReviewCreateSerializer, UserCreateSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.
# def create_view(request):
# 	form = ReviewForm()
# 	context = {
# 		"form":form
# 	}
# 	return render(request, 'create_page.html', context)

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer



class ReviewListView(ListAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewListSerializer
	permission_classes = [AllowAny]
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['title', 'author',]



class ReviewDetailView(RetrieveAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'detail_id'

class ReviewCreateView(CreateAPIView):
	serializer_class = ReviewCreateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class ReviewUpdateView(RetrieveUpdateAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewCreateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'update_id'


class ReviewDeleteView(DestroyAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'delete_id'
	permission_classes = [IsAdminUser]