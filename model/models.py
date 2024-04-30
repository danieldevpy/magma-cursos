from django.db import models


class Text(models.Model):
    field = models.CharField(max_length=200)
    size = models.IntegerField()
    pos_x = models.CharField(max_length=200)
    pos_y = models.IntegerField()

    def __str__(self) -> str:
        return self.field

    def get_pos_x(self):
        return eval(self.pos_x)

class Model(models.Model):
    name = models.CharField(max_length=200)
    front = models.FileField(upload_to='models/')
    back = models.FileField(upload_to='models/')
    texts = models.ManyToManyField(Text)

    def __str__(self) -> str:
        return self.name
    
    def to_json(self):
        return {
            "id": self.pk,
            "name": self.name
        }