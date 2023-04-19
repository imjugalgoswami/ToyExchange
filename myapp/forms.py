from django import forms
from .models import Ad

# class AdForm(forms.ModelForm):
#     class Meta:
#         model = Ad
#         fields = ['title', 'description', 'price', 'image']
#         widgets = {
#             'description': forms.Textarea(attrs={'rows': 4}),
#         }

#     def __init__(self, *args, **kwargs):
#         super(AdForm, self).__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs.update({'class': 'form-control'})
#         self.fields['description'].widget.attrs.update({'class': 'form-control'})
#         self.fields['price'].widget.attrs.update({'class': 'form-control'})
#         self.fields['image'].widget.attrs.update({'class': 'form-control'})

from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'city']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AdForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['image1'].widget.attrs.update({'class': 'form-control'})
        self.fields['image2'].widget.attrs.update({'class': 'form-control'})
        self.fields['image3'].widget.attrs.update({'class': 'form-control'})
        self.fields['image4'].widget.attrs.update({'class': 'form-control'})
        self.fields['image5'].widget.attrs.update({'class': 'form-control'})
        self.fields['image6'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
