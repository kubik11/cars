from django.db import models
#from django.utils import timezone
from datetime import datetime
#from multiselectfield import MultiSelectField
#from ckeditor.fields import RichTextField # In order to edit text in admin panel
# Create your models here.
class Vehicle(models.Model):
	state_choices = (
		('АИ', 'Киевская обл'),
		('ВН', 'Одесская обл'),
		('ХИ', 'Херсонская обл'),
	)
	features_choices = (
		('Cruise control','Cruise control'),
		('Airbags','Airbags'),
		('Audio Interface','Audio Interface'),
	)
	doors_choices = (
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
		('6','6'),
	)
	year_choices = []
	for i in range(2000, (datetime.now().year + 1)):
		year_choices.append((i, i))

	car_title = models.CharField(max_length = 255)
	state = models.CharField(choices = state_choices, max_length = 255)
	city = models.CharField(max_length = 100)
	color = models.CharField(max_length = 100)
	model = models.CharField(max_length = 100)
	year = models.IntegerField(('year'), choices = year_choices,)
	condition = models.CharField(max_length = 100)
	price = models.IntegerField()
	description = models.TextField(max_length = 500)
	car_photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
	car_photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
	car_photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
	car_photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
	car_photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
	features = models.CharField(choices = features_choices, max_length = 100)
	body_style = models.CharField(max_length = 100)
	engine = models.CharField(max_length = 100)
	transmition = models.CharField(max_length = 100)
	miles = models.IntegerField()
	doors = models.CharField(choices = doors_choices, max_length = 10)
	passengers = models.CharField(max_length = 100)
	vin_no = models.CharField(max_length = 100)
	milage = models.CharField(max_length = 100)
	fuel_type = models.CharField(max_length = 50)
	no_of_owners = models.CharField(max_length = 100)
	is_featured = models.BooleanField(default = False)
	created_date = models.DateTimeField(default = datetime.now(), blank = True)
