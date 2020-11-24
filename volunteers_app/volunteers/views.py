from django.http import HttpResponse
from django.shortcuts import render, redirect
from .volunteer_form import VolunteerForm
from .branch_form import BranchForm
from .models import Volunteer, Branch


def index(request):
    return render(request, "volunteers/index.html")


def volunteers_list(request):
    context = {'volunteers_list': Volunteer.objects.all()}
    return render(request, "volunteers/volunteers_list.html", context)


def volunteer_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = VolunteerForm()
        else:
            volunteer = Volunteer.objects.get(pk=id)
            form = VolunteerForm(instance=volunteer)
        return render(request, "volunteers/volunteer_form.html", {'form': form})
    else:
        if id == 0:
            form = VolunteerForm(request.POST)
        else:
            volunteer = Volunteer.objects.get(pk=id)
            form = VolunteerForm(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
        return redirect('/volunteers/volunteers_list')


def volunteer_delete(request, id):
    volunteer = Volunteer.objects.get(pk=id)
    volunteer.delete()
    return redirect('/volunteers/volunteers_list')


def branch_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = BranchForm()
        else:
            branch = Branch.objects.get(pk=id)
            form = BranchForm(instance=branch)
        return render(request, "volunteers/branch_form.html", {'form': form})
    else:
        if id == 0:
            form = BranchForm(request.POST)
        else:
            branch = Branch.objects.get(pk=id)
            form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
        return redirect('/volunteers/branch_list')


def branch_list(request):
    context = {'branch_list': Branch.objects.all()}
    return render(request, "volunteers/branch_list.html", context)


def branch_delete(request):
    return
