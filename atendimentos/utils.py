# Arquivo de configuração para gerar PDF a partir de um HTML
from io import BytesIO
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

class GerarPDF:

    def render_to_pdf(self,template_end, context_dict={}):
        template = get_template(template_end)
        html = render_to_string(template_end, context_dict)        
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None