from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest,JsonResponse
from django.views import View
from django.views.generic.list import ListView
from .models import Article, ArticleComment, ArticleCategory
from django.views.generic import ListView, DetailView
from .form import ArticleCommentForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class ArticleListView(ListView):
    template_name = 'article_modules/article_list.html'
    model = Article
    context_object_name = 'article_list'
    paginate_by = 6
    #در هر صفحه 6 مقاله نشون بده


    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        context['header_title'] = 'لیست مقالات'
        return context

    def get_queryset(self):
        base_query = super(ArticleListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            base_query = base_query.filter(selected_categories__url_title__iexact=category_name)
        return base_query


class ArticleDetailView(DetailView):
    template_name = 'article_modules/article_detail.html'
    model = Article

    def get_object(self, queryset=None):
        return get_object_or_404(Article, id=self.kwargs['id'])

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        article: Article = kwargs.get('object')
        context['comments'] = ArticleComment.objects.filter(article=article,
                        parent=None).order_by('create_date').prefetch_related('articlecomment_set')
        context['comments_count'] = ArticleComment.objects.filter(article=article).count()
        context['comment_form'] = ArticleCommentForm()
        return context

    def post(self, request, *args, **kwargs):
        article = self.get_object()
        article_form = ArticleCommentForm(request.POST)
        if article_form.is_valid():
            comment = article_form.save(commit=False)
            comment.article = article
            if request.user.is_authenticated:
                comment.user = request.user
            comment.save()
            return redirect(article.get_absolute_url())
        return self.get(request, *args, **kwargs)


@csrf_exempt
def add_article_comment(request: HttpRequest):
    if request.method == "POST" and request.user.is_authenticated:
        article_id = request.POST.get('articleID')
        article_comment = request.POST.get('articleComment')
        parent_id = request.POST.get('parentId')
        parent_id = None if parent_id in [None, '', 'null'] else parent_id

        if not article_id or not article_comment:
            return JsonResponse({'error': 'مقادیر نامعتبر هستند'}, status=400)
        new_comment = ArticleComment(article_id=article_id, text=article_comment, user_id=request.user.id,
                                     parent_id=parent_id if parent_id else None)
        new_comment.save()
        context = {
            'comments': ArticleComment.objects.filter(article_id=article_id,
             parent=None).order_by('create_date').prefetch_related('articlecomment_set'),
            'comments_count': ArticleComment.objects.filter(article_id=article_id).count()
        }
        return render(request, 'article_modules/include/article_comment_partial.html', context)
    return JsonResponse({'error': 'درخواست نامعتبر'}, status=400)



