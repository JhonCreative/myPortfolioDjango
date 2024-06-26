from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# def about_view(request):
#    my_profile={
#       'name':'Jhon Calsina'
#    }
#    return render(request, 'index.html', {'my_profile':
#       my_profile})



class index(TemplateView):
   template_name = 'index.html'
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['name'] = 'Jhon'
      context['lastname'] = 'Calsina'
      context['description'] = 'Hi everyone 👋 Im Jhon 20-year-old junior frontend developer 💻 and photo editor 📷 with a passion for learning and exploring new technologies 📲.'
      return context