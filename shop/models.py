from django.db import models
from django.db.models.fields import BooleanField
from django.utils.safestring import mark_safe
from django_resized import ResizedImageField


class Material(models.Model):
    name = models.CharField(verbose_name='Материал изделия', max_length=30, unique=True)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
        db_table = 'material'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name='Категория изделия', max_length=30, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'category'

    def __str__(self):
        return self.name


class Gem(models.Model):
    name = models.CharField(verbose_name='Драгоценный камень', max_length=30, unique=True)
    choice = BooleanField(verbose_name='Наличие', null=True)

    class Meta:
        verbose_name = 'Драгоценный камень'
        verbose_name_plural = 'Драгоценные камни'
        db_table = 'gem'

    def __str__(self):
        return self.name


class Photo(models.Model):
    def set_file_directory(self, filename):
        return (f'{self.decoration.category}/{self.decoration.name}/{filename}')

    photo = ResizedImageField(verbose_name='Изображение', size=[900, 900], upload_to=set_file_directory,
                              blank=True, null=True)
    decoration = models.ForeignKey('Decoration', on_delete=models.CASCADE, related_name='decoration_photo',
                                   verbose_name='Название изделия', blank=True, null=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        db_table = 'photo'

    def __str__(self):
        return self.photo.path

    def display_image(self):
        return mark_safe(f'<img src="{self.photo.url}"width="100" height="100"')

    display_image.short_description = 'Изображение'


class Decoration(models.Model):
    name = models.CharField(verbose_name='Название изделия', max_length=250, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='category',
                                 verbose_name='Категория', null=True)
    material = models.ManyToManyField(Material, verbose_name='Материал', blank=True)
    gem = models.ManyToManyField(Gem, verbose_name='Драгоценные камни', blank=True)
    description = models.TextField(verbose_name='Описание', max_length=1500, blank=True, null=True)

    class Meta:
        verbose_name = 'Украшение'
        verbose_name_plural = 'Украшения'
        db_table = 'decoration'

    def __str__(self):
        return self.name

    def display_gems(self):
        return "\n, ".join([gem.name for gem in self.gem.all()])

    display_gems.short_description = 'Драгоценные камни'

    def display_material(self):
        return "\n, ".join([material.name for material in self.material.all()])

    display_material.short_description = 'Материал'

    def display_images(self):
        try:
            images = ''
            for image in self.decoration_photo.all():
                images += (f'<img src="{image.photo.url}" width="100" height="100">')
            return mark_safe(images)
        except (AttributeError, ValueError):
            return None

    display_images.short_description = 'Изображение'


class MainPhoto(models.Model):
    photo = ResizedImageField(verbose_name='Главное фото', size=[1200, 900], upload_to='Главное фото',
                              blank=True, null=True)
    content = models.TextField(verbose_name='Приветствие', max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'Главное фото сайта и приветствие'
        verbose_name_plural = 'Главное фото сайта и приветствие'
        db_table = 'mainphoto'

    def __str__(self):
        return f'Path: {self.photo.path}'

    def display_image(self):
        try:
            return mark_safe(f'<img src="{self.photo.url}" "width="750" height="500">')
        except (AttributeError, ValueError):
            return None
    display_image.short_description = 'Главное фото'


class SocialNetwork(models.Model):
    name = models.CharField(verbose_name='Название соцсети', max_length=20, unique=True, null=False)
    link = models.CharField(verbose_name='Ссылка на аккаунт', max_length=200, unique=True, null=False)
    svg_link = models.CharField(verbose_name='Ссылка на svg', max_length=200, unique=True, null=False,
                                help_text='https://boxicons.com/, найти иконку, выбрать её, далее выбрать параметр Font'
                                          'и скопировать тег i')

    class Meta:
        verbose_name = 'Соцсеть'
        verbose_name_plural = 'Соцсети'
        db_table = 'socialnetwork'

    def __str__(self):
        return (f'name: {self.name}, link: {self.link}, svg_link: {self.svg_link}')


class MaterialsText(models.Model):
    content = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Текст категории материалы'
        verbose_name_plural = 'Текст категории материалы'
        db_table = 'materialstext'

    def __str__(self):
        return f'content: {self.content}'


class ContactsText(models.Model):
    content = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Текст категории контакты'
        verbose_name_plural = 'Текст категории контакты'
        db_table = 'contactstext'

    def __str__(self):
        return f'content: {self.content}'


class DeliveryText(models.Model):
    content = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Текст категории доставка'
        verbose_name_plural = 'Текст категории доставка'
        db_table = 'deliverytext'

    def __str__(self):
        return f'content: {self.content}'


class PaymentText(models.Model):
    content = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Текст категории оплата'
        verbose_name_plural = 'Текст категории оплата'
        db_table = 'paymenttext'

    def __str__(self):
        return f'content: {self.content}'
