from django.db import models
from autoslug import AutoSlugField
from django_countries.fields import CountryField


class Location(models.Model):

    
    def __str__(self):
        return str(self.name)

    name = CountryField("Country of Origin", blank=True)

class Dinosaur(models.Model):
    class Diet(models.TextChoices):
        UNKNOWN = "unknown", "UnKnown"
        HERBIVOROUS = "herbivorous", "Herbivorous"
        OMNIVOROUS = "omnivorous", "Omnivorous"
        CARNIVOROUS = "carnivorous", "Carnivorous"

    class Period(models.TextChoices):
        UNKNOWN = "unknown", "UnKnown"
        LATE_TRIASSIC = "Late Triassic"
        EARLY_JURASSIC = "Early Jurassic"
        MID_JURASSIC = "Mid Jurassic"
        LATE_JURASSIC = "Late Jurassic"
        EARLY_CRETACEOUS = "Early Cretaceous"
        LATE_CRETACEOUS = "Late Cretaceous"

    class Typeofdino(models.TextChoices):
        UNKNOWN = "unknown", "UnKnown"
        ARMOURED_DINOSAURS = "Armoured dinosaurs"
        CERATOPSIAN = "Ceratopsian"
        EUORNITHOPOD = "Euornithopod"
        SAUROPOD = "Sauropod"
        LARGE_THEROPOD = "Large theropod"
        SMALL_THEROPOD = "Small theropod"

    #TODO - "add a choices option for species after scraping data"

    def __str__(self):
        return str(self.name)

    name = models.CharField("Name of Dinosaur", max_length=100)
    slug = AutoSlugField("Dinosaur Address", unique=True, always_update=False, populate_from="name")
    pronunciation = models.CharField("How to Pronounce the Name", max_length=120)
    length = models.IntegerField("Length of Dinosaur")
    diet = models.CharField("Diet of the Dinosaur", max_length=25, choices=Diet.choices, default=Diet.UNKNOWN)
    period = models.CharField("Period of time when dinosaur lived", max_length=25, choices = Period.choices, default=Period.UNKNOWN)
    typeofdino = models.CharField("Type of Dinosaur", max_length=25, choices = Typeofdino.choices, default=Typeofdino.UNKNOWN)
    species = models.CharField("Species of Dinosaur", max_length=25)
    locations = models.ManyToManyField(Location, related_name="dinosaurs")



    