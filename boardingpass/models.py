from django.db import models
 

# Create your models here.
class pengguna(models.Model):
	nik = models.CharField(max_length=16, null=True, unique=True)
	nama = models.CharField(max_length=255, null=True, blank=True)
	email = models.EmailField(max_length=255, null=True, blank=True)
	password = models.CharField(max_length=255, null=True, blank=True)
	created_at = models.DateField(auto_now_add=True, editable=False, null=True, blank=True)
	updated_at = models.DateField(auto_now=True, editable=False, null=True, blank=True)

	def __str__(self):
		return "{}. {}".format(self.id, self.nama)

class tiket(models.Model):
	id = models.BigAutoField(primary_key=True)
	nik = models.ForeignKey(pengguna, to_field='nik', on_delete=models.CASCADE, null=True, blank=True)
	kode_booking = models.CharField(max_length=31, null=True, blank=True)
	status = models.CharField(max_length=1, null=True, blank=True)
	wajah = models.CharField(max_length=1, null=True, blank=True)
	masker = models.CharField(max_length=1, null=True, blank=True)
	suhu = models.CharField(max_length=2, null=True, blank=True)
	created_at = models.DateField(auto_now_add=True, editable=False, null=True, blank=True)
	updated_at = models.DateField(auto_now=True, editable=False, null=True, blank=True)


	def __str__(self):
		return "{}".format(self.kode_booking)