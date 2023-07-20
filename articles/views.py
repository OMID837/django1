from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from .models import Articles
from django.views.generic import DetailView

# Create your views here.
class Article(View):
    def get(self, request):
        article = Articles.objects.filter(is_active=True)[:12]
        return render(request, 'articles/articles.html', {'article': article})

class ArticleDetails(DetailView):
    model = Articles
    template_name = 'articles/article_details.html'
    # return render(request, 'articles/article_details.html', {'article' :article})










def header_component(request):
    return render(request, 'shared/header_component.html')


def footer_component(request):
    return render(request, 'shared/footer_component.html')
