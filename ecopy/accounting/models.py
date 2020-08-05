from django.db import models
import numpy as np


# CATEGORY CLASSES
# -----------------------------------------------------------------------------
class BaseCategory(models.Model):
    name = models.CharField()
    color = models.CharField()
    income = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseCategory):
    pass


class SubCategory(BaseCategory):
    main_category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)


# TRANSACTION CLASSES
# -----------------------------------------------------------------------------
class Transaction(models.Model):
    amount = models.FloatField()
    name = models.Charfield(max_length=100)
    description = models.Charfield(max_length=300)
    date = models.DateField()

    class Meta:
        abstract = True

    @property
    def rounded_amount(self):
        return np.round(amount)


class Income(Transaction):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Expense(Transaction):
    category = models.ForeignKey(ECategory, on_delete=models.CASCADE)
