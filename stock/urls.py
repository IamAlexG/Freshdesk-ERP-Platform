from django.urls import path
from stock.views.donwload_stock_pdf import DownloadStockPDF
from stock.views.export_stock_csv_views import DownloadStockCSV
from stock.views.stock_pdf_views import ViewStockPDF
from stock.views.stock_report_views import StockReportView

urlpatterns = [
    path('report/', StockReportView.as_view(), name='stock_report'),
    path('export/', DownloadStockCSV.as_view(), name='donwload_stock_csv'),
    path('pdf/', ViewStockPDF.as_view(), name='view_stock_pdf'),
    path('download/', DownloadStockPDF.as_view(), name='download_stock_pdf'),
]
