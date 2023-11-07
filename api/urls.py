from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import CustomTokenObtainPairView

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),

    # IWT Token
    # path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    ########################## Category #####################################
    path('category-list-create/', views.CategoryListCreate.as_view()),
    # category detail - function based views
    path('category-detail/<int:pk>', views.CategoryDetail),
    # used to create multiple categories
    path('category-multiple-create/', views.CategoryMultipleCreate),
    ########################### End of Category #############################

    ########################## Image Urls #####################################
    path('imageurl-list-create/', views.ImageurlListCreate.as_view()),
    ########################## End of Image Urls ##############################

    ########################### Products #######################################
    path('product-list-create/', views.ProductListCreate.as_view()),
    path('product-multiple-create-page-pagination/',
         views.ProductListCreateAndPagePagination.as_view()),
    path('product-detail/<slug:slug>/', views.ProductDetail),

    # used to get products by list of id
    path('product-list-by-ids/', views.ProductListFilterByIdList),

    # used to create multiple products
    path('product-multiple-create/', views.productMultipleCreate),
    path('product-multiple-create-by-category/<int:categoryId>',
         views.ProudctMultipleCreateByCategory),
    # Create multiple products with multiple categrories
    path('product-multiple-create-with-categories/',
         views.productMultipleCreateWithCategories),
    ########################### End of Product #############################

    # JWT authorization testing
    path('notes/', views.getNotes),
    path('note-detail/<int:pk>/', views.getDetailNote),
]
