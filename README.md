# Career Guidance Web Application

Full-stack career guidance platform with Flask + MongoDB Atlas backend and Vanilla HTML/CSS/JS frontend.

## Features

- JWT authentication with roles: `admin`, `student`
- Secure bcrypt password hashing
- Role-based access control (RBAC)
- Career listing/detail with pagination
- Mentor listing/detail and booking system
- Reviews and ratings for mentors
- User dashboard and profile goal tracking
- Responsive chatbot with career assistant replies
- Centralized error handling, validation, CORS, and logging
- Production-ready modular backend architecture

## Tech Stack

- **Backend:** Flask, PyMongo, PyJWT, bcrypt, Flask-CORS
- **Database:** MongoDB Atlas
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Deployment:** Render/Railway (backend), Netlify/Vercel (frontend)

## Folder Structure

```text
backend/
  app/
    routes/
    controllers/
    models/
    services/
    middleware/
    utils/
  config.py
  run.py
  requirements.txt
  .env.example

frontend/
  assets/
    css/styles.css
    js/api.js
    js/main.js
  index.html
  login.html
  signup.html
  dashboard.html
  profile.html
  careers.html
  career-detail.html
  mentors.html
  chatbot.html
  mentor-detail.html
  booking.html
  booking-confirmation.html
  admin.html
  about.html
  contact.html
  faq.html
  404.html
```

## API Documentation

Base URL: `/api/v1`

### Auth
- `POST /auth/register`
- `POST /auth/login`

### Users
- `GET /users/profile` (JWT)
- `PUT /users/profile` (JWT)

### Careers
- `GET /careers?page=1&limit=10`
- `GET /careers/:id`

### Mentors
- `GET /mentors`
- `GET /mentors/:id`

### Bookings
- `POST /bookings` (JWT)
- `GET /bookings/me` (JWT)

### Reviews
- `POST /reviews` (JWT)
- `GET /reviews/mentor/:mentor_id`

### Chatbot
- `POST /chat/message`
- `GET /chat/suggestions`

### Admin
- `POST /admin/careers` (JWT + admin role)

## Database Collections

- `users`
- `mentors`
- `careers`
- `bookings`
- `reviews`

Indexes:
- Unique index on `users.email`
- Index on `careers.career_title`

## Setup Instructions

### 1) Backend local setup

1. Open terminal in `backend`
2. Create and activate virtual environment
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Copy `.env.example` to `.env`
5. Configure:
   - `MONGO_URI`
   - `MONGO_DB_NAME`
   - `SECRET_KEY`
   - `CORS_ORIGINS`
6. Run server:
   - `python run.py`

### 2) MongoDB Atlas setup

1. Create Atlas cluster
2. Create database user and password
3. Add IP access (or `0.0.0.0/0` for testing)
4. Put connection string into `MONGO_URI` in `.env`

### 3) Frontend local setup

1. Open `frontend` with a static server (e.g. VSCode Live Server)
2. Ensure backend runs on `http://127.0.0.1:5000`
3. Open `index.html`

## Deployment

### Backend (Render/Railway)

1. Deploy `backend` directory
2. Start command: `python run.py`
3. Add environment variables from `.env.example`

### Frontend (Netlify/Vercel)

1. Deploy `frontend` directory
2. Update `API_BASE_URL` in `frontend/assets/js/api.js` to deployed backend URL

## Security Notes

- Store secrets in environment variables only
- Use strong `SECRET_KEY`
- Keep CORS origins restricted in production
- Never expose MongoDB credentials in frontend code
