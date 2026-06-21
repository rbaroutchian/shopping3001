from django.db import models
from django.urls import reverse


# Create your models here.
class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name="عنوان")
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در  url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'دسته بندی'
        verbose_name_plural='دسته بندی ها'

class ProductBrand(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='نام برند')
    is_Active = models.BooleanField(verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'برند'
        verbose_name_plural='برندها'


class ProductTag(models.Model):
    caption = models.CharField(max_length=200, verbose_name='عنوان تگ')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name= 'تگ '
        verbose_name_plural='تگ ها'


class Product(models.Model):
    title = models.CharField(max_length=200, db_index=True , verbose_name="عنوان محصولات")
    category = models.ForeignKey(ProductCategory, db_index=True ,
                                 on_delete=models.CASCADE , null=True, verbose_name='دسته بندی محصول',
                                 related_name='ProductCategory')

    product_Tag = models.ManyToManyField(ProductTag, verbose_name='تگ محصول' ,)
    product_brand = models.ForeignKey(ProductBrand, db_index=True ,
                                      on_delete=models.CASCADE,
                                      verbose_name='برند محصول')
    price = models.IntegerField(default=0, verbose_name='قیمت')

    short_description = models.CharField(max_length=400, db_index=True ,null=True ,
                                         verbose_name='توضیحات کوتاه')
    description = models.TextField(null=True , verbose_name='توضیحات تکمیلی محصول')

    image = models.ImageField(upload_to='products/', default='products/default.jpg',
                              verbose_name='تصویر')

    slug = models.CharField(max_length=300, default='', null=True ,blank=True,
                             db_index=True,
                             verbose_name='عنوان در url',)
    is_active = models.BooleanField(default=True, db_index=True ,verbose_name='فعال / غیر فعال')
    is_deleted= models.BooleanField(default=False, verbose_name='حذف / حذف نشد')


    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'



