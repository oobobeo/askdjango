from django.db import models
import re
from django.forms import ValidationError
from django.utils import timezone


def lnglat_validator(value):
	if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
		raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
	title = models.CharField(max_length=100, verbose_name = 'verbose_name',
							 help_text = 'title should be no more than 100 letters')
	content = models.TextField(help_text='use Markdown syntax')
	tags = models.CharField(max_length=100,blank=True)
	lnglat = models.CharField(max_length=50,
							validators=[lnglat_validator],
							help_text='위도,경도 포맷으로 입력',
							default = 'default for lnglat')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)