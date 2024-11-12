from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class BookCategory(models.Model):
    name = models.CharField(max_length=140)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Book(models.Model):
    PUBLISHED = 'Published'
    DRAFT = 'Draft'

    STATUSES = [
                (PUBLISHED,'Опубликовано'),
                (DRAFT,'Черновик'),
                ]

    title = models.CharField(max_length=140)
    author = models.CharField(max_length=140)
    category = models.ForeignKey(BookCategory,on_delete=models.SET_NULL,blank=True,null=True,related_name='books')
    description = models.CharField(max_length=800)
    review = models.CharField(max_length=800)
    rate = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    status = models.CharField(max_length=140,default='Draft',choices=STATUSES)