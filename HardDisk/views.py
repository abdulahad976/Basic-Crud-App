from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Disk
from django.contrib import messages


def Display(request):
    disks = Disk.objects.all()
    return render(request, 'display.html', {'disks': disks})

def AddDisk(request):
    if request.method == 'POST':
        name = request.POST['name']
        capacity = request.POST['capacity']
        price = request.POST['price']
        disk = Disk(name=name, capacity=capacity, price=price)
        disk.save()
        return redirect('display')
    return render(request, 'adddisk.html')
    
def UpdateDisk(request, disk_id):
    disk = Disk.objects.get(id=disk_id)
    if request.method == 'POST':
        name = request.POST['name']
        capacity = request.POST['capacity']
        price = request.POST['price']
        disk.name = name
        disk.capacity = capacity
        disk.price = price
        disk.save()
        return redirect('display')
    return render(request, 'updatedisk.html', {'disk': disk})

def DeleteDisk(request, disk_id):
    disk = Disk.objects.get(id=disk_id)
    disk.delete()
    messages.success(request, f"Disk {disk.name} successfully deleted.")
    return redirect('display')


