from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
import calendar
import datetime



class H2OFlintDeliveryDate(models.Model):
    weekday = models.CharField(max_length=9, null=True, blank=True)
    month = models.CharField(max_length=9, null=True, blank=True)
    date = models.CharField(max_length=2, null=True, blank=True)
    year = models.CharField(max_length=4, default="2016")
    start_time = models.CharField(max_length=8)
    end_time = models.CharField(max_length=8)
    volunteers_needed = models.IntegerField(null=True, blank=True)
    volunteers_scheduled = models.IntegerField(null=True, blank=True)
    vehicles_needed = models.IntegerField(null=True, blank=True)
    vehicles_scheduled = models.IntegerField(null=True, blank=True)
    cases_to_deliver = models.IntegerField(null=True, blank=True)
    cases_delivered = models.IntegerField(null=True, blank=True)
    filters_to_deliver = models.IntegerField(null=True, blank=True)
    filters_delivered = models.IntegerField(null=True, blank=True)
    wipes_to_deliver = models.IntegerField(null=True, blank=True)
    wipes_delivered = models.IntegerField(null=True, blank=True)
    vaseline_to_deliver = models.IntegerField(null=True, blank=True)
    vaseline_delivered = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default = timezone.now)

    def __unicode__(self):
        return self.weekday+" "+self.month + " "+self.date+", "+self.start_time+"-"+self.end_time+" delivery run"


class DeliveryRequest(models.Model):
    delivery_date = models.ForeignKey(H2OFlintDeliveryDate)
    recipient_first = models.CharField(max_length=45, null=True, blank=True)
    recipient_last = models.CharField(max_length=45, null=True, blank=True)
    recipient_address = models.CharField(max_length=200, null=True, blank=True)
    longitude = models.FloatField(default = -83.6874562)
    latitude = models.FloatField(default = 43.0125274)
    recipient_phone = models.CharField(max_length=20, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    persons_in_household = models.IntegerField(null=True, blank=True)
    cases_requested = models.IntegerField(null=True, blank=True)
    contact_first_name = models.CharField(max_length=45, null=True, blank=True)
    contact_last_name = models.CharField(max_length=45, null=True, blank=True)
    contact_email = models.CharField(max_length=200, null=True, blank=True)
    contact_phone = models.CharField(max_length=20, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default = timezone.now)

    def __unicode__(self):
        return self.recipient_first+" "+self.recipient_last + ", "+self.recipient_address+" for "+unicode(self.delivery_date)


class IndividualHelper(models.Model):
    user = models.ForeignKey(User)
    user_type = models.IntegerField(default = 1)
    local = models.BooleanField(default=False)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=4, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(default = timezone.now)

    def __unicode__(self):
        return self.user.first_name+" "+self.user.last_name


class IndividualHelpOffer(models.Model):
    individual_helper = models.ForeignKey(IndividualHelper, null=True, blank=True)
    wants_to_volunteer = models.BooleanField(default=False)
    group_size = models.IntegerField(null=True, blank=True)
    will_unload = models.BooleanField(default=False)
    will_deliver_with_vehicle = models.BooleanField(default=False)
    will_do_admin = models.BooleanField(default=False)
    will_do_testing = models.BooleanField(default=False)
    will_do_plumbing = models.BooleanField(default=False)
    mon_availability_start_time = models.CharField(max_length=8, null=True, blank=True)
    mon_availability_end_time = models.CharField(max_length=8, null=True, blank=True)
    tue_availability_start_time = models.CharField(max_length=8, null=True, blank=True)
    tue_availability_end_time = models.CharField(max_length=8, null=True, blank=True)
    wed_availability_start_time = models.CharField(max_length=8, null=True, blank=True)
    wed_availability_end_time = models.CharField(max_length=8, null=True, blank=True)
    thu_availability_start_time = models.CharField(max_length=8, null=True, blank=True)
    thu_availability_end_time = models.CharField(max_length=8, null=True, blank=True)
    fri_availability_start_time = models.CharField(max_length=8, null=True, blank=True)
    fri_availability_end_time = models.CharField(max_length=8, null=True, blank=True)
    sat_availability_start_time = models.CharField(max_length=8, null=True, blank=True)
    sat_availability_end_time = models.CharField(max_length=8, null=True, blank=True)
    sun_availability_start_time = models.CharField(max_length=8, null=True, blank=True)
    sun_availability_end_time = models.CharField(max_length=8, null=True, blank=True)
    availability_start_date = models.CharField(max_length=2, null=True, blank=True)
    availability_end_date = models.CharField(max_length=2, null=True, blank=True)
    availability_start_month = models.CharField(max_length=9, null=True, blank=True)
    availability_end_month = models.CharField(max_length=9, null=True, blank=True)
    availability_start_year = models.CharField(max_length=4, null=True, blank=True)
    availability_end_year = models.CharField(max_length=4, null=True, blank=True)
    cases_count = models.IntegerField(null=True, blank=True)
    pallets_count = models.IntegerField(null=True, blank=True)
    back_braces_count = models.IntegerField(null=True, blank=True)
    dollies_count = models.IntegerField(null=True, blank=True)
    vaseline_count = models.IntegerField(null=True, blank=True)
    wipes_count = models.IntegerField(null=True, blank=True)
    dollar_donation_amount = models.FloatField(null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True)
    note_for_recipient = models.TextField(null=True, blank=True)
    doing_park_and_serve = models.BooleanField(default = False)
    park_and_serve_address = models.CharField(max_length=200, null=True, blank=True)
    park_and_serve_city = models.CharField(max_length=45, default = 'Flint')
    park_and_serve_state = models.CharField(max_length=4, default = 'MI')
    park_and_serve_zipcode = models.CharField(max_length=10, null=True, blank=True)
    park_and_serve_month = models.CharField(max_length=9, null=True, blank=True)
    park_and_serve_weekday = models.CharField(max_length=9, null=True, blank=True)
    park_and_serve_date = models.CharField(max_length=2, null=True, blank=True)
    park_and_serve_items = models.CharField(max_length=140, null=True, blank=True)
    park_and_serve_year = models.CharField(max_length=4, default="2016")
    park_and_serve_start_time = models.CharField(max_length=8, null=True, blank=True)
    park_and_serve_end_time = models.CharField(max_length=8, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default = timezone.now)


    def __unicode__(self):
        return unicode(self.individual_helper) +" "+unicode(self.date_created)


class Organization(models.Model):
    contact = models.ForeignKey(User)
    approved = models.BooleanField(default=False)
    org_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=45, default = "Flint")
    state = models.CharField(max_length=4, default = "MI")
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    public_email = models.CharField(max_length=200, null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    has_water = models.BooleanField(default=False)
    has_volunteers = models.BooleanField(default=False)
    has_vehicles_or_drivers = models.BooleanField(default=False)
    has_testers = models.BooleanField(default=False)
    has_filters = models.BooleanField(default=False)
    has_testing_skills = models.BooleanField(default=False)
    has_plumbing_skills = models.BooleanField(default=False)
    has_wipes = models.BooleanField(default=False)
    has_vaseline = models.BooleanField(default=False)
    has_lifting_supplies = models.BooleanField(default=False)
    has_other_supplies = models.BooleanField(default=False)
    other_supplies_on_hand = models.TextField(null=True, blank=True)
    needs_water = models.BooleanField(default=False)
    needs_volunteers = models.BooleanField(default=False)
    needs_vehicles_or_drivers = models.BooleanField(default=False)
    needs_testers = models.BooleanField(default=False)
    needs_filters = models.BooleanField(default=False)
    needs_wipes = models.BooleanField(default=False)
    needs_vaseline = models.BooleanField(default=False)
    needs_lifting_supplies = models.BooleanField(default=False)
    needs_other_supplies = models.BooleanField(default=False)
    other_supplies_needed = models.TextField(null=True, blank=True)
    monday_dist_start = models.CharField(max_length=8, null=True, blank=True)
    monday_dist_end = models.CharField(max_length=8, null=True, blank=True)
    tuesday_dist_start = models.CharField(max_length=8, null=True, blank=True)
    tuesday_dist_end = models.CharField(max_length=8, null=True, blank=True)
    wednesday_dist_start = models.CharField(max_length=8, null=True, blank=True)
    wednesday_dist_end = models.CharField(max_length=8, null=True, blank=True)
    thursday_dist_start = models.CharField(max_length=8, null=True, blank=True)
    thursday_dist_end = models.CharField(max_length=8, null=True, blank=True)
    friday_dist_start = models.CharField(max_length=8, null=True, blank=True)
    friday_dist_end = models.CharField(max_length=8, null=True, blank=True)
    saturday_dist_start = models.CharField(max_length=8, null=True, blank=True)
    saturday_dist_end = models.CharField(max_length=8, null=True, blank=True)
    sunday_dist_start = models.CharField(max_length=8, null=True, blank=True)
    sunday_dist_end = models.CharField(max_length=8, null=True, blank=True)
    limits = models.CharField(max_length=140, null=True, blank=True)
    pickup_requirements = models.CharField(max_length=140, null=True, blank=True)
    date_created = models.DateTimeField(default = timezone.now)
    notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.org_name



class DistributionEvent(models.Model):
    organization = models.ForeignKey(Organization)
    event_name = models.CharField(max_length=45, default="Distribution Event")
    weekday = models.CharField(max_length=9, null=True, blank=True)
    month = models.CharField(max_length=9, null=True, blank=True)    
    date = models.CharField(max_length=2, null=True, blank=True)
    time_start = models.CharField(max_length=8, null=True, blank=True)
    time_end = models.CharField(max_length=8, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=45, default = "Flint")
    state = models.CharField(max_length=4, default = "MI")
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    volunteers_needed = models.IntegerField(null=True, blank=True)
    volunteers_registered = models.IntegerField(null=True, blank=True)
    vehicles_with_driver_needed = models.IntegerField(null=True, blank=True)
    vehicles_with_driver_registered = models.IntegerField(null=True, blank=True)
    dollies_needed = models.IntegerField(null=True, blank=True)
    dollies_confirmed = models.IntegerField(null=True, blank=True)
    back_braces_needed = models.IntegerField(null=True, blank=True)
    back_braces_confirmed = models.IntegerField(null=True, blank=True)
    has_water = models.IntegerField(null=True, blank=True)
    has_testing_kits = models.IntegerField(null=True, blank=True)
    cases_distributed = models.IntegerField(null=True, blank=True)
    pallettes_distributed = models.IntegerField(null=True, blank=True)
    testing_kits_distributed = models.IntegerField(null=True, blank=True)
    has_other_supplies = models.IntegerField(null=True, blank=True)
    other_supplies_on_hand = models.TextField(null=True, blank=True)
    other_supplies_distributed = models.TextField(null=True, blank=True)
    water_case_limit = models.CharField(max_length=200, null=True, blank=True)
    requirements_for_pickup = models.CharField(max_length=200, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default = timezone.now)

    def __unicode__(self):
        return self.organization.org_name +" "+ self.event_name+", " + self.weekday+" "+self.month + " "+self.date