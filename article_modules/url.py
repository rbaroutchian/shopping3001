from django.db import models
from django.urls import reverse
from account_modules.models import User
# Create your models here.


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', null=True, blank=True,
                               verbose_name='دسته بندی والد', on_delete=models.CASCADE)
    title = models.CharField(max_length=200,verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=200,verbose_name= 'عنوان در url', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال ')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی های مقاله'



class Article(models.Model):
        title = models.CharField(max_length=300,verbose_name='عنوان')
        slug = models.SlugField(max_length=400, allow_unicode=True, unique=True, verbose_name='عنوان در url')
        image=models.ImageField(upload_to='articles/%Y/%m/%d/', verbose_name='تصویر')
        short_description = models.TextField(verbose_name='توضیحات کوتاه')
        text = models.TextField(verbose_name='توضیحات')
        is_Active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
        selected_category = models.ManyToManyField(ArticleCategory,verbose_name='دسته بندی مقاله')
        created_date = models.DateTimeField(auto_now_add=True,null=True,editable=False,
                                      verbose_name='تاریخ ثبت مقاله')
        author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', null=True, editable=True)

        def get_absolute_url(self):
            return reverse('article_detail' , args=[self.id])
        def __str__(self):
            return self.title

        # def get_jalali_create_date(self):
        #     return datetime.date
        # def get_jalali_create_time(self):

        class Meta:
            verbose_name='مقاله'
            verbose_name_plural='مقالات'

class ArticleComment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name='مقاله')
    parent = models.ForeignKey('ArticleComment', null=True, blank=True,
                               on_delete=models.CASCADE, related_name='articlecomment_set', verbose_name='والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,verbose_name='کاربر')
    create_date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ثبت',)
    text = models.TextField(verbose_name='متن نظر' , default='نظر')
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(null=True, blank=True, verbose_name='ایمیل')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name= 'نظر مقاله'
        verbose_name_plural= 'نظرات مقاله'