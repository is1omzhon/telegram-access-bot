from django.db import models
from django.contrib.auth.models import User

class TelegramUser(models.Model):   
    telegram_id = models.BigIntegerField(
        unique=True,
        verbose_name="Telegram ID"
    )
    username = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Имя в Telegram"
    )   
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Связанный пользователь Django"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации"
    )
    
    def __str__(self):
        return self.username or str(self.telegram_id)
    
    class Meta:
        verbose_name = "Telegram-пользователь"
        verbose_name_plural = "Telegram-пользователи"

class AccessRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('approved', 'Одобрено'),
        ('rejected', 'Отказано'),
    ]
    
    telegram_user = models.ForeignKey(
        TelegramUser,
        on_delete=models.CASCADE,
        verbose_name="Telegram-пользователь"
    )
    service_name = models.CharField(
        max_length=255,
        verbose_name="Название сервиса"
    )
    reason = models.TextField(
        blank=True,
        verbose_name="Причина запроса"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата запроса"
    )
    processed_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата обработки"
    )
    
    def __str__(self):
        return f"{self.telegram_user} - {self.service_name} ({self.status})"
    
    class Meta:
        verbose_name = "Запрос доступа"
        verbose_name_plural = "Запросы доступа"