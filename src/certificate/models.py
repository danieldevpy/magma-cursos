from django.db import models
from model.models import Model
import json, re 

class Certificate(models.Model):
    identifier = models.CharField(max_length=200)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    data_json = models.CharField(max_length=200)
    render = ''

    def __str__(self) -> str:
        return self.identifier
    
    def get_json(self):
        self.data_json = re.sub(r"(?<!\\)'", '"', self.data_json)
        return json.loads(self.data_json)
    
    def render_html(self):
        data_json = self.get_json()
        for k, v in data_json.items():
            self.render += f'<b>{k}:</b> <label>{v}</label><br>'
        
        return self