from django import forms
from django.conf import settings

from converter.models import WaypointFile


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = WaypointFile
        fields = ['file']
