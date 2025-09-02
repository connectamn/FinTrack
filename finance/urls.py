from django.urls import path
from django.contrib.auth import views as auth_views
from finance.views import landing_view, RegisterView, DashboardView, TransactionView, TransactionListView, GoalCreateView, GoalListView, ProfileView, AdminDashboardView, export_transactions
urlpatterns = [
   path('', landing_view, name='landing'),
   path('login/', auth_views.LoginView.as_view(template_name='finance/registration/login.html'), name='login'),
   path('register/', RegisterView.as_view(), name='register'),
   path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
   path('transaction/add/', TransactionView.as_view(), name='transaction_add'),
   path('transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('goals/', GoalListView.as_view(), name='goal_list'),
   path('goal/add/', GoalCreateView.as_view(), name='goal_add'),
   path('generate-report/', export_transactions, name='export_transactions'),
]
