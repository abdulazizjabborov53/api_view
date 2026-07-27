from django.core.management.base import BaseCommand
from main.models import Category, Course

class Command(BaseCommand):
    help = 'Populate database with 10 categories and 30 courses'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Course.objects.all().delete()
        Category.objects.all().delete()
        
        # Create 10 categories
        categories = []
        category_names = [
            'Web Development',
            'Mobile Development',
            'Data Science',
            'Machine Learning',
            'DevOps',
            'Cloud Computing',
            'Cybersecurity',
            'UI/UX Design',
            'Game Development',
            'Blockchain'
        ]
        
        for name in category_names:
            category = Category.objects.create(name=name)
            categories.append(category)
            self.stdout.write(f'Created category: {name}')
        
        # Create 30 courses (3 courses per category)
        course_names = [
            'HTML & CSS', 'JavaScript', 'React.js',
            'Android Development', 'iOS Development', 'Flutter',
            'Python for Data Science', 'Data Analysis', 'SQL',
            'Deep Learning', 'Neural Networks', 'TensorFlow',
            'Docker', 'Kubernetes', 'CI/CD',
            'AWS', 'Azure', 'Google Cloud',
            'Ethical Hacking', 'Network Security', 'Penetration Testing',
            'Figma', 'Adobe XD', 'Sketch',
            'Unity', 'Unreal Engine', 'Godot',
            'Solidity', 'Smart Contracts', 'Web3.js'
        ]
        
        prices = [49.99, 79.99, 99.99, 129.99, 149.99, 199.99, 249.99, 299.99]
        
        for i, name in enumerate(course_names):
            category = categories[i // 3]  # 3 courses per category
            price = prices[i % len(prices)]
            course = Course.objects.create(
                name=name,
                category=category,
                price=price
            )
            self.stdout.write(f'Created course: {name} ({category.name}) - ${price}')
        
        self.stdout.write(self.style.SUCCESS('Successfully created 10 categories and 30 courses'))
