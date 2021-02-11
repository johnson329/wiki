from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from courses.models import Category, Lesson


# class CategorySiteMap(Sitemap):
#     changefreq = "Weekly"
#     priority = "0.6"
#
#     def items(self):
#         return Category.objects.all()
#
#     def lastmod(self, obj):
#         return obj.updated

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['category_all', ]

    def location(self, item):
        # print(item,"*"*100)
        return reverse(item)

class CourseSiteMap(Sitemap):
    changefreq = "Weekly"
    priority = "0.9"

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.updated


class LessonSiteMap(Sitemap):
    changefreq = "Weekly"
    priority = "1.0"

    def items(self):
        return Lesson.objects.all()

    def lastmod(self, obj):
        return obj.updated
