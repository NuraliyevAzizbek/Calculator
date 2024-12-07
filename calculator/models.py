from django.db import models
from django.core.exceptions import ValidationError

class Math_hints(models.TextChoices):
    PLUS = '+'
    MINUS = '-'
    BULISH = '/'
    KUPAYTIRISH = '*'


def validate_zero(value):
    if value  == 0:
        raise ValidationError(
            "%(value)s is not an 0",
            params={"value": value},
        )

# Create your models here.
class Calculator(models.Model):
    # action = models.TextField() #a + b = c
    value_1 = models.FloatField(verbose_name='1chi qiymat', null=True)
    value_2 = models.FloatField(verbose_name='2chi qiymat', null=True, help_text='0 bulishi mumkin emas') #validators=[funkisiya]
    hint = models.CharField(verbose_name="Amal", max_length=1, choices=Math_hints.choices, default=Math_hints.PLUS)
    # outout = models.FloatField(
    #     verbose_name='Natija'
    # ) # value_1 hint value_2
    created_at = models.DateTimeField(auto_now_add=True)



    @property
    def outout(self):
        try:
            self.value_1 = int(self.value_1)
            self.value_2 = int(self.value_2)
            if self.hint == Math_hints.PLUS:
                return self.value_1 + self.value_2
            elif self.hint == Math_hints.MINUS:
                return  self.value_1 - self.value_2
            elif self.hint == Math_hints.KUPAYTIRISH:
                return  self.value_1 * self.value_2
            elif self.hint == Math_hints.BULISH:
                natija =   self.value_1 / self.value_2
                return natija
        except Exception as e:
            return f"Xato: {e}"

        return 0
    
    def clean(self):
        if self.hint == Math_hints.BULISH and self.value_2 == 0:
            raise ValidationError("0 ga bo'lish mumkin emas!")


    def __str__(self):
        return f"{self.value_1} {self.hint} {self.value_2}"