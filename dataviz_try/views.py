from django.views.generic import TemplateView
import plotly.express as px
from dataviz_try.models import ME2NModel

# Create your views here.
class DatavizView(TemplateView):
    template_name = 'dataviz_try/dataviz_try.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ME2N = ME2NModel.objects.all()
        # qs1 = ME2NModel.objects.annotate(sum_tokens=Sum('bids__tokens'))
        # qs2 = qs1.filter(sum_tokens__gte=100)

        fig = px.pie(
                values=[c.valeur for c in ME2N], 
                names=[c.fournisseur for c in ME2N], 
                title='Population of European continent'
                )
        fig.update_traces(textposition='inside')
        fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
        
        chart = fig.to_html()

        context["chart"] = chart

        return context