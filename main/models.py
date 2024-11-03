from django.db import models

class Products(models.Model):
    type = models.CharField("Тип", max_length = 50)
    store_count = models.IntegerField("Количество на складе")
    time_to_make = models.DateTimeField("Время на производство")    
    art = models.CharField("Артикул", max_length = 50)

    def __str__(self):
        return self.type
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    
class Customers(models.Model):
    name = models.CharField("Наименование покупателя", max_length = 50)
    address = models.CharField("Адрес покупателя", max_length = 50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"

class Orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    type = models.ForeignKey(Products, on_delete=models.CASCADE)
    count = models.IntegerField("Количество в заказе")
    term_num = models.IntegerField("Номер договора")
    is_confirmed = models.BooleanField("Статус подтверждения")
    is_done = models.BooleanField("Статус доставки")

    def __str__(self):
        return str(self.term_num)
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"