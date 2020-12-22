from django import forms
class FlowerForm(forms.Form):
	sl=forms.FloatField()
	sw=forms.FloatField()
	pl=forms.FloatField()
	pw=forms.FloatField()