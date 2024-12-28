from django.db import models

class Chambers(models.Model):
    """
    Model for chambers information and management.
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(
        upload_to='chambers_logos/',
        blank=True,
        null=True
    )
    website = models.URLField(blank=True)
    is_claimed = models.BooleanField(default=False)
    claimed_by = models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='claimed_chambers'
    )
    practice_areas = models.ManyToManyField(
        'practice_areas.PracticeArea',
        related_name='chambers'
    )
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True)
    subscription_status = models.CharField(
        max_length=20,
        choices=[
            ('TRIAL', 'Free Trial'),
            ('LISTING', 'Listing'),
            ('GROWTH', 'Growth'),
        ],
        default='TRIAL'
    )
    trial_leads_remaining = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'chambers'

    def __str__(self):
        return self.name

class Office(models.Model):
    """
    Model for chambers offices.
    """
    chambers = models.ForeignKey(
        Chambers,
        on_delete=models.CASCADE,
        related_name='offices'
    )
    name = models.CharField(max_length=255)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    practice_areas = models.ManyToManyField(
        'practice_areas.PracticeArea',
        related_name='offices'
    )

    def __str__(self):
        return f"{self.chambers.name} - {self.name}"
