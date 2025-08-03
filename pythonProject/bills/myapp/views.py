# # # from django.shortcuts import render
# # #
# # # # Create your views here.
# # # from django.http import HttpResponse
# # #
# # #
# # # from django.shortcuts import render, redirect
# # # from .models import Item
# # #
# # # def index(request):
# # #     if request.method == 'POST':
# # #         if 'add' in request.POST:
# # #             material = request.POST['material']
# # #             quantity = float(request.POST['quantity'])
# # #             rate = float(request.POST['rate'])
# # #             Item.objects.create(material=material, quantity=quantity, rate=rate)
# # #         elif 'delete' in request.POST:
# # #             item_id = request.POST['delete']
# # #             Item.objects.get(id=item_id).delete()
# # #         return redirect('index')
# # #
# # #     items = Item.objects.all()
# # #     overall_total = sum(item.total for item in items)
# # #     return render(request, 'index.html', {'items': items, 'overall_total': overall_total})
# # # def print_bill(request):
# # #     items = Item.objects.all()
# # #     overall_total = sum(item.total for item in items)
# # #     return render(request, 'print_bill.html', {'items': items, 'overall_total': overall_total})
# # #
# # import uuid
# #
# # from django.shortcuts import render, redirect
# # from .models import Item
# #
# # # Home page with only Add button
# # def index(request):
# #     return render(request, 'index.html')
# #
# # # # Add item form view
# # # def add_item(request):
# # #     if request.method == 'POST':
# # #         customer_name = request.POST['customer_name']
# # #         material = request.POST['material']
# # #         quantity = float(request.POST['quantity'])
# # #         rate = float(request.POST['rate'])
# # #         Item.objects.create(customer_name=customer_name, material=material, quantity=quantity, rate=rate)
# # #         return redirect('bill')
# # #     return render(request, 'add_item.html')
# # # def add_item(request):
# # #     # Create bill_id if not in session
# # #     if 'bill_id' not in request.session:
# # #         request.session['bill_id'] = str(uuid.uuid4())
# # #
# # #     bill_id = request.session['bill_id']
# # #
# # #     if request.method == 'POST':
# # #         customer_name = request.POST['customer_name']
# # #         material = request.POST['material']
# # #         quantity = float(request.POST['quantity'])
# # #         rate = float(request.POST['rate'])
# # #
# # #         Item.objects.create(
# # #             bill_id=bill_id,
# # #             customer_name=customer_name,
# # #             material=material,
# # #             quantity=quantity,
# # #             rate=rate
# # #         )
# # #
# # #     items = Item.objects.filter(bill_id=bill_id)
# # #     overall_total = sum(item.total for item in items)
# # #
# # #     return render(request, 'add_item.html', {
# # #         'items': items,
# # #         'overall_total': overall_total
# # #     })
# # # # Bill view page
# # def bill_view(request):
# #     items = Item.objects.all()
# #     overall_total = sum(item.total for item in items)
# #     return render(request, 'bill.html', {'items': items, 'overall_total': overall_total})
# # def delete_item(request, item_id):
# #     Item.objects.get(id=item_id).delete()
# #     return redirect('bill')
# #
# # def edit_item(request, item_id):
# #     item = Item.objects.get(id=item_id)
# #     if request.method == 'POST':
# #         item.material = request.POST['material']
# #         item.quantity = float(request.POST['quantity'])
# #         item.rate = float(request.POST['rate'])
# #         item.save()
# #         return redirect('bill')
# #     return render(request, 'edit_item.html', {'item': item})
# #
# # # def new_bill(request):
# # #     try:
# # #         del request.session['bill_id']
# # #     except KeyError:
# # #         pass
# # #     return redirect('add_item')
# # def new_bill(request):
# #     request.session.pop('bill_id', None)
# #     request.session.pop('customer_name', None)
# #     return redirect('add_item')
# # import uuid
# # from .models import Item
# #
# # def add_item(request):
# #     if 'bill_id' not in request.session:
# #         request.session['bill_id'] = str(uuid.uuid4())
# #
# #     bill_id = request.session['bill_id']
# #
# #     if request.method == 'POST':
# #         if 'customer_name' not in request.session:
# #             customer_name = request.POST.get('customer_name')
# #             request.session['customer_name'] = customer_name
# #         else:
# #             customer_name = request.session['customer_name']
# #
# #         material = request.POST['material']
# #         quantity = float(request.POST['quantity'])
# #         rate = float(request.POST['rate'])
# #
# #         Item.objects.create(
# #             bill_id=bill_id,
# #             customer_name=customer_name,
# #             material=material,
# #             quantity=quantity,
# #             rate=rate
# #         )
# #
# #     items = Item.objects.filter(bill_id=bill_id)
# #     overall_total = sum(item.total for item in items)
# #
# #     return render(request, 'add_item.html', {
# #         'items': items,
# #         'overall_total': overall_total,
# #         'customer_name': request.session.get('customer_name', None),
# #     })
# #
# # from django.shortcuts import render
# # from .models import Bill
# #
# # def bill_history(request):
# #     bills = Bill.objects.order_by('-created_at')
# #     return render(request, 'myapp/bill_history.html', {'bills': bills})
# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
# from .models import Bill, Item
# from django.utils import timezone
# from django.template.loader import get_template
# from xhtml2pdf import pisa
#
#
# # 📄 Render HTML to PDF
# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     response = HttpResponse(content_type='application/pdf')
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('PDF error <pre>' + html + '</pre>')
#     return response
#
#
# # 🏠 Home
# def index(request):
#     return render(request, 'index.html')
#
#
# # ➕ Start New Bill
# def new_bill(request):
#     bill = Bill.objects.create(created_at=timezone.now())
#     return redirect('add_item', bill_id=bill.id)
#
#
# # ✍️ Add Item to Bill
# def add_item(request, bill_id):
#     bill = get_object_or_404(Bill, id=bill_id)
#     items = Item.objects.filter(bill=bill)
#     overall_total = sum(item.total for item in items)
#
#     if request.method == 'POST':
#         material = request.POST.get('material')
#         quantity = float(request.POST.get('quantity'))
#         rate = float(request.POST.get('rate'))
#         total = quantity * rate
#         Item.objects.create(
#             bill=bill,
#             material=material,
#             quantity=quantity,
#             rate=rate,
#             total=total
#         )
#         return redirect('add_item', bill_id=bill.id)
#
#     return render(request, 'add_item.html', {
#         'bill': bill,
#         'items': items,
#         'overall_total': overall_total,
#     })
#
# def create_bill(request):
#     bill = Bill.objects.create()  # create new bill
#     return redirect('add_item', bill_id=bill.id)
#
# # 🧾 View Bill
# def bill_view(request, bill_id):
#     bill = get_object_or_404(Bill, id=bill_id)
#     items = Item.objects.filter(bill=bill)
#     total = sum(item.total for item in items)
#     return render(request, 'bill.html', {'bill': bill, 'items': items, 'overall_total': total})
#
#
# # 🖨️ Generate PDF of Bill
# def bill_pdf(request, bill_id):
#     bill = get_object_or_404(Bill, id=bill_id)
#     items = Item.objects.filter(bill=bill)
#     total = sum(item.total for item in items)
#     context = {'bill': bill, 'items': items, 'total': total}
#     return render_to_pdf('pdf_template.html', context)
#
#
# # 🗃️ View All Bills
# def bill_history(request):
#     bills = Bill.objects.order_by('-created_at')
#     return render(request, 'history.html', {'bills': bills})
#
#
# # ✏️ Edit Item
# def edit_item(request, item_id):
#     item = get_object_or_404(Item, id=item_id)
#     if request.method == 'POST':
#         item.material = request.POST['material']
#         item.quantity = float(request.POST['quantity'])
#         item.rate = float(request.POST['rate'])
#         item.total = item.quantity * item.rate
#         item.save()
#         return redirect('add_item', bill_id=item.bill.id)
#
#     return render(request, 'edit_item.html', {'item': item})
#
#
# # 🗑️ Delete Item
# def delete_item(request, item_id):
#     item = get_object_or_404(Item, id=item_id)
#     bill_id = item.bill.id
#     item.delete()
#     return redirect('add_item', bill_id=bill_id)

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Bill, Item
from django.utils import timezone
from xhtml2pdf import pisa


# PDF render utility
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Error rendering PDF")
    return response


# Home Page
def index(request):
    return render(request, 'index.html')


# Create New Bill and Redirect to Add Item
def new_bill(request):
    bill = Bill.objects.create()
    return redirect('add_item', bill_id=bill.id)

#
# # Add Item to Bill
# def add_item(request, bill_id):
#     bill = get_object_or_404(Bill, id=bill_id)
#     items = Item.objects.filter(bill=bill)
#     total = sum(item.total for item in items)
#
#     if request.method == 'POST':
#         material = request.POST['material']
#         quantity = float(request.POST['quantity'])
#         rate = float(request.POST['rate'])
#         total_item = quantity * rate
#
#         Item.objects.create(
#             bill=bill,
#             material=material,
#             quantity=quantity,
#             rate=rate,
#             total=total_item
#         )
#         return redirect('add_item', bill_id=bill.id)
#
#     return render(request, 'add_item.html', {
#         'bill': bill,
#         'items': items,
#         'overall_total': total
#     })
def add_item(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    items = Item.objects.filter(bill=bill)
    overall_total = sum(item.total for item in items)

    if request.method == 'POST':
        if not bill.customer_name:
            customer_name = request.POST.get('customer_name')
            if customer_name:
                bill.customer_name = customer_name
                bill.save()

        material = request.POST.get('material')
        quantity = float(request.POST.get('quantity'))
        rate = float(request.POST.get('rate'))
        total = quantity * rate

        Item.objects.create(
            bill=bill,
            material=material,
            quantity=quantity,
            rate=rate,
            total=total
        )
        return redirect('add_item', bill_id=bill.id)

    return render(request, 'add_item.html', {
        'bill': bill,
        'items': items,
        'overall_total': overall_total,
    })
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Bill

def delete_bill(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    bill.delete()  # This also deletes all associated items
    messages.success(request, "Bill and all related items deleted successfully.")
    return redirect('history')



# View Single Bill
def bill_view(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    items = bill.items.all()
    total = sum(item.total for item in items)
    return render(request, 'bill.html', {
        'bill': bill,
        'items': items,
        'overall_total': total
    })


# Export PDF of Bill
def bill_pdf(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    items = bill.items.all()
    total = sum(item.total for item in items)
    context = {'bill': bill, 'items': items, 'total': total}
    return render_to_pdf('pdf_template.html', context)


# Bill History
def bill_history(request):
    bills = Bill.objects.order_by('-created_at')
    return render(request, 'history.html', {'bills': bills})


# Edit Item
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        item.material = request.POST['material']
        item.quantity = float(request.POST['quantity'])
        item.rate = float(request.POST['rate'])
        item.total = item.quantity * item.rate
        item.save()
        return redirect('add_item', bill_id=item.bill.id)

    return render(request, 'edit_item.html', {'item': item})


# Delete Item
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    bill_id = item.bill.id
    item.delete()
    return redirect('add_item', bill_id=bill_id)
from django.db.models import Sum, F

def overall_history(request):
    items = Item.objects.all().order_by('-id')

    total_quantity = items.aggregate(total_qty=Sum('quantity'))['total_qty'] or 0
    total_revenue = items.aggregate(total_sales=Sum('total'))['total_sales'] or 0

    return render(request, 'overall_history.html', {
        'items': items,
        'total_quantity': total_quantity,
        'total_revenue': total_revenue,
    })
