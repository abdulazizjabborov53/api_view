from rest_framework import serializers
from .models import HeroSection, Category, Course


class HeroSectionSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    sub_title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = HeroSection
        fields = ['id', 'image', 'title', 'sub_title', 'description']

    def get_title(self, obj):
        lang = self.context.get('lang')
        if lang == 'ru':
            return obj.title_ru or obj.title_uz
        elif lang == 'en':
            return obj.title_en or obj.title_uz
        return obj.title_uz

    def get_sub_title(self, obj):
        lang = self.context.get('lang')
        if lang == 'ru':
            return obj.sub_title_ru or obj.sub_title_uz
        elif lang == 'en':
            return obj.sub_title_en or obj.sub_title_uz
        return obj.sub_title_uz

    def get_description(self, obj):
        lang = self.context.get('lang')
        if lang == 'ru':
            return obj.description_ru or obj.description_uz
        elif lang == 'en':
            return obj.description_en or obj.description_uz
        return obj.description_uz


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'category', 'price']
