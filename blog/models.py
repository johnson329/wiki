from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.urls import reverse
from mdeditor.fields import MDTextField

from courses.fields import OrderField
from courses.models import Page, Social



class Blog(Page, Social):
    # course = models.ForeignKey(Course, related_name='lessons',
    #                            on_delete=models.CASCADE, verbose_name="所属课程")
    order = OrderField( blank=True, verbose_name="排序")
    md_content = MDTextField("内容", blank=True, null=True)
    html_content = RichTextField("内容", blank=True, null=True)

    class Meta:
        verbose_name_plural = verbose_name = '博客内容'

    def get_absolute_url(self):
        return reverse('blog_detail', args=(self.slug,))

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])
