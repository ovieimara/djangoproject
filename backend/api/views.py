import json
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# Create your views here.

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    # body = request.body
    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print((request.POST))
    data = request.data
    instance = Product.objects.all().order_by('?').first()
    data = {}

    # if request.method != 'POST':
    #     return Response({'detail' : 'GET not allowed!'}, status=405)

    if instance:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # data = ProductSerializer(instance).data
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            print(serializer.data)

            return Response(serializer.data)

    return Response({"message" : "invalid data"}, status=400)
