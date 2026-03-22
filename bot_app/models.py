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
