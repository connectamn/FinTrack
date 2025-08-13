# Quick Setup Guide for FinTrack

## 🚀 Get Started in 5 Minutes

### 1. Install Python
Make sure you have Python 3.8+ installed on your system.

### 2. Download/Clone the Project
- Download the project files or clone the repository
- Navigate to the project folder: `cd FinTrack`

### 3. Set Up Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Set Up Database
```bash
python manage.py migrate
```

### 6. Run the Application
```bash
python manage.py runserver
```

### 7. Open in Browser
Go to: `http://127.0.0.1:8000/`

## 🎯 First Steps for New Users

1. **Register**: Click "Register" and create your account
   - **Required**: Username, Email, First Name, Last Name, Password
   - **Optional**: Phone Number, Date of Birth, Bio
2. **Login**: Use your credentials to log in
3. **Add Your First Transaction**: 
   - Click "Add Transaction"
   - Fill in the details (e.g., "Coffee", $5.00, Expense, Food & Dining)
   - Submit
4. **Explore Dashboard**: See your financial overview with interactive charts
5. **Set a Goal**: Click "Add Goal" to set a savings target

## 💡 Pro Tips

- Use descriptive categories for better chart analysis
- Add both income and expenses for accurate balance tracking
- Export your data regularly using "Generate Report"
- The dashboard shows your spending patterns over time
- Customize your profile with additional information
- Use the admin panel for advanced user management

## 🔧 Admin Access

To access the admin panel:
1. Create a superuser: `python manage.py createsuperuser`
2. Go to: `http://127.0.0.1:8000/admin/`
3. Manage users, transactions, and goals

## 🆘 Need Help?

- Check the main README.md for detailed documentation
- Ensure all dependencies are installed correctly
- Make sure your virtual environment is activated
- Try running `python manage.py check` to verify setup
- Check that migrations are applied: `python manage.py migrate`

## 🆕 What's New

- **Custom User System**: Enhanced registration with additional fields
- **Interactive Charts**: Pie chart and monthly expense histogram
- **Professional Admin**: Comprehensive admin interface
- **Better Forms**: Styled forms with validation
- **User Profiles**: Additional user information management

---

**Ready to track your finances? Let's go! 💰**
