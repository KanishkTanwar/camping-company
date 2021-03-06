from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

# Create your models here.

# All Destination


class Destination(models.Model):
    place = models.CharField(max_length=64)
    state_city = models.CharField(max_length=64)
    cc_higlight = models.CharField(max_length=128)
    map_loc = models.CharField(max_length=64)
    description = models.TextField()
    distance = models.IntegerField()
    hours = models.IntegerField()
    accommodation = models.CharField(max_length=64)
    important_to_know = models.TextField()
    note = models.CharField(max_length=128)
    night_time_temperature_summer = models.CharField(max_length=64)
    night_time_temperature_winter = models.CharField(max_length=64)
    season = models.CharField(max_length=64)
    slug = models.SlugField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.place

# Detail map location model


class Image(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='maps/detail', blank=True)
    image2 = models.ImageField(upload_to='maps/detail', blank=True)
    image3 = models.ImageField(upload_to='maps/detail', blank=True)
    image4 = models.ImageField(upload_to='maps/detail', blank=True)

    def __str__(self):
        return self.destination.place


class Amenity(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    basic_toilet = models.BooleanField()
    bathroom = models.BooleanField()
    kitchen = models.BooleanField()
    pets_allowed = models.BooleanField()
    charging_points = models.BooleanField()
    drinking_water = models.BooleanField()
    covered_area = models.BooleanField()
    barbeque_grills = models.BooleanField()
    good_for_groups = models.BooleanField()
    campfire = models.BooleanField()
    picnic_table = models.BooleanField()
    breakfast = models.BooleanField()

    def __str__(self):
        return self.destination.place


class Detail(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    type_of_land = models.CharField(max_length=64)
    accessible_By = models.CharField(max_length=64)
    check_in = models.CharField(max_length=64)
    check_out = models.CharField(max_length=64)
    phone = models.BigIntegerField(null=True, blank=True)
    cancellation_policy = models.CharField(max_length=64)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return self.destination.place


class Booking(models.Model):
    txnid = models.CharField(max_length=128, blank=True, null=True)
    destination = models.ForeignKey(Detail, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caravan = models.IntegerField()
    rooftop = models.IntegerField()
    ground = models.IntegerField()
    days = models.IntegerField()
    date = models.DateField(null=True, blank=True)
    amount = models.FloatField()
    igst = models.FloatField(blank=True, null=True)
    convenient = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.txnid


class Activity(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    off_roading = models.BooleanField()
    trekking = models.BooleanField()
    boating = models.BooleanField()
    waterfall = models.BooleanField()
    lake = models.BooleanField()
    jungle_walk = models.BooleanField()
    caving = models.BooleanField()
    local_farm = models.BooleanField()
    river_beach = models.BooleanField()
    swimming = models.BooleanField()
    historical_monument = models.BooleanField()
    fishing = models.BooleanField()

    def __str__(self):
        return self.destination.place

# map related


class Map(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    latitude = models.FloatField(max_length=128, blank=True, null=True)
    longitude = models.FloatField(max_length=128, blank=True, null=True)
    images = models.ImageField(upload_to='maps/image', blank=True)
    iconImage = models.ImageField(upload_to='maps/iconImage', blank=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.destination.place


class Region(models.Model):
    region = models.ManyToManyField(Map, related_name="Region")
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name


class Circuit(models.Model):
    slug = models.SlugField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=128,blank=True, null=True)
    para11 = models.CharField(max_length=256,blank=True, null=True)
    para12 = models.CharField(max_length=256,blank=True, null=True)
    para13 = models.TextField()
    para21 = models.CharField(max_length=256, blank=True, null=True)
    para22 = models.CharField(max_length=256, blank=True, null=True)
    para23 = models.TextField()
    para31 = models.CharField(max_length=256, blank=True, null=True)
    para32 = models.CharField(max_length=256, blank=True, null=True)
    para33 = models.TextField()
    para41 = models.CharField(max_length=256, blank=True, null=True)
    para42 = models.CharField(max_length=256, blank=True, null=True)
    para43 = models.TextField()
    para51 = models.CharField(max_length=256, blank=True, null=True)
    para52 = models.CharField(max_length=256, blank=True, null=True)
    para53 = models.TextField()
    main_image = models.ImageField(upload_to='circuit', blank=True)
    image1 = models.ImageField(upload_to='circuit', blank=True)
    image2 = models.ImageField(upload_to='circuit', blank=True)
    image3 = models.ImageField(upload_to='circuit', blank=True)
    image4 = models.ImageField(upload_to='circuit', blank=True)
    image5 = models.ImageField(upload_to='circuit', blank=True)

    def __str__(self):
        return self.slug


def destination_pre_save_receiver(sender, instance, **kwargs):
    title = instance.place.split()
    instance.slug = "-".join(title).replace("?", "")
    # slug cant have question marks boy


pre_save.connect(destination_pre_save_receiver, sender=Destination)