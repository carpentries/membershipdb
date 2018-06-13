# Generated by Django 2.0.6 on 2018-06-13 16:29

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import djmoney.models.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_auto_20180612_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='domain',
        ),
        migrations.RemoveField(
            model_name='membershipterm',
            name='instrucutor',
        ),
        migrations.RemoveField(
            model_name='membershipterm',
            name='name',
        ),
        migrations.RemoveField(
            model_name='membershipterm',
            name='num_org_workshop',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='has_active',
        ),
        migrations.AddField(
            model_name='membership',
            name='annual_fee_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('XUA', 'ADB Unit of Account'), ('AFN', 'Afghani'), ('DZD', 'Algerian Dinar'), ('ARS', 'Argentine Peso'), ('AMD', 'Armenian Dram'), ('AWG', 'Aruban Guilder'), ('AUD', 'Australian Dollar'), ('AZN', 'Azerbaijanian Manat'), ('BSD', 'Bahamian Dollar'), ('BHD', 'Bahraini Dinar'), ('THB', 'Baht'), ('PAB', 'Balboa'), ('BBD', 'Barbados Dollar'), ('BYN', 'Belarussian Ruble'), ('BYR', 'Belarussian Ruble'), ('BZD', 'Belize Dollar'), ('BMD', 'Bermudian Dollar (customarily known as Bermuda Dollar)'), ('BTN', 'Bhutanese ngultrum'), ('VEF', 'Bolivar Fuerte'), ('BOB', 'Boliviano'), ('XBA', 'Bond Markets Units European Composite Unit (EURCO)'), ('BRL', 'Brazilian Real'), ('BND', 'Brunei Dollar'), ('BGN', 'Bulgarian Lev'), ('BIF', 'Burundi Franc'), ('XOF', 'CFA Franc BCEAO'), ('XAF', 'CFA franc BEAC'), ('XPF', 'CFP Franc'), ('CAD', 'Canadian Dollar'), ('CVE', 'Cape Verde Escudo'), ('KYD', 'Cayman Islands Dollar'), ('CLP', 'Chilean peso'), ('XTS', 'Codes specifically reserved for testing purposes'), ('COP', 'Colombian peso'), ('KMF', 'Comoro Franc'), ('CDF', 'Congolese franc'), ('BAM', 'Convertible Marks'), ('NIO', 'Cordoba Oro'), ('CRC', 'Costa Rican Colon'), ('HRK', 'Croatian Kuna'), ('CUP', 'Cuban Peso'), ('CUC', 'Cuban convertible peso'), ('CZK', 'Czech Koruna'), ('GMD', 'Dalasi'), ('DKK', 'Danish Krone'), ('MKD', 'Denar'), ('DJF', 'Djibouti Franc'), ('STD', 'Dobra'), ('DOP', 'Dominican Peso'), ('VND', 'Dong'), ('XCD', 'East Caribbean Dollar'), ('EGP', 'Egyptian Pound'), ('SVC', 'El Salvador Colon'), ('ETB', 'Ethiopian Birr'), ('EUR', 'Euro'), ('XBB', 'European Monetary Unit (E.M.U.-6)'), ('XBD', 'European Unit of Account 17(E.U.A.-17)'), ('XBC', 'European Unit of Account 9(E.U.A.-9)'), ('FKP', 'Falkland Islands Pound'), ('FJD', 'Fiji Dollar'), ('HUF', 'Forint'), ('GHS', 'Ghana Cedi'), ('GIP', 'Gibraltar Pound'), ('XAU', 'Gold'), ('XFO', 'Gold-Franc'), ('PYG', 'Guarani'), ('GNF', 'Guinea Franc'), ('GYD', 'Guyana Dollar'), ('HTG', 'Haitian gourde'), ('HKD', 'Hong Kong Dollar'), ('UAH', 'Hryvnia'), ('ISK', 'Iceland Krona'), ('INR', 'Indian Rupee'), ('IRR', 'Iranian Rial'), ('IQD', 'Iraqi Dinar'), ('IMP', 'Isle of Man Pound'), ('JMD', 'Jamaican Dollar'), ('JOD', 'Jordanian Dinar'), ('KES', 'Kenyan Shilling'), ('PGK', 'Kina'), ('LAK', 'Kip'), ('KWD', 'Kuwaiti Dinar'), ('AOA', 'Kwanza'), ('MMK', 'Kyat'), ('GEL', 'Lari'), ('LVL', 'Latvian Lats'), ('LBP', 'Lebanese Pound'), ('ALL', 'Lek'), ('HNL', 'Lempira'), ('SLL', 'Leone'), ('LSL', 'Lesotho loti'), ('LRD', 'Liberian Dollar'), ('LYD', 'Libyan Dinar'), ('SZL', 'Lilangeni'), ('LTL', 'Lithuanian Litas'), ('MGA', 'Malagasy Ariary'), ('MWK', 'Malawian Kwacha'), ('MYR', 'Malaysian Ringgit'), ('TMM', 'Manat'), ('MUR', 'Mauritius Rupee'), ('MZN', 'Metical'), ('MXV', 'Mexican Unidad de Inversion (UDI)'), ('MXN', 'Mexican peso'), ('MDL', 'Moldovan Leu'), ('MAD', 'Moroccan Dirham'), ('BOV', 'Mvdol'), ('NGN', 'Naira'), ('ERN', 'Nakfa'), ('NAD', 'Namibian Dollar'), ('NPR', 'Nepalese Rupee'), ('ANG', 'Netherlands Antillian Guilder'), ('ILS', 'New Israeli Sheqel'), ('RON', 'New Leu'), ('TWD', 'New Taiwan Dollar'), ('NZD', 'New Zealand Dollar'), ('KPW', 'North Korean Won'), ('NOK', 'Norwegian Krone'), ('PEN', 'Nuevo Sol'), ('MRO', 'Ouguiya'), ('TOP', 'Paanga'), ('PKR', 'Pakistan Rupee'), ('XPD', 'Palladium'), ('MOP', 'Pataca'), ('PHP', 'Philippine Peso'), ('XPT', 'Platinum'), ('GBP', 'Pound Sterling'), ('BWP', 'Pula'), ('QAR', 'Qatari Rial'), ('GTQ', 'Quetzal'), ('ZAR', 'Rand'), ('OMR', 'Rial Omani'), ('KHR', 'Riel'), ('MVR', 'Rufiyaa'), ('IDR', 'Rupiah'), ('RUB', 'Russian Ruble'), ('RWF', 'Rwanda Franc'), ('XDR', 'SDR'), ('SHP', 'Saint Helena Pound'), ('SAR', 'Saudi Riyal'), ('RSD', 'Serbian Dinar'), ('SCR', 'Seychelles Rupee'), ('XAG', 'Silver'), ('SGD', 'Singapore Dollar'), ('SBD', 'Solomon Islands Dollar'), ('KGS', 'Som'), ('SOS', 'Somali Shilling'), ('TJS', 'Somoni'), ('SSP', 'South Sudanese Pound'), ('LKR', 'Sri Lanka Rupee'), ('XSU', 'Sucre'), ('SDG', 'Sudanese Pound'), ('SRD', 'Surinam Dollar'), ('SEK', 'Swedish Krona'), ('CHF', 'Swiss Franc'), ('SYP', 'Syrian Pound'), ('BDT', 'Taka'), ('WST', 'Tala'), ('TZS', 'Tanzanian Shilling'), ('KZT', 'Tenge'), ('XXX', 'The codes assigned for transactions where no currency is involved'), ('TTD', 'Trinidad and Tobago Dollar'), ('MNT', 'Tugrik'), ('TND', 'Tunisian Dinar'), ('TRY', 'Turkish Lira'), ('TMT', 'Turkmenistan New Manat'), ('TVD', 'Tuvalu dollar'), ('AED', 'UAE Dirham'), ('XFU', 'UIC-Franc'), ('USD', 'US Dollar'), ('USN', 'US Dollar (Next day)'), ('UGX', 'Uganda Shilling'), ('CLF', 'Unidad de Fomento'), ('COU', 'Unidad de Valor Real'), ('UYI', 'Uruguay Peso en Unidades Indexadas (URUIURUI)'), ('UYU', 'Uruguayan peso'), ('UZS', 'Uzbekistan Sum'), ('VUV', 'Vatu'), ('CHE', 'WIR Euro'), ('CHW', 'WIR Franc'), ('KRW', 'Won'), ('YER', 'Yemeni Rial'), ('JPY', 'Yen'), ('CNY', 'Yuan Renminbi'), ('ZMK', 'Zambian Kwacha'), ('ZMW', 'Zambian Kwacha'), ('ZWD', 'Zimbabwe Dollar A/06'), ('ZWN', 'Zimbabwe dollar A/08'), ('ZWL', 'Zimbabwe dollar A/09'), ('PLN', 'Zloty')], default='USD', editable=False, max_length=3),
        ),
        migrations.AddField(
            model_name='membershipterm',
            name='mem_type',
            field=models.CharField(choices=[('SS', 'Standard Silver'), ('CS', 'Corporate Silver'), ('SG', 'Standard Gold'), ('SP', 'Standard Platinum'), ('CP', 'Coordinated Platinum'), ('SC', 'SWC Contract'), ('DC', 'DC Contract'), ('CT', 'Contract')], default='CT', help_text='Descriptive name for membership', max_length=2, verbose_name='Membership type'),
        ),
        migrations.AddField(
            model_name='membershipterm',
            name='n_instructors',
            field=models.SmallIntegerField(default=0, help_text='how many instructors can be trained with membership', verbose_name='Number of instructors'),
        ),
        migrations.AddField(
            model_name='membershipterm',
            name='n_workshops',
            field=models.SmallIntegerField(default=0, help_text='Number of organized workshops that come with membership', verbose_name='Number of workshops'),
        ),
        migrations.AddField(
            model_name='person',
            name='title',
            field=models.CharField(blank=True, help_text='Title of the person in the organization', max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='agreement',
            field=models.URLField(blank=True, help_text='GitHub repo link for agreement text', null=True, verbose_name='Agreement Github link'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='annual_fee',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), default_currency='USD', help_text='Annual Fee paid in USD', max_digits=10, verbose_name='Annual fee'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='event',
            field=models.URLField(blank=True, help_text='URLs in AMY for Training event', null=True, verbose_name='Event'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='event_status',
            field=models.CharField(blank=True, choices=[('CP', 'Complete'), ('SD', 'Scheduled'), ('PD', 'Pending')], default='PD', help_text='Have we held instructor training for them yet?', max_length=9, null=True, verbose_name='Event status'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='expires',
            field=models.DateTimeField(help_text='Calculated as start date plus membership term duration', verbose_name='Expiring date'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='hubspot',
            field=models.URLField(blank=True, help_text='Hubspot link to member', null=True, verbose_name='Hubspot link'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='invoice_request',
            field=models.CharField(blank=True, choices=[('PD', 'Paid'), ('ST', 'Sent'), ('RQ', 'Requested'), ('NR', 'Not Ready to Request'), ('NF', 'Request from NumFOCUS')], help_text='Status of invoice', max_length=18, null=True, verbose_name='Invoice request'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='member_type',
            field=models.ForeignKey(help_text='Type of membership', on_delete=django.db.models.deletion.CASCADE, to='membership.MembershipTerm'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='new_renew',
            field=models.CharField(choices=[('N', 'New'), ('R', 'Renew')], default='N', help_text='Is it a new membership or is it a renewal?', max_length=1, verbose_name='New or renew?'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(help_text='Long form name of member', on_delete=django.db.models.deletion.CASCADE, to='membership.Organization'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='paid_in_full',
            field=models.BooleanField(help_text='Did they pay all their membership up-front?', verbose_name='Paid in full?'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='start_date',
            field=models.DateTimeField(help_text='The starting date for the membership', verbose_name='Starting date'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='status',
            field=models.CharField(choices=[('PD', 'Pending'), ('OS', 'Out for Signatures'), ('AC', 'Active'), ('DT', 'Dormant'), ('EX', 'Expired'), ('LD', 'Lead'), ('ST', 'Stale')], default='LD', help_text='Current status of membership', max_length=2, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='membershipterm',
            name='coordinate',
            field=models.BooleanField(help_text='Do they have a workshop coordinator offered up as in-kind effort?', verbose_name='Offered coordinator?'),
        ),
        migrations.AlterField(
            model_name='membershipterm',
            name='inh_trainer',
            field=models.BooleanField(help_text='Do they have an inhouse trainer?', verbose_name='Inhouse trainer?'),
        ),
        migrations.AlterField(
            model_name='membershipterm',
            name='loc_train',
            field=models.BooleanField(help_text='Are they eligible for local training?', verbose_name='Local training?'),
        ),
        migrations.AlterField(
            model_name='membershipterm',
            name='publicize',
            field=models.BooleanField(help_text='Will we publicize the membership?', verbose_name='Publicize?'),
        ),
        migrations.AlterField(
            model_name='membershipterm',
            name='recruit',
            field=models.BooleanField(help_text='Will we help them recruit?', verbose_name='Recruit help?'),
        ),
        migrations.AlterField(
            model_name='membershipterm',
            name='reserve',
            field=models.BooleanField(help_text='Do we reserve seats in trainings?', verbose_name='Reserved seats?'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='country',
            field=django_countries.fields.CountryField(help_text='Country of the organization', max_length=2, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='domain',
            field=models.URLField(blank=True, help_text='URL/domain of the organization', null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='members',
            field=models.ForeignKey(blank=True, help_text='The names of those members if umbrella', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='membership.Organization'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(help_text='Long/official name', max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='shortname',
            field=models.CharField(help_text='Short name', max_length=10, unique=True, verbose_name='Short name'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='umbrella',
            field=models.BooleanField(help_text='Does this membership cover other organizations under its “umbrella”?', verbose_name='Is umbrella?'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='vendor_reg',
            field=models.BooleanField(help_text='Are they registered as a vendor with CI?', verbose_name='Reistered vendor?'),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(blank=True, help_text='Snail mail address', max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='person',
            name='advisory_council',
            field=models.BooleanField(help_text='Is the advisory council representative?', verbose_name='Council representative?'),
        ),
        migrations.AlterField(
            model_name='person',
            name='billing_contact',
            field=models.BooleanField(help_text='Should be the primary billing contact?', verbose_name='Billing contact?'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, help_text='Email address', max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='person',
            name='hubspot',
            field=models.URLField(blank=True, help_text='Link to their Hubspot record', null=True, verbose_name='Hubspot link'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(help_text="Contact's last name", max_length=50, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='member_contact',
            field=models.BooleanField(help_text='Should be the primary member contact?', verbose_name='Primary contact?'),
        ),
        migrations.AlterField(
            model_name='person',
            name='merger_notify',
            field=models.BooleanField(help_text='Have they been notified of the SWC/DC merger?', verbose_name='Notified of merger?'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(help_text="Contact's first name", max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='nf2nci_letter',
            field=models.BooleanField(help_text='Did they respond to the NumFOCUS to CI assignment letter?', verbose_name='Respond assignment letter?'),
        ),
        migrations.AlterField(
            model_name='person',
            name='organization',
            field=models.ForeignKey(help_text='Organization with which the person is associated', on_delete=django.db.models.deletion.CASCADE, to='membership.Organization'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Phone number in + notation', max_length=128, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='person',
            name='signatory',
            field=models.BooleanField(help_text='Does this person sign agreements?', verbose_name='Is signatory?'),
        ),
        migrations.AlterField(
            model_name='person',
            name='trainer',
            field=models.BooleanField(help_text='Is this person an instructor trainer?', verbose_name='Is trainer?'),
        ),
    ]