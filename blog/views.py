import markdown
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Blog


def blog_index(request):
    blogs = Blog.objects.all()

    return render(request, 'blog/index.html', context={
        'blogs': blogs
    })


def blog_detail(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug, visible=True)
    blog.viewed()

    blog.content = markdown.markdown(blog.md_content.replace("\r\n", '  \n'),
                                     extensions=['markdown.extensions.extra',
                                                 'markdown.extensions.codehilite',
                                                 'markdown.extensions.toc', ])

    return render(request, 'blog/detail.html', locals())
