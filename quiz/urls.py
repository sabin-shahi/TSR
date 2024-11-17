from django.urls import path, include
from .views import QuizListView, CategoriesListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizDetailView, QuizTake

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz_index'),
    path('quiz_category_list_all', CategoriesListView.as_view(), name='quiz_category_list_all'),
    path('category/<category_name>/', ViewQuizListByCategory.as_view(), name='quiz_category_list_matching'),
    path('quiz_progress', QuizUserProgressView.as_view(), name='quiz_progress'),
    path('marking/', QuizMarkingList.as_view(), name='quiz_marking'),
    path('marking/<pk>/', QuizMarkingDetail.as_view(), name='quiz_marking_detail'),
    path('<slug>/', QuizDetailView.as_view(), name='quiz_start_page'),
    path('<quiz_name>/take/', QuizTake.as_view(), name='quiz_question'),
]