from datetime import datetime

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from djmoney.models.fields import MoneyField
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

class Note(models.Model):
    """
    Generic notes for all the models
    """
    title = models.CharField(
        verbose_name='Note title',
        max_length=64,
        help_text='Title of the Note'
        )
    content = models.TextField(
        verbose_name='Note content',
        max_length=512,
        help_text='Content of the Note'
        )
    date_time = models.DateTimeField(
        verbose_name='Note time',
        default=datetime.now,
        help_text='Date and time of the last update of the note'
        )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class MembershipTerm(models.Model):
    """
    Terms on which are based the different types of Memberships.
    """
    STANDARD_SILVER = 'SS'
    CORPORATE_SILVER = 'CS'
    STANDARD_GOLD = 'SG'
    STANDARD_PLATINUM = 'SP'
    COORDINATED_PLATINUM = 'CP'
    SWC_CONTRACT = 'SC'
    DC_CONTRACT = 'DC'
    CONTRACT = 'CT'

    TYPE_CHOICES = (
        (STANDARD_SILVER,'Standard Silver'),
        (CORPORATE_SILVER,'Corporate Silver'),
        (STANDARD_GOLD,'Standard Gold'),
        (STANDARD_PLATINUM,'Standard Platinum'),
        (COORDINATED_PLATINUM,'Coordinated Platinum'),
        (SWC_CONTRACT,'SWC Contract'),
        (DC_CONTRACT,'DC Contract'),
        (CONTRACT,'Contract'),
    )

    mem_type = models.CharField(
        'Membership type',
        max_length=2,
        choices=TYPE_CHOICES,
        default=CONTRACT,
        help_text='Descriptive name for membership'
        )
    n_workshops = models.SmallIntegerField(
        'Number of workshops',
        default=0,
        help_text='Number of organized workshops that come with membership'
        )
    n_instructors = models.SmallIntegerField(
        'Number of instructors',
        default=0,
        help_text='how many instructors can be trained with membership'
        )
    reserve = models.BooleanField(
        'Reserved seats?',
        help_text='Do we reserve seats in trainings?'
        )
    inh_trainer = models.BooleanField(
        'Inhouse trainer?',
        help_text='Do they have an inhouse trainer?'
        )
    loc_train = models.BooleanField(
        'Local training?',
        help_text='Are they eligible for local training?'
        )
    publicize = models.BooleanField(
        'Publicize?',
        help_text='Will we publicize the membership?'
        )
    recruit = models.BooleanField(
        'Recruit help?',
        help_text='Will we help them recruit?'
        )
    coordinate = models.BooleanField(
        'Offered coordinator?',
        help_text='Do they have a workshop coordinator offered up as in-kind effort?'
        )
    notes = GenericRelation(Note)

class Organization(models.Model):
    """
    Membership organizations.
    """
    name = models.CharField(
        'Name',
        max_length=100,
        help_text='Long/official name'
        )
    shortname = models.CharField(
        'Short name',
        max_length=10,
        help_text='Short name',
        unique=True
        )
    country = CountryField(
        'Country',
        help_text='Country of the organization'
        )
    # has_active = models.SmallIntegerField() Calculated from Membership active
    domain = models.URLField(
        'URL',
        help_text='URL/domain of the organization',
        blank=True, null=True
        )
    umbrella = models.BooleanField(
        'Is umbrella?',
        help_text='Does this membership cover other organizations under its “umbrella”?'
        )
    members = models.ForeignKey(
        'self',
        blank=True, null=True,
        related_name='contact',
        on_delete=models.CASCADE,
        help_text='The names of those members if umbrella'
        )
    vendor_reg = models.BooleanField(
        'Reistered vendor?',
        help_text='Are they registered as a vendor with CI?'
        )
    notes = GenericRelation(Note)

class Person(models.Model):
    """
    Contact persons from organizations.
    """
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        help_text='Organization with which the person is associated'
    )
    name = models.CharField(
        'Name',
        max_length=50,
        help_text='Contact\'s first name'
        )
    last_name = models.CharField(
        'Last name',
        max_length=50,
        help_text='Contact\'s last name'
        )
    title = models.CharField(
        'Title',
        max_length=100,
        help_text='Title of the person in the organization',
        blank=True, null=True
    )
    email = models.EmailField(
        'Email',
        help_text='Email address',
        blank=True, null=True
        )
    advisory_council = models.BooleanField(
        'Council representative?',
        help_text='Is the advisory council representative?'
        )
    signatory = models.BooleanField(
        'Is signatory?',
        help_text='Does this person sign agreements?'
        )
    member_contact = models.BooleanField(
        'Primary contact?',
        help_text='Should be the primary member contact?'
        )
    billing_contact = models.BooleanField(
        'Billing contact?',
        help_text='Should be the primary billing contact?'
        )
    trainer = models.BooleanField( # Could be a lookup to AMY DB
        'Is trainer?', 
        help_text='Is this person an instructor trainer?'
        )
    merger_notify = models.BooleanField(
        'Notified of merger?',
        help_text='Have they been notified of the SWC/DC merger?'
        )
    nf2nci_letter = models.BooleanField(
        'Respond assignment letter?',
        help_text='Did they respond to the NumFOCUS to CI assignment letter?'
        )
    hubspot = models.URLField(
        'Hubspot link',
        help_text='Link to their Hubspot record',
        blank=True, null=True
        )
    address = models.CharField(
        'Address',
        max_length=200,
        help_text='Snail mail address',
        blank=True, null=True
        )
    phone = PhoneNumberField(
        'Phone number',
        help_text='Phone number in + notation',
        blank=True, null=True
        )
    notes = GenericRelation(Note)

class Membership(models.Model):
    """
    Organization memberships.
    """
    PENDING = 'PD'
    OUT4SIGNATURES = 'OS'
    ACTIVE = 'AC'
    DORMANT = 'DT'
    EXPIRED = 'EX'
    LEAD = 'LD'
    STALE = 'ST'

    STATUS_CHOICES = (
        (PENDING, 'Pending'), #- In discussion that we really confident will lead to membership
        (OUT4SIGNATURES, 'Out for Signatures'), #- Agreement has been sent out for signatures (membership eminent)
        (ACTIVE, 'Active'), #- Agreement has been signed and term of agreement has started
        (DORMANT, 'Dormant'), #- Agreement has been signed but term of agreement has not started
        (EXPIRED, 'Expired'), #- Term of agreement has ended
        (LEAD, 'Lead'), #- Interest in membership has been expressed, but an agreement may or may not be likely
        (STALE, 'Stale'), #- At one point was pending or lead, but a membership does now not seem likely
    )

    NEW = 'N'
    RENEW = 'R'

    NEW_RENEW_CHOICES = (
        (NEW, 'New'),
        (RENEW, 'Renew'),
    )

    PAID = 'PD'
    SENT = 'ST'
    REQUESTED = 'RQ'
    NOT_READY = 'NR'
    NUMFOCUS = 'NF'

    INVOICE_REQUEST = (
        (PAID, 'Paid'),
        (SENT, 'Sent'),
        (REQUESTED, 'Requested'),
        (NOT_READY, 'Not Ready to Request'),
        (NUMFOCUS, 'Request from NumFOCUS'),
    )

    COMPLETE = 'CP'
    SCHEDULED = 'SD'
    # PENDING = 'PD' Already defined

    EVENT_STATUS = (
        (COMPLETE, 'Complete'),
        (SCHEDULED, 'Scheduled'),
        (PENDING, 'Pending'),
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        help_text='Long form name of member'
        )
    member_type = models.ForeignKey(
        MembershipTerm,
        on_delete=models.CASCADE,
        help_text='Type of membership'
        )
    status = models.CharField(
        'Status',
        max_length=2,
        choices=STATUS_CHOICES,
        default=LEAD,
        help_text='Current status of membership'
        )
    new_renew = models.CharField(
        'New or renew?',
        max_length=1,
        choices=NEW_RENEW_CHOICES,
        default=NEW,
        help_text='Is it a new membership or is it a renewal?'
        )
    hubspot = models.URLField(
        'Hubspot link',
        help_text='Hubspot link to member',
        blank=True, null=True
        )
    annual_fee = MoneyField(
        'Annual fee',
        max_digits=10,
        decimal_places=2,
        default_currency='USD',
        help_text='Annual Fee paid in USD'
        )
    paid_in_full = models.BooleanField(
        'Paid in full?',
        help_text='Did they pay all their membership up-front?'
        )
    # term calculated field: expires - start_date in years
    start_date = models.DateTimeField(
        'Starting date',
        help_text='The starting date for the membership'
        )
    expires = models.DateTimeField(
        'Expiring date',
        help_text='Calculated as start date plus membership term duration'
        )
    agreement = models.URLField(
        'Agreement Github link',
        help_text='GitHub repo link for agreement text',
        blank=True, null=True
        )
    invoice_request = models.CharField(
        'Invoice request',
        max_length=18, 
        choices=INVOICE_REQUEST,
        help_text='Status of invoice',
        blank=True, null=True
        )
    event_status = models.CharField(
        'Event status',
        max_length=9,
        choices=EVENT_STATUS,
        default=PENDING,
        help_text='Have we held instructor training for them yet?',
        blank=True, null=True
        )
    event = models.URLField(
        'Event',
        help_text='URLs in AMY for Training event',
        blank=True, null=True
        )
    notes = GenericRelation(Note)

    
