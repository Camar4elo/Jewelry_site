from django.db import models
from django.utils.safestring import mark_safe


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

    class Meta:
        verbose_name = 'Драгоценный камень'
        verbose_name_plural = 'Драгоценные камни'

    def __str__(self):
        return self.name


class Image(models.Model):
    def set_file_directory(instance, filename):
        return (f'{instance.decoration.category}/'
                f'{instance.decoration.name}/{filename}')

    name = models.ImageField(upload_to=set_file_directory,
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

    def delete(self, *args, **kwargs):
        storage = self.name.storage
        path = self.name.path
        super(Image, self).delete(*args, **kwargs)
        storage.delete(path)


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
