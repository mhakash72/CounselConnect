from django.db import models
from django.utils.translation import gettext_lazy as _

class Enquiry(models.Model):
    """
    Model for managing booking enquiries.
    """
    class Status(models.TextChoices):
        NEW = 'NEW', _('New')
        ACKNOWLEDGED = 'ACKNOWLEDGED', _('Acknowledged')
        UNDER_REVIEW = 'UNDER_REVIEW', _('Under Review')
        ACCEPTED = 'ACCEPTED', _('Accepted')
        REJECTED = 'REJECTED', _('Rejected')
        CLOSED = 'CLOSED', _('Closed')

    sender = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='sent_enquiries'
    )
    chambers = models.ManyToManyField(
        'chambers.Chambers',
        related_name='received_enquiries',
        blank=True
    )
    barristers = models.ManyToManyField(
        'barristers.Barrister',
        related_name='received_enquiries',
        blank=True
    )
    practice_area = models.ForeignKey(
        'practice_areas.PracticeArea',
        on_delete=models.SET_NULL,
        null=True
    )
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW
    )
    instruction_type = models.CharField(
        max_length=50,
        choices=[
            ('HEARING', 'Hearing'),
            ('TRIAL', 'Trial'),
            ('ADVICE', 'Advice'),
            ('DRAFTING', 'Drafting Pleadings'),
        ]
    )
    court = models.CharField(max_length=255, blank=True)
    claim_number = models.CharField(max_length=100, blank=True)
    hearing_length = models.CharField(max_length=100, blank=True)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return f"Enquiry {self.id} - {self.instruction_type}"
