from django.db import models


class Material(models.Model):
    material = models.CharField(max_length=30, help_text="Материал изделия")

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return self.material


class Category(models.Model):
    category = models.CharField(max_length=30, help_text="Категория изделия")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.category


class Decorations(models.Model):
    name = models.CharField(max_length=250, help_text="Название украшения")
    category = models.ManyToManyField(Material)
    material = models.ManyToManyField(Category)

    def __str__(self):
        return (f'<{self.name} {self.category}'
                f'{self.material}>')

    class Meta:
        verbose_name = "Украшение"
        verbose_name_plural = "Украшения"
