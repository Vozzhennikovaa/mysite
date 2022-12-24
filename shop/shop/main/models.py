from django.db import models
from django.urls import reverse

# Модель категорий
class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Ссылка')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('main:product_list_by_category', args=[self.slug])

# Модель продуктов
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, db_index=True, verbose_name='Наименование') 
    slug = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Ссылка') 
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
    upload = models.DateTimeField(auto_now=True, verbose_name='Обновлён')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.id, self.slug])



# Модель статус заказа
# class Status(models.Model):
#     orderstatus = models.CharField(max_length=100,db_index=True, verbose_name='Статус заказа')
#     # slug = models.SlugField(max_length=100, unique=True, verbose_name='Ссылка')
#     class Meta:
#         ordering = ('orderstatus',)
#         verbose_name = 'Статус заказа'
#         verbose_name_plural = 'Статус заказа'

#     def __str__(self):
#         return self.orderstatus

# Модель статус заказа
# class Delivery(models.Model):
#     delivery = models.CharField(max_length=50,db_index=True, verbose_name='Способ получения')
#     # slug = models.SlugField(max_length=50, unique=True, verbose_name='Ссылка')
#     class Meta:
#         ordering = ('delivery',)
#         verbose_name = 'Способ получения'
#         verbose_name_plural = 'Способ получения'

#     def __str__(self):
#         return self.delivery

# Модель заказов
class Orders(models.Model):

    # status = models.ForeignKey(Status, related_name='orders', on_delete=models.CASCADE, verbose_name='Статус') #статус заказа
   
    # slug = models.SlugField(max_length=100, unique=True, verbose_name='Ссылка')
    person = models.TextField(max_length=150, blank=True, verbose_name='Имя заказчика')
    email = models.TextField(max_length=150, blank=True, verbose_name='Email заказчика')
    delivery = models.TextField(max_length=150, blank=True, verbose_name='Способ получения') #статус заказа
    
    adress = models.TextField(max_length=150, blank=True, verbose_name='Адрес доставки')
    date = models.DateField(max_length=50, blank=True, verbose_name='Дата доставки')
    time = models.TimeField(max_length=20, blank=True, verbose_name='Время доставки')

    comment = models.TextField(max_length=150, blank=True, verbose_name='Комментарий к заказу')
    # product = models.TextField(max_length=200, blank=True, verbose_name='Товар')
    # items = models.TextField(max_length=100, blank=True, verbose_name='Всего товаров')
    # price = models.TextField(max_length=50, blank=True, verbose_name='К оплате')
    
   
    class Meta:
        ordering = ('person',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        # index_together = (('id', 'slug'))

    def __str__(self):
        return self.person


    
# Модель страниц
class Pages(models.Model):
    name = models.CharField(max_length=100,db_index=True, verbose_name='Название страницы')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Ссылка')
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_list_by_pages', args=[self.slug])    

# Модель записей
class Articles(models.Model):
    pages = models.ForeignKey(Pages, related_name='pages', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, db_index=True, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Ссылка') 
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлена')
    upload = models.DateTimeField(auto_now=True, verbose_name='Обновлена')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        index_together = (('id', 'slug'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:Articles_detail', args=[self.id, self.slug])     


       