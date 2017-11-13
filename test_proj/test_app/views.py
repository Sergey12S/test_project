import xlwt
from django.views.generic import ListView, DetailView, DeleteView, View, \
    CreateView
from django.http import HttpResponse
from django.db.models import F
from django.shortcuts import redirect
from django.db import transaction
from django.utils.decorators import method_decorator
from datetime import date
from dateutil.relativedelta import relativedelta
from .models import Client
from .forms import ListClientsForm, AddClientForm


class AddClientView(CreateView):
    """Add client page"""
    model = Client
    template_name = "add_client.html"
    form_class = AddClientForm
    success_url = "/clients/"


class ListClientsView(ListView):
    """List clients page"""
    template_name = "list_clients.html"

    def get(self, request, *args, **kwargs):
        self.form = ListClientsForm(request.GET)
        self.form.is_valid()
        return super(ListClientsView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Client.objects.all()
        if self.form.cleaned_data.get("search_first_name"):
            queryset = queryset.filter(
                first_name=self.form.cleaned_data["search_first_name"])
        if self.form.cleaned_data.get("search_last_name"):
            queryset = queryset.filter(
                last_name=self.form.cleaned_data["search_last_name"])
        if self.form.cleaned_data.get("sort_field"):
            queryset = queryset.order_by(self.form.cleaned_data["sort_field"])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListClientsView, self).get_context_data(**kwargs)
        context["form"] = self.form
        return context


class DetailClientView(DetailView):
    """Detail client page"""
    model = Client
    template_name = "detail_client.html"

    def get_context_data(self, **kwargs):
        context = super(DetailClientView, self).get_context_data(**kwargs)
        context["age"] = relativedelta(date.today(),
                                       self.object.birth_date).years
        return context


class DeleteClientView(DeleteView):
    """Delete client page"""
    model = Client
    template_name = "delete_client.html"
    success_url = "/clients/"


def export_users_xls(request):
    """Export to xls"""
    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = "attachment; filename='clients.xls'"

    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("Clients")

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ["username", "first_name", "last_name", "birth_date", ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    font_style.num_format_str = "D-MMM-YY"

    rows = Client.objects.all().values_list("username", "first_name",
                                            "last_name", "birth_date")
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


class VotingListView(ListView):
    """Voting list page"""
    template_name = "voting.html"
    model = Client


class LikeMixin:
    """Common class for likes and AJAX"""
    def like(self):
        self.queryset.select_for_update().\
            filter(rating__lt=10, pk=self.kwargs["pk"]).\
            update(rating=F("rating") + 1)


@method_decorator(transaction.atomic, name="get")
class LikeUserView(LikeMixin, View):
    """Like"""
    queryset = Client.objects.all()

    def get(self, request, *args, **kwargs):
        self.like()
        return redirect("/clients/voting/")
