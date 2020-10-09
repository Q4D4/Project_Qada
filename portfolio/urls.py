from django.urls import path
from portfolio import views

urlpatterns = [
	path('about/', views.AboutApiView.as_view(), name='portfolio-about'),
	path('languages/', views.LanguageListView.as_view(), name='portfolio-lang-list'),
	path('languages/<int:pk>', views.LanguageDetailView.as_view(), name='portfolio-lang-detail'),
	path('skills/', views.SkillListView.as_view(), name='portfolio-skill-list'),
	path('skills/<int:pk>', views.SkillDetailView.as_view(), name='portfolio-skill-detail'),
	path('feedback', views.FeedbackCreateView.as_view(), name='portfolio-feedback-create'),
	path('projects/', views.ProjectListView.as_view(), name='portfolio-project-list'),
	path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='portfolio-project-detail'),
	path('categories/', views.CategoryListView.as_view(), name='portfolio-category-list'),
	path('categories/<int:pk>', views.CategoryDetailView.as_view(), name='portfolio-category-detail'),
]
