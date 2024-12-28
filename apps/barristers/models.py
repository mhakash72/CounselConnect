from django.db import models

class Barrister(models.Model):
    """
    Model for barrister profiles, including both chambers and direct access barristers.
    """
    user = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='barrister_profile'
    )
    chambers = models.ForeignKey(
        'chambers.Chambers',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='barristers'
    )
    practice_areas = models.ManyToManyField(
        'practice_areas.PracticeArea',
        related_name='barristers'
    )
    is_direct_access = models.BooleanField(default=False)
    year_of_call = models.IntegerField()
    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        blank=True,
        null=True
    )
    bio = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)
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
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()}"
