from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.department_name}"
    
    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class UserDepartment(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Отдел: {self.department}, Пользователь: {self.user}"
    
    class Meta:
        verbose_name = 'Связь пользователей с отделами'
        verbose_name_plural = 'Связи пользователей с отделами'