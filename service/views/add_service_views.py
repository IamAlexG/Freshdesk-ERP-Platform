from django.shortcuts import redirect, render
from django.views import View
from service.models import Service


class CreateService(View):
    ''' Create a new expense '''

    def get(self, request, *args, **kwargs):
        ''' Respond to GET request '''
        return render(request,  'service/add_service.html')

    def post(self, request, *args, **kwargs):
        ''' Respond to POST request '''
        service_name = request.POST.get('service_name')
        service_charge = request.POST.get('service_charge')
        paid_amount = request.POST.get('paid_amount')
        description = request.POST.get('service_description')
        service = Service(user=self.request.user, service_name=service_name, charge=service_charge, description=description, paid_amount=paid_amount)
        service.save()
        '''Provide a redirect on GET request.'''
        return redirect('manage_service')
