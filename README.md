# FinExp - Personal Finance Tracker

A modern, user-friendly personal finance management application built with Django. Track your income, expenses, set financial goals, and visualize your spending patterns with interactive charts.

## Features

- **Custom User Authentication**: Enhanced registration and login system with additional user fields
- **User Profile Management**: Phone number, date of birth, bio, and profile information
- **Transaction Management**: Add and track income and expenses with categories
- **Financial Dashboard**: Visual overview of your financial status with real-time calculations
- **Interactive Charts**: 
  - Pie chart showing expenses by category
  - Bar chart displaying monthly expense trends (last 12 months)
- **Goal Setting & Tracking**: Set financial goals and track progress automatically
- **Data Export**: Export transactions to Excel format
- **Responsive Design**: Works on desktop and mobile devices
- **Admin Interface**: Comprehensive admin panel for user and transaction management

## Screenshots

- Modern dashboard with animated background and interactive charts
- Enhanced registration form with additional user fields
- Clean and intuitive user interface
- Mobile-responsive design
- Professional admin interface

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone or Download the Project
```bash
git clone <repository-url>
cd FinExp
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migrations
```bash
python manage.py migrate
```

### Step 5: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server
```bash
python manage.py runserver
```

### Step 7: Access the Application
Open your browser and go to: `http://127.0.0.1:8000/`

## Usage Guide

### For New Users

1. **Registration**: Click "Register" on the landing page to create your account
   - Fill in required fields: Username, Email, First Name, Last Name, Password
   - Optional fields: Phone Number, Date of Birth, Bio
2. **Login**: Use your credentials to log in
3. **Dashboard**: View your financial overview with charts and statistics
4. **Add Transactions**: 
   - Click "Add Transaction" in the navigation
   - Fill in the transaction details (title, amount, type, date, category)
   - Submit to add to your records
5. **View Transactions**: Click "View Transactions" to see all your entries
6. **Set Goals**: Click "Add Goal" to set financial targets
7. **Export Data**: Use "Generate Report" to download your transactions as Excel

### Transaction Categories
Common categories you can use:
- Food & Dining
- Transportation
- Entertainment
- Shopping
- Bills & Utilities
- Healthcare
- Education
- Travel
- Income (for earnings)

### User Profile Features
- **Enhanced Registration**: More detailed user information collection
- **Profile Management**: Update personal information through admin
- **User Analytics**: Track user activity and transaction patterns

## Project Structure

```
FinExp/
├── finance/                 # Main application
│   ├── templates/          # HTML templates
│   │   ├── finance/
│   │   │   ├── registration/  # Login templates
│   │   │   └── ...           # Other templates
│   ├── templatetags/       # Custom template filters
│   ├── migrations/         # Database migrations
│   ├── models.py           # Database models (CustomUser, Transaction, Goal)
│   ├── views.py            # View logic
│   ├── forms.py            # Form definitions (CustomUserCreationForm, etc.)
│   ├── admin.py            # Admin interface configuration
│   └── urls.py             # URL routing
├── finexp/                 # Project settings
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── SETUP.md                # Quick setup guide
```

## Technology Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite (can be changed to PostgreSQL/MySQL for production)
- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Charts**: Chart.js
- **Data Export**: Django Import-Export
- **Image Processing**: Pillow (for future profile picture support)
- **Custom User Model**: Extended AbstractUser with additional fields

## Custom User System

The application uses a custom user model (`CustomUser`) that extends Django's `AbstractUser` with:

- **Additional Fields**:
  - Phone Number (optional)
  - Date of Birth (optional)
  - Bio (optional)
  - Created/Updated timestamps
- **Enhanced Validation**: Username minimum length, unique email
- **Custom Forms**: `CustomUserCreationForm` and `CustomAuthenticationForm`
- **Admin Integration**: Full admin interface for user management

## Customization

### Adding New Features
1. Create new models in `finance/models.py`
2. Add corresponding views in `finance/views.py`
3. Create templates in `finance/templates/finance/`
4. Update URL patterns in `finance/urls.py`

### Styling
- The application uses Tailwind CSS for styling
- Custom CSS can be added to template files
- Chart colors and styles can be modified in the dashboard template

### User Model Extensions
To add more fields to the user model:
1. Add fields to `CustomUser` in `models.py`
2. Update forms in `forms.py`
3. Update admin configuration in `admin.py`
4. Create and run migrations

## Deployment

### For Production
1. Set `DEBUG = False` in `finexp/settings.py`
2. Configure a production database (PostgreSQL recommended)
3. Set up static file serving
4. Use a production WSGI server (Gunicorn, uWSGI)
5. Configure environment variables for security

### Environment Variables
Create a `.env` file for sensitive settings:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=your-database-url
```

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `runserver` command
   ```bash
   python manage.py runserver 8001
   ```

2. **Database errors**: Run migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Static files not loading**: Collect static files
   ```bash
   python manage.py collectstatic
   ```

4. **Custom user model issues**: Ensure `AUTH_USER_MODEL` is set correctly in settings

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review Django documentation
3. Create an issue in the repository

---

**Happy Financial Tracking! 💰📊**
