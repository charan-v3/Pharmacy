from django.shortcuts import render


def bill_summary(request):
    return render(request, "bills/bill_summary.htm;")


def bill_add(request):
    pass


def bill_delete(request):
    pass


def bill_update(request):
    pass
