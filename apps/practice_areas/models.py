from django.db import models

class PracticeArea(models.Model):
    """
    Model for practice areas with hierarchical structure.
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )
    level = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_selectable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Practice Area'
        verbose_name_plural = 'Practice Areas'

    def __str__(self):
        return self.name

    @property
    def is_root(self):
        return self.parent is None
