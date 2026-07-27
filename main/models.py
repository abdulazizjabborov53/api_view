from django.db import models
from deep_translator import GoogleTranslator


class HeroSection(models.Model):
    image = models.ImageField(upload_to='hero_section', null=True, blank=True)
    sub_title_uz = models.CharField(max_length=255)
    sub_title_ru = models.CharField(max_length=255, null=True, blank=True)
    sub_title_en = models.CharField(max_length=255, null=True, blank=True)

    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)

    description_uz = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        fields_to_translate = ["sub_title", "title", "description"]

        for field in fields_to_translate:
            uz_val = getattr(self, f"{field}_uz")
            if uz_val:
                # Ru tarjimasi
                if not getattr(self, f"{field}_ru"):
                    translated_ru = GoogleTranslator(
                        source="uz", target="ru"
                    ).translate(uz_val)
                    setattr(self, f"{field}_ru", translated_ru)

                # EN tarjimasi
                if not getattr(self, f"{field}_en"):
                    translated_en = GoogleTranslator(
                        source="uz", target="en"
                    ).translate(uz_val)
                    setattr(self, f"{field}_en", translated_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_uz


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name