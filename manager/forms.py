
from django.forms import ModelForm
from . models import Scube_ss,orders

class PrForm(ModelForm):
      class Meta:
            model=Scube_ss
            fields='__all__'

class OrderForm(ModelForm):
      class Meta:
            model=orders
            fields='__all__'            
           
            

