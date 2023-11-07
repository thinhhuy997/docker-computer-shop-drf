from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Product, Category, ImageURL, Note
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.pagination import PageNumberPagination
from .serializers import CategorySerializer, ProductSerializer, ImageURLSerializer, NoteSerializer

from .serializers import CustomTokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

# used for authorization
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

from api import serializers
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }

    return Response(api_urls)

############################ CATEGORY VIEWS #####################################


@api_view(['GET', 'POST'])
def CategoryMultipleCreate(request):
    if request.method == "GET":
        return Response({"This API used to create multiple categories!"})
    if request.method == "POST":
        for item in request.data['items']:
            # create a product object
            try:
                category_obj = Category.objects.create(
                    name=item['category_name'])
            except Exception as e:
                print(e)
                return Response({"An error occurred when creating multiple categories!"})
        return Response({"Created multiple categories successfully!"})


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


@api_view(['GET', 'PUT', 'DELETE'])
def CategoryDetail(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = CategorySerializer(category, many=False)
        return Response(serializers.data)
############################ END OF CATEGORY VIEWS ################################


############################ IMAGE URLS VIEWS #################################
class ImageurlListCreate(generics.ListCreateAPIView):
    queryset = ImageURL.objects.all()
    serializer_class = ImageURLSerializer
    filter_backends = [SearchFilter]
    search_fields = ['url']
############################ END OF IMAGE URLS VIEWS ##########################


############################ PRODUCT VIEWS ####################################
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name']
    # customized filter class
    filterset_class = ProductFilter

# page number pagination


class ProductListCreateAndPagePagination(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name']
    # customized filter class
    filterset_class = ProductFilter
    pagination_class = PageNumberPagination

# product list by list of ids


@api_view(['GET', 'POST'])
def ProductListFilterByIdList(request):
    if request.method == "GET":
        return Response({"This API use for get list of products by list of ids"})

    if request.method == "POST":
        id_list = request.data['ids']

        products = Product.objects.filter(pk__in=id_list)
        if products.exists():
            serializer = ProductSerializer(products, many=True)
            return Response({"count": len(serializer.data), "results": serializer.data})
        else:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def ProductDetail(request, slug):
    try:
        product = Product.objects.get(slug__iexact=slug)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = ProductSerializer(product, many=False)
        return Response(serializers.data)


@api_view(['GET', 'POST'])
def productMultipleCreate(request):
    if request.method == "GET":
        return Response({"This API used to create multiple products"})
    if request.method == "POST":
        for item in request.data['items']:

            # create a product object
            try:
                product_obj = Product.objects.create(name=str(item['product_name']).strip(), price=float(
                    item["product_price"]), description_from_crawler=item["product_description"])
            except Exception as e:
                print(e)

            # connect image_url object to above product object through foreign key
            try:
                for piu in item["product_img_urls"].split():
                    image_url_obj = ImageURL.objects.create(
                        url=piu, product=product_obj)
            except Exception as e:
                print(e)

        return Response({"testing..."})


@api_view(['GET', 'POST'])
def ProudctMultipleCreateByCategory(request, categoryId):
    i = 1
    try:
        category = Category.objects.get(id=categoryId)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = CategorySerializer(category, many=False)
        return Response(serializers.data)

    if request.method == "POST":
        for item in request.data['items']:
            # create a product object
            try:
                product_obj = Product.objects.create(name=str(item['product_name']).strip(), price=float(
                    item["product_price"]), description_from_crawler=item["product_description"])
                product_obj.categories.add(category)
                print("Process in - " + str(i))
                i += 1
            except Exception as e:
                print(e)
                return Response({"An error occurred when creating multiple categories!"})
            # connect image_url object to above product object through foreign key
            try:
                for piu in item["product_img_urls"].split():
                    image_url_obj = ImageURL.objects.create(
                        url=piu, product=product_obj)
            except Exception as e:
                print(e)
        return Response({"Created multiple categories successfully!"})


@api_view(['GET', 'POST'])
def productMultipleCreateWithCategories(request):
    if request.method == "GET":
        return Response({"This API is used to create multiple products with multiple categories"})

    if request.method == "POST":
        for dataset in request.data['datasets']:
            # if it doesn't exist, create a new one, if it already exists, get it and assign it to the variable "obj"
            category_obj, created = Category.objects.get_or_create(
                name=dataset['category_name'])

            for item in dataset['items']:
                # create a product object
                try:
                    product_obj = Product.objects.create(name=str(item['product_name']).strip(), price=float(
                        item["product_price"]), description_from_crawler=item["product_description"])
                    product_obj.categories.add(category_obj.id)
                    print("Product with id {} is created successfully!".format(
                        product_obj.id))
                except Exception as e:
                    print(e)

                # connect image_url object to above product object through foreign key
                try:
                    for piu in item["product_img_urls"].split():
                        image_url_obj = ImageURL.objects.create(
                            url=piu, product=product_obj)
                except Exception as e:
                    print(e)

        return Response({"testing..."})

############################ END OF PRODUCT VIEWS #####################################


# JWT view
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# Jwt authen-authorization testing


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


# only note owner can view their note
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def getDetailNote(request, pk):
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        print('-------request--------', request.user)
        if request.user != note.user:
            return Response(
                {'message': "You do not have permission to view this note!"},
                status=status.HTTP_403_FORBIDDEN)

        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)

    elif request.method == "PUT":
        if request.user != note.user:
            return Response(
                {'message': "You do not have permission to do thi action!"},
                status=status.HTTP_403_FORBIDDEN)

        serializer = NoteSerializer(note, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
