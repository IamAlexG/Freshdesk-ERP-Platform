from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import View
from purchase.models import Purchase
from utils.render_to_pdf import generate_pdf


class DownloadPurchasePDF(LoginRequiredMixin, View):
    '''
    Automaticly downloads to PDF file.
    '''
    def get(self, request, *args, **kwargs):
        purchase = Purchase.objects.all().order_by('-id')
        pdf = generate_pdf('purchase/pdf/purchase_pdf.html', {'purchase': purchase})
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Purchase-Data-%s.pdf" % date.today()
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response
