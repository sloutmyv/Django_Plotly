from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["name"].widget.attrs.update({"placeholder":"Prénom Nom","class":'form-control'})
        self.fields["email"].widget.attrs.update({"placeholder":"Email","class":'form-control'})
        self.fields["content"].widget.attrs.update({"placeholder":"Message","class":'form-control'})
