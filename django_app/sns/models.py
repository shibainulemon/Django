from django.db import models
from django.contrib.auth.models import User


# Messageテーブル
class Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_owner")
    content = models.TextField(max_length=1000)
    good_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.content)}({str(self.owner)})"

    class Meta:
        ordering = ("-pub_date",)


#Goodテーブル
class Good(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="good_owner")
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"'{str(self.message)} (by{str(self.owner)})"

    class Meta:
        ordering = ("-pub_date",)


#Replyテーブル
class Reply(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reply_owner")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="replies")
    replied = models.TextField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)
