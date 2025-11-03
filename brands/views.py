from django.views.generic import ListView, CreateView
from brands.forms import BrandModelForm
from brands.models import Brand

# Create your views here.
class BrandListView(ListView):
  model = Brand
  template_name = "brands.html"
  context_object_name = 'brands'

  def get_queryset(self):
    brands = super().get_queryset().order_by('name')
    search = self.request.GET.get('search')
    if search :
      brands = brands.filter(name__icontains=search)
    return brands

class NewBrandCreateView(CreateView):
  model = Brand
  form_class = BrandModelForm
  template_name = 'new_brand.html'
  success_url = '/brands/'
