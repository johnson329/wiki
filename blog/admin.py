from django.contrib import admin

# Register your models here.
from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(BlogAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)
    fields = ('title', 'slug', 'keywords',('owner',),'description', 'md_content', 'html_content')
    list_display = ('title', 'order', 'visible','owner', 'created', 'updated')
    list_filter = ('visible', 'owner')
    list_editable = ['visible']


admin.site.register(Blog, BlogAdmin)