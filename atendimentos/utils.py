# Arquivo de configuração para gerar PDF a partir de um HTML
from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

class GerarPDF:

    def render_to_pdf(self, template_end, context_dict={}):
        template = get_template(template_end)
        html = template.render(context_dict)
        print(html)
        result = BytesIO()
        try:
            pdf = pisa.pisaDocument(BytesIO(html.encode("")), result)
            return HttpResponse(result.getvalue(),
                                content_type='application/pdf')
        except Exception as e:
           return HttpResponse('Erro ao gerar PDF: {}'.format(str(e)))
