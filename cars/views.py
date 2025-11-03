from django.shortcuts import redirect, render
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.

class CarsView(View):
  def get(self, request):
    cars = Car.objects.all()
    search = request.GET.get('search')

    if search:
      cars = cars.filter(model__icontains=search)

    return render(request, 'cars.html', {"cars": cars})

class CarsListView(ListView):
  model = Car
  template_name = 'cars.html'
  context_object_name = 'cars'

  def get_queryset(self):
    cars = super().get_queryset().order_by('model')
    search = self.request.GET.get('search')
    if search:
      cars = cars.filter(model__icontains=search)
    return cars

class NewCarView(View):
  def get(self, request):
    new_car_form = CarModelForm()
    return render(request, 'new_car.html', {"new_car_form": new_car_form})

  def post(self, request):
    new_car_form = CarModelForm(request.POST, request.FILES)
    if new_car_form.is_valid():
      new_car_form.save()
      return redirect('cars_list')
    return render(request, 'new_car.html', {"new_car_form": new_car_form})

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
  model = Car
  form_class = CarModelForm
  template_name = 'new_car.html'
  success_url = '/cars/'

class CarDetailView(DetailView):
  model = Car
  template_name = 'car_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
  model = Car
  form_class = CarModelForm
  template_name = 'car_update.html'
  success_url = '/cars/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
  model = Car
  template_name = 'car_delete.html'
  success_url = '/cars/'
