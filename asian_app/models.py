from django.db import models # type: ignore
from pytils.translit import slugify # type: ignore
from datetime import datetime

class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)


    class Meta:
        verbose_name = "Город"
        verbose_name_plural  = "Города"

    def __str__(self):
        return self.name

    def save (self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Job(models.Model):
    title = models.CharField("Актуальные предложения", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите категории")
    company = models.CharField("Название компании", max_length=100)
    experience = models.CharField("Стаж работы", max_length=85, default="без опыта")
    salary = models.CharField("Оклад", max_length=85)
    description = models.TextField("Описание предложения")
    skills = models.CharField("Навыки", max_length=255)
    address = models.CharField("Адрес", max_length=100)
    phone = models.CharField("Телефон", max_length=14)
    mail = models.CharField("E-mail", max_length=100)
    created_id = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Предложения"
        verbose_name = "Предложении"

    def __str__(self):
        return self.title
    
class Information(models.Model):
    title = models.CharField("Информации", max_length=255)
    description = models.TextField("Описание информации")
    image = models.CharField("URL-фото", max_length=500)
    created_at = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Информация"
        verbose_name = "Информации"

    def __str__(self):
        return self.title
    
class Likes(models.Model):
    title = models.CharField("Избранное", max_length=255)
    created_id = models.DateTimeField("Дата и время публикации", default=datetime.now )
    class Meta:
        verbose_name = "Избранное"
        verbose_name = "Избранные"

    def __str__(self):
        return self.title

