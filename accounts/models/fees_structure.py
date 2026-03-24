from django.db import models


# CLASS
class SchoolClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# TERM (Dynamic)
class Term(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# FEE HEADER
class FeeHeader(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# FEE STRUCTURE
class FeeStructure(models.Model):

    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    fee_header = models.ForeignKey(FeeHeader, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.school_class} - {self.term} - {self.fee_header}"