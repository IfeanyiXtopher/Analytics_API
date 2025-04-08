# Django Analytics API

A REST API for tracking and analyzing website visits with JWT authentication.
## Features

- User Authentication (JWT tokens)
  	User registration
  	Login with access/refresh tokens
- Visit Tracking
  	Record website visits (IP, URL, country, device type)
  	Auto-generated timestamps
- Analytics
  	Total visit counts
  	Visits by country
  	Visits by device type
  	Daily visit trends
-Dev Tools
  	SQLite database (default)
  	Postman documentation

## Setup Instructions

### 1. Prerequisites
 Python 3.8+


### 2. Installation
bash
# Clone repository
git clone https://github.com/IfeanyiXtopher/Analytics_API.git
cd Analytics_API

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt


### 3. Configuration
Create .env file:
env
SECRET_KEY=your-django-secret-key
DEBUG=True


### 4. Database Setup
python manage.py migrate
python manage.py createsuperuser


### 5. Run Development Server
python manage.py runserver





## API Endpoints

### Authentication
Endpoint          			Method 	  		   Description 
/user/register/ 			   POST   				Create new user           
/user/login/    			   POST   				Get JWT tokens            
/user/refresh/  			   POST   				Refresh access token      

### Analytics
 Endpoint                	Method  			   Description                     
 /api/visits/        		POST   			   Record new visit (authenticated)
 /api/visits/stats/   		GET    			   Get aggregated visit statistics (authenticated)





## Generating Test Data
Create 10,000 sample visits:
bash
python manage.py generate_visits





## Usage Examples

### 1. Register User
bash
curl -X POST http://localhost:8000/user/register/ 
  -H "Content-Type: application/json" 
  -d '{"username":"testuser", "email":"test@example.com", "password":"secure123", "password2":"secure123"}'


### 2. Login (Get Tokens)
bash
curl -X POST http://localhost:8000/user/login/ 
  -H "Content-Type: application/json" 
  -d '{"username":"testuser", "password":"secure123"}'


### 3. Record Visit (Authenticated)
bash
curl -X POST http://localhost:8000/api/visits/ 
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" 
  -H "Content-Type: application/json" 
  -d '{"ip_address": "192.168.1.1", "page_url": "https://example.com", "country": "US", "device_type": "desktop"}'


### 4. Get Statistics
bash
curl http://localhost:8000/api/visits/stats/ 
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"



## Documentation
- [Postman API Documentation](https://documenter.getpostman.com/view/33125691/2sB2cVg2vT#8b142751-8123-45f2-bf11-6a61d90aeeac)



## Project Structure
Analytics_API/
├── analytics/            # Visit tracking app
│   ├── models.py         # Visit data model
│   ├── serializers.py    # Data serializers
│   ├── views.py          # API endpoints
│   └── management/       # Fake data command
├── users/                # Authentication app
│   ├── serializers.py    # User registration
│   └── views.py          # Auth endpoints
├── .env                  # Environment variables
└── requirements.txt      # Dependencies

