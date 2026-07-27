from django_filters import rest_framework as filters
from .models import Course

class CourseFilter(filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'name': ['exact', 'icontains'],
            'price': ['exact', 'gte', 'lte'],
            'category': ['exact'],
        }
