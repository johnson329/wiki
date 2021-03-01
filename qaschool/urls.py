from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from courses import views
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from courses.models import Lesson
from courses.models import Course
from qaschool.sitemap import CourseSiteMap,LessonSiteMap,StaticViewSitemap

# info_dict = {
#     'queryset': Lesson.objects.all(),
#     # 'date_field': 'pub_date',
# }
#
# category_dict={
#     'queryset': Course.objects.all(),
#     # 'date_field': 'pub_date',
# }

sitemaps={
    'courses':CourseSiteMap,
    'lesson':LessonSiteMap,
    'index':StaticViewSitemap
}


urlpatterns = [
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('wocao1/', admin.site.urls),


    path('mdeditor/', include('mdeditor.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),

    # path('', views.index, name='index'),

    # path('account/', include('account.urls')),
    path('', include('courses.urls')),
    path('blog/', include('blog.urls')),
    # path('resource/', include('resource.urls')),
    # path('practice/', include('practice.urls')),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

