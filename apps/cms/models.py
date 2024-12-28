from django.db import models

class Article(models.Model):
    """
    Model for articles and blog posts.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='articles'
    )
    chambers = models.ForeignKey(
        'chambers.Chambers',
        on_delete=models.CASCADE,
        related_name='articles',
        null=True,
        blank=True
    )
    practice_areas = models.ManyToManyField(
        'practice_areas.PracticeArea',
        related_name='articles'
    )
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class NotableCase(models.Model):
    """
    Model for notable cases.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    chambers = models.ForeignKey(
        'chambers.Chambers',
        on_delete=models.CASCADE,
        related_name='notable_cases',
        null=True,
        blank=True
    )
    barrister = models.ForeignKey(
        'barristers.Barrister',
        on_delete=models.CASCADE,
        related_name='notable_cases',
        null=True,
        blank=True
    )
    practice_areas = models.ManyToManyField(
        'practice_areas.PracticeArea',
        related_name='notable_cases'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
