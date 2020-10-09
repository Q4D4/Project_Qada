from rest_framework import serializers
# Models
from portfolio.models import Language, About, Skill, Feedback, Category, Project
# Settings
from django.conf import settings
from datetime import date


class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Language
		fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
	languages = LanguageSerializer(many=True, read_only=True)
	profile_image = serializers.SerializerMethodField()
	age = serializers.SerializerMethodField()

	def get_profile_image(self, obj):
		return {
			'low': settings.DOMAIN_LINK + settings.STATIC_URL + 'portfolio/profile-images/' + str(obj.id) + '_low.jpg',
			'medium': settings.DOMAIN_LINK + settings.STATIC_URL + 'portfolio/profile-images/' + str(obj.id) + '_medium.jpg',
			'high': settings.DOMAIN_LINK + settings.STATIC_URL + 'portfolio/profile-images/' + str(obj.id) + '_high.jpg'
		}


	def get_age(self, obj):
		return	date.today().year - obj.birth_date.year - ((date.today().month, date.today().day) < (obj.birth_date.month, obj.birth_date.day))


	class Meta:
		model = About
		fields = [
			'id',
			'age',
			'first_name',
			'last_name',
			'birth_date',
			'short_bio',
			'profile_image',
			'country',
			'city',
			'phone',
			'email',
			'nationality',
			'experience_years',
			'completed_projects',
			'happy_clients',
			'awards_won',
			'facebook_profile',
			'instagram_profile',
			'twitter_profile',
			'github_profile',
			'languages'
		]


class SkillSerializer(serializers.ModelSerializer):
	photo = serializers.SerializerMethodField()


	def get_photo(self, obj):
		return {
			'low': settings.DOMAIN_LINK + settings.STATIC_URL + 'portfolio/skill-images/' + (obj.skill_name).strip().replace(' ', '_') + '_low.png',
			'medium': settings.DOMAIN_LINK + settings.STATIC_URL + 'portfolio/skill-images/' + (obj.skill_name).strip().replace(' ', '_') + '_medium.png',
			'high': settings.DOMAIN_LINK + settings.STATIC_URL + 'portfolio/skill-images/' + (obj.skill_name).strip().replace(' ', '_') + '_high.png'
		}

	class Meta:
		model = Skill
		fields = [
			'id',
			'skill_name',
			'photo'
		]


class FeedbackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Feedback
		fields = [
			'name',
			'email',
			'subject',
			'message',
		]
		read_only_fields = [
			'id'
		]


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
	used_technologies = SkillSerializer(many=True, read_only=True)
	categories = CategorySerializer(many=True, read_only=True)
	photo = serializers.SerializerMethodField()


	def get_photo(self, obj):
		return {
			'low': settings.DOMAIN_LINK + settings.STATIC_URL + 'portfolio/project-images/' + str(obj.id) + '_low.jpg',
			'medium': settings.DOMAIN_LINK + settings.STATIC_URL + 'portfolio/project-images/' + str(obj.id) + '_medium.jpg',
			'high': settings.DOMAIN_LINK + settings.STATIC_URL + 'portfolio/project-images/' + str(obj.id) + '_high.jpg'
		}


	class Meta:
		model = Project
		fields = [
			'id',
			'project_name',
			'used_technologies',
			'categories',
			'repository_link',
			'link_to_project',
			'about_project',
			'photo'
		]