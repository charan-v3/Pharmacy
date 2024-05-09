from django.shortcuts import render
from home.models import *
from .models import *
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def bill_summary(request):
    return render(request, "bills/bill_summary.htm;")


@require_POST
def create_bill(request):
    if request.user.is_authenticated and request.user.profile.user_type == "Worker":
        # Get the selected customer's username from the request data
        customer_username = request.POST.get("customer")
        # Retrieve the customer's profile
        customer_profile = Profile.objects.filter(
            user__username=customer_username
        ).first()
        if customer_profile:
            # Create the bill object
            bill = Bill.objects.create(
                customer_profile=customer_profile, worker=request.user
            )
            return JsonResponse({"success": True, "bill_id": bill.id})
    return JsonResponse({"success": False})


@require_POST
def add_item_to_bill(request):
    if request.user.is_authenticated and request.user.profile.user_type == "Worker":
        # Get the bill ID and item ID from the request data
        bill_id = request.POST.get("bill_id")
        item_id = request.POST.get("item_id")
        # Retrieve the bill object
        bill = Bill.objects.filter(id=bill_id).first()
        # Retrieve the item object
        item = medicine.objects.filter(id=item_id).first()
        if bill and item:
            # Create the bill item object
            bill_item = BillItem.objects.create(item=item, quantity=1, bill=bill)
            return JsonResponse({"success": True})
    return JsonResponse({"success": False})
