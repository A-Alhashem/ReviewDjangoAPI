from django.shortcuts import render
from .forms import ReviewForm

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from my_app.models import Review
from .serializers import ReviewListSerializer, ReviewDetailSerializer, ReviewCreateSerializer


# Create your views here.
# def create_view(request):
# 	form = ReviewForm()
# 	context = {
# 		"form":form
# 	}
# 	return render(request, 'create_page.html', context)



class ReviewListView(ListAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewListSerializer


class ReviewDetailView(RetrieveAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'detail_id'

class ReviewCreateView(CreateAPIView):
	serializer_class = ReviewCreateSerializer

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