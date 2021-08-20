from django.db import models
from django.utils.safestring import mark_safe


class Material(models.Model):
    material = models.CharField(max_length=30, verbose_name="Материал изделия",
                                unique=True)

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return self.material


class Category(models.Model):
    category = models.CharField(max_length=30,
                                verbose_name="Категория изделия",
                                unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.category


class Gems(models.Model):
    gems = models.CharField(max_length=30, verbose_name="Драгоценный камень",
                            unique=True)

    class Meta:
        verbose_name = "Драгоценный камень"
        verbose_name_plural = "Драгоценные камни"

    def __str__(self):
        return self.gems


class Images(models.Model):
    image = models.ImageField(upload_to='', verbose_name='Изображение',
                              blank=True, null=True)
    decoration = models.ForeignKey('Decorations', on_delete=models.CASCADE,
                                   verbose_name='Название изделия',
                                   blank=True,
                                   null=True)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.image.url

    def display_image(self):
        return mark_safe(f'<img src="{self.image.url}"width="100" height="100"')

    display_image.short_description = 'Изображение'


class Decorations(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название изделия',
                            unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, verbose_name='Категория')
    material = models.ManyToManyField(Material, verbose_name='Материал',
                                      blank=True)
    gems = models.ManyToManyField(Gems, verbose_name='Драгоценные камни',
                                  blank=True)
    description = models.TextField(max_length=1500, verbose_name='Описание',
                                   null=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True,
                                verbose_name='Цена')
    image = models.ManyToManyField(Images, verbose_name='Изображения',
                                   blank=True)

    class Meta:
        verbose_name = "Украшение"
        verbose_name_plural = "Украшения"

    def __str__(self):
        return self.name

    def display_gems(self):
        return "\n, ".join([p.gems for p in self.gems.all()])

    display_gems.short_description = 'Драгоценные камни'

    def display_material(self):
        return "\n, ".join([p.material for p in self.material.all()])

    display_material.short_description = 'Материал'

    def display_image(self):
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!{self.image.all()}')
        return mark_safe(f'<img src="{self.image.filter().first().image.url}"width="100" height="100"')

    display_image.short_description = 'Изображение'
