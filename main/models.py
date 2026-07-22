from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banners/')
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
class About(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='about/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=100, help_text="Icon class or name")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='articles/')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def comments(self):
        return ArticleComment.objects.filter(article=self)

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)