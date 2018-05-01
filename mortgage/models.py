from django.db import models

	

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=70, unique= True)
    

    

# class Loan(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     loan_amount = models.FloatField(default=0)
#     year = models.IntegerField()
#     month = models.IntegerField()
#     rate = models.FloatField()
#     loan_name = models.CharField(max_length=250, default='DEFAULT VALUE')
#     down_payment = models.FloatField(default=0)
#     add_per_month = models.FloatField(default=0)
#     add_per_year = models.FloatField(default=0)

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    year = models.IntegerField()
    month = models.IntegerField()
    rate =  models.DecimalField(max_digits=3, decimal_places=2, default=0)
    loan_name = models.CharField(max_length=250, default='DEFAULT VALUE')
    down_payment = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    add_per_month = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    add_per_year = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    
objects = models.Manager()
