from django.shortcuts import render

# Create your views here.
from django.views import View


class Api(View):
    def get(self, request):
        template_name = ""
        print("request")
        return render(self.template_name)