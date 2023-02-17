import environ
from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404

from back.models import Item
from mysite import settings


import stripe

from django.core.paginator import Paginator
env = environ.Env()

environ.Env.read_env()




def session_create(request, item_id=1):
    item = get_object_or_404(Item, id=item_id)
    SECRET_KEY = env('SECRET_KEY')
    stripe.api_key = SECRET_KEY
    session = stripe.checkout.Session.create(
        line_items=[
        {
          "price_data": {
            "currency": "usd",
            "product_data": {"name": item.name,
                             # 'description':item.description,
                             # 'price':item.price
                             },
                "unit_amount": item.price,
          },
          "quantity": 1,
        },
      ],
        mode='payment',
        success_url="http://localhost/success.html"
    )
    return JsonResponse({
        'session': session,
        'item_id':item_id,
    })

def item(request, item_id=1):
    item = get_object_or_404(Item, id=item_id)
    publish_key = env('PUBLISHABLE_KEY')
    return render(request, 'checkout.html', {'item': item,
                                             'publish_key': publish_key})


def index(request):
    item_list = Item.objects.all()
    paginator = Paginator(item_list, settings.POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html', {'page': page,
                                                'paginator': paginator,
                                                'post_list': item_list,
                                                })
