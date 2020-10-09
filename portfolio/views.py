from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters
# Models
from portfolio.models import Language, About, Skill, Feedback, Category, Project
# Serializers
from portfolio.serializers import AboutSerializer, LanguageSerializer, SkillSerializer, FeedbackSerializer, ProjectSerializer, CategorySerializer

# API Views
class AboutApiView(APIView):
	def get(self, request, format=None):
		about_object = About.objects.all().using('portfolio').last()
		serializer = AboutSerializer(about_object, many=False)
		return Response(serializer.data)


class LanguageListView(generics.ListAPIView):
	queryset = Language.objects.all().using('portfolio')
	serializer_class = LanguageSerializer


class LanguageDetailView(generics.RetrieveAPIView):
	queryset = Language.objects.all().using('portfolio')
	serializer_class = LanguageSerializer


class SkillListView(generics.ListAPIView):
	queryset = Skill.objects.all().using('portfolio')
	serializer_class = SkillSerializer
	filter_backends = [filters.OrderingFilter]
	ordering_fields = ['level', 'id']


class SkillDetailView(generics.RetrieveAPIView):
	queryset = Skill.objects.all().using('portfolio')
	serializer_class = SkillSerializer


class FeedbackCreateView(generics.CreateAPIView):
	throttle_scope = 'feedback'
	queryset = Feedback.objects.all().using('portfolio')
	serializer_class = FeedbackSerializer


class ProjectListView(generics.ListAPIView):
	queryset = Project.objects.all().using('portfolio')
	serializer_class = ProjectSerializer
	filter_backends = [filters.OrderingFilter]
	ordering_fields = ['id']


class ProjectDetailView(generics.RetrieveAPIView):
	queryset = Project.objects.all().using('portfolio')
	serializer_class = ProjectSerializer


class CategoryListView(generics.ListAPIView):
	queryset = Category.objects.all().using('portfolio')
	serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
	queryset = Category.objects.all().using('portfolio')
	serializer_class = CategorySerializer