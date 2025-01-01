from django.shortcuts import render

# Create your views here.


def home(request):
  context = {"name": "Pat"}
  return render(request, "app1/home.html", context)
  # return HttpResponse(template.render(context))