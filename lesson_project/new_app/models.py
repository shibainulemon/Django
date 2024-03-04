from django.db import models

#メンバーテーブル
class Members(models.Model):
    username = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    mail = models.EmailField(max_length=100)

    def __str__(self):
        return f"Member:id={str(self.id),{self.username},{self.phone},({self.age})}"



#カテゴリーテーブル
class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category



#投稿テーブル
class Post(models.Model):
    members = models.ForeignKey(Members, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<Message:id={str(self.id)},{self.title} ({str(self.pub_date)}),{self.members.username}>"

    class Meta:
        ordering = ("-pub_date",)




