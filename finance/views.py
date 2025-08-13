from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from finance.forms import CustomUserCreationForm, CustomUserChangeForm, TransactionForm, GoalForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction, Goal, CustomUser
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from .admin import TransactionResource
from django.contrib import messages
from datetime import date

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, 'finance/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('dashboard')
        return render(request, 'finance/register.html', {'form': form})


class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.filter(user=request.user)
        goals = Goal.objects.filter(user=request.user)  # ✅ fetch all goals

        # Calculate totals
        total_income = transactions.filter(transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        total_expenses = transactions.filter(transaction_type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
        balance = total_income - total_expenses
        remaining_balance = balance

        # Expense breakdown by category for pie chart
        expense_by_category = (
            transactions
            .filter(transaction_type='expense')
            .values('category')
            .annotate(total=Sum('amount'))
            .order_by('-total')
        )

        expense_breakdown_labels = [entry['category'] for entry in expense_by_category]
        expense_breakdown_data = [float(entry['total']) for entry in expense_by_category]
        top_expense_category = expense_breakdown_labels[0] if expense_breakdown_labels else None
        top_expense_amount = expense_breakdown_data[0] if expense_breakdown_data else 0

        # Monthly expenses for last 12 months (histogram data)
        expense_monthly_qs = (
            transactions
            .filter(transaction_type='expense')
            .annotate(month=TruncMonth('date'))
            .values('month')
            .annotate(total=Sum('amount'))
        )

        expense_month_to_total = {row['month']: float(row['total']) for row in expense_monthly_qs}

        today_dt = date.today()
        start_year = today_dt.year
        start_month = today_dt.month
        monthly_labels = []
        monthly_expense_data = []
        for offset in range(11, -1, -1):
            total_months = start_year * 12 + start_month - 1 - offset
            year = total_months // 12
            month = total_months % 12 + 1
            month_date = date(year, month, 1)
            monthly_labels.append(month_date.strftime('%b %Y'))
            monthly_expense_data.append(expense_month_to_total.get(month_date, 0.0))

        # Calculate goal progress
        goal_progress = []
        for goal in goals:  #  loop over the queryset, not a single object
            if remaining_balance >= goal.target_amount:
                goal_progress.append({
                    'goal': goal,
                    'progress': 100
                })
                remaining_balance -= goal.target_amount
            elif remaining_balance > 0:
                progress = (remaining_balance / goal.target_amount) * 100
                goal_progress.append({
                    'goal': goal.name,
                    'progress': progress
                })
                remaining_balance = 0
            else:
                goal_progress.append({
                    'goal': goal,
                    'progress': 0
                })

        context = {
            'transactions': transactions,
            'goals': goals,
            'goal_progress': goal_progress,
            'total_income': total_income,
            'total_expenses': total_expenses,
            'balance': balance,
            'expense_breakdown': {
                'labels': expense_breakdown_labels,
                'data': expense_breakdown_data,
            },
            'top_expense_category': top_expense_category,
            'top_expense_amount': top_expense_amount,
            'monthly_expenses': {
                'labels': monthly_labels,
                'data': monthly_expense_data,
            },
        }

        return render(request, 'finance/dashboard.html', context)

        
class TransactionView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = TransactionForm()
        return render(request, 'finance/transaction_form.html', {'form': form, 'today': date.today().isoformat()})

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, 'Transaction added successfully.')
            return redirect('dashboard')
        return render(request, 'finance/transaction_form.html', {'form': form, 'today': date.today().isoformat()})


class TransactionListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.filter(user=request.user)
        return render(request, 'finance/transaction_list.html', {'transactions': transactions})


class GoalListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        goals = Goal.objects.filter(user=request.user)
        return render(request, 'finance/goal_list.html', {'goals': goals})


class GoalCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = GoalForm()
        return render(request, 'finance/goal_form.html', {'form': form, 'today': date.today().isoformat()})

    def post(self, request, *args, **kwargs):
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, 'Goal created successfully.')
            return redirect('dashboard')
        return render(request, 'finance/goal_form.html', {'form': form, 'today': date.today().isoformat()})

def landing_view(request):
    return render(request, 'finance/landing.html')
    
class AdminDashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request, 'Access denied. Staff privileges required.')
            return redirect('dashboard')

        total_users = CustomUser.objects.count()
        active_users = CustomUser.objects.filter(is_active=True).count()
        total_transactions = Transaction.objects.count()
        total_goals = Goal.objects.count()

        recent_users = CustomUser.objects.order_by('-date_joined')[:5]
        recent_transactions = Transaction.objects.select_related('user').order_by('-date')[:10]

        users_with_transactions = CustomUser.objects.filter(transaction__isnull=False).distinct().count()
        users_with_goals = CustomUser.objects.filter(goal__isnull=False).distinct().count()

        context = {
            'total_users': total_users,
            'active_users': active_users,
            'total_transactions': total_transactions,
            'total_goals': total_goals,
            'recent_users': recent_users,
            'recent_transactions': recent_transactions,
            'users_with_transactions': users_with_transactions,
            'users_with_goals': users_with_goals,
        }

        return render(request, 'finance/admin_dashboard.html', context)

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = CustomUserChangeForm(instance=request.user)
        return render(request, 'finance/profile.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        return render(request, 'finance/profile.html', {'form': form})

def export_transactions(request):
    user_transactions = Transaction.objects.filter(user=request.user)
    
    transaction_resource = TransactionResource()
    dataset = transaction_resource.export(queryset=user_transactions)
    
    excel_data = dataset.export('xlsx')
    
    # Create an HttpResponse with the correct MIME type for an Excel file
    response = HttpResponse(excel_data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
    # Set the header to prompt a download
    response['Content-Disposition'] = 'attachment; filename="transactions.xlsx"'
    return response