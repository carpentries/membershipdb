from django.db import models

class MembershipTerm(models.Model):
    TYPE_CHOICES = (
        ('SS','Standard Silver'),
        ('CS','Corporate Silver'),
        ('SG','Standard Gold'),
        ('SP','Standard Platinum'),
        ('CP','Coordinated Platinum'),
        ('SW','SWC Contract'),
        ('DC','DC Contract'),
        ('CT','Contract'),
    )

    name = models.CharField(max_length=2, choices=TYPE_CHOICES, default='CT')
    num_org_workshop = models.SmallIntegerField()
    instrucutor = models.SmallIntegerField()
    reserve = models.BooleanField()
    inh_trainer = models.BooleanField()
    loc_train = models.BooleanField()
    publicize = models.BooleanField()
    recruit = models.BooleanField()
    coordinate = models.BooleanField()

class Organization(models.Model):
    name = models.CharField(max_length=100)
    shortname = models.CharField(max_length=10)
    country = models.CharField(max_length=2)
    has_active = models.BooleanField() # Calculated from Memebership active
    domain = models.URLField()
    umbrella = models.BooleanField()
    members = models.ForeignKey(
        'self',
        null=True,
        related_name='contact',
        on_delete=models.CASCADE
    )
    vendor_reg = models.BooleanField()

class Person(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    advisory_council = models.BooleanField()
    signatory = models.BooleanField()
    member_contact = models.BooleanField()
    billing_contact = models.BooleanField()
    trainer = models.BooleanField()
    merger_notify = models.BooleanField()
    nf2nci_letter = models.BooleanField()
    hubspot = models.URLField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)

class Membership(models.Model):
    STATUS_CHOICES = (
        ('PD', 'Pending'), #- In discussion that we really confident will lead to membership
        ('OS', 'Out for Signatures'), #- Agreement has been sent out for signatures (membership eminent)
        ('AC', 'Active'), #- Agreement has been signed and term of agreement has started
        ('DT', 'Dormant'), #- Agreement has been signed but term of agreement has not started
        ('EX', 'Expired'), #- Term of agreement has ended
        ('LD', 'Lead'), #- Interest in membership has been expressed, but an agreement may or may not be likely
        ('ST','Stale'), #- At one point was pending or lead, but a membership does now not seem likely
    )

    NEW_RENEW_CHOICES = (
        ('N', 'New'),
        ('R', 'Renew'),
    )

    INVOICE_REQUEST = (
        ('PAID','Paid'),
        ('SENT','Sent'),
        ('REQUESTED','Requested'),
        ('NOT READY','Not Ready to Request'),
        ('NUMFOCUS','Request from NumFOCUS'),
    )

    EVENT_STATUS = (
        ('COMPLETE','Complete'),
        ('SCHEDULED','Scheduled'),
        ('PENDING','Pending'),
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )               
    member_type = models.ForeignKey(
        MembershipTerm,
        on_delete=models.CASCADE
    )
    domain = models.URLField(max_length=50)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='LD')
    new_renew = models.CharField(max_length=1, choices=NEW_RENEW_CHOICES, default='N')
    hubspot = models.URLField()
    annual_fee = models.CharField(max_length=50)
    paid_in_full = models.BooleanField()
    start_date = models.DateTimeField()
    expires = models.DateTimeField()
    agreement = models.URLField()
    invoice_request = models.CharField(max_length=18, choices=INVOICE_REQUEST)
    event_status = models.CharField(max_length=9, choices=EVENT_STATUS, default='PENDING')
    event = models.URLField()


# class Notes(models.Model):
    
