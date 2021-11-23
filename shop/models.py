from django.db import models
from django.db.models.fields import BooleanField
from django.utils.safestring import mark_safe
from django_resized import ResizedImageField


class Material(models.Model):
    name = models.CharField(max_length=30, verbose_name='Материал изделия',
                            unique=True)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30,
                            verbose_name='Категория изделия',
                            unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Gem(models.Model):
    name = models.CharField(max_length=30, verbose_name='Драгоценный камень',
                            unique=True)
    choice = BooleanField(verbose_name='Наличие', null=True)

    class Meta:
        verbose_name = 'Драгоценный камень'
        verbose_name_plural = 'Драгоценные камни'

    def __str__(self):
        return self.name


class Photo(models.Model):
    def set_file_directory(self, filename):
        return (f'{self.decoration.category}/'
                f'{self.decoration.name}/{filename}')

    name = ResizedImageField(size=[900, 900], upload_to=set_file_directory,
                             verbose_name='Изображение',
                             blank=True, null=True)
    decoration = models.ForeignKey('Decoration', on_delete=models.CASCADE,
                                   verbose_name='Название изделия',
                                   blank=True, null=True, related_name='image')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.name.path

    def display_image(self):
        return mark_safe(f'<img src="{self.name.url}"width="100" height="100"')

    display_image.short_description = 'Изображение'


class Decoration(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название изделия',
                            unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, verbose_name='Категория',
                                 related_name='categ')
    material = models.ManyToManyField(Material, verbose_name='Материал',
                                      blank=True)
    gem = models.ManyToManyField(Gem, verbose_name='Драгоценные камни',
                                 blank=True)
    description = models.TextField(max_length=1500, verbose_name='Описание',
                                   null=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True,
                                verbose_name='Цена')

    class Meta:
        verbose_name = 'Украшение'
        verbose_name_plural = 'Украшения'

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
            for image in self.image.all():
                images += (f'<img src="{image.name.url}"'
                           f'height="100" width="100"/>')
            return mark_safe(images)
        except (AttributeError, ValueError):
            return None
    display_images.short_description = 'Изображение'


class MainPhoto(models.Model):
    main_photo = ResizedImageField(size=[1200, 900],
                                   upload_to='main_photo',
                                   verbose_name='Главное фото',
                                   blank=True, null=True)
    greetings = models.TextField(max_length=500, verbose_name='Приветствие',
                                 null=True, blank=True)

    def __str__(self):
        return f'Path: {self.main_photo.path}'

    def display_image(self):
        try:
            return mark_safe(f'<img src="{self.main_photo.url}'
                             f'"width="750" height="500"')
        except (AttributeError, ValueError):
            return None
    display_image.short_description = 'Главное фото'

    class Meta:
        verbose_name = 'Главное фото сайта и приветствие'
        verbose_name_plural = 'Главное фото сайта и приветствие'


class SocialNetwork(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название соцсети',
                            unique=True, null=False,
                            help_text='Название соцсети')
    link = models.CharField(max_length=200, verbose_name='Ссылка на аккаунт',
                            unique=True, null=False)
    svg_link = models.CharField(max_length=200,
                                verbose_name='Ссылка на svg',
                                unique=True, null=False,
                                help_text='https://boxicons.com/, '
                                'найти иконку, выбрать её, '
                                'далее выбрать параметр Font '
                                'и скопировать тег i')

    def __str__(self):
        return f'name: {self.name}, link: {self.link}'

    class Meta:
        verbose_name = 'Соцсеть'
        verbose_name_plural = 'Соцсети'


class MaterialsText(models.Model):
    content = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'content: {self.content}'

    class Meta:
        verbose_name = 'Текст категории материалы'
        verbose_name_plural = 'Текст категории материалы'


class ContactsText(models.Model):
    content = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'content: {self.content}'

    class Meta:
        verbose_name = 'Текст категории контакты'
        verbose_name_plural = 'Текст категории контакты'


class DeliveryText(models.Model):
    content = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'content: {self.content}'

    class Meta:
        verbose_name = 'Текст категории доставка'
        verbose_name_plural = 'Текст категории доставка'


class PaymentText(models.Model):
    content = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'content: {self.content}'

    class Meta:
        verbose_name = 'Текст категории оплата'
        verbose_name_plural = 'Текст категории оплата'
