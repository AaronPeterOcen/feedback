from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm

# Create your views here.


def storefile(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            "form": form
        })

    def post(self, request):
        # pass
        subform = ProfileForm(request.POST, request.FILES)

        if subform.is_valid():
            storefile(request.FILES["image"])
            return HttpResponseRedirect("/profiles")

        return render(request, "profiles/create_profile.html", {
            "form": subform
        })
        