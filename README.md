# Placement Portal

A full-stack Placement Portal web application developed using Flask and deployed on AWS Cloud.

## Project Overview

The Placement Portal provides a simple authentication system for students.

Features include:

- Student Registration
- Student Login
- JWT Authentication
- Password Hashing using bcrypt
- Admin Login
- User Listing
- Logging System
- Input Validation

---

## Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Flask
- Flask-CORS
- PyJWT
- bcrypt
- python-dotenv

### Database

- Amazon RDS (MySQL)

### AWS Services

- Amazon EC2
- Amazon S3
- Amazon RDS
- AWS IAM
- Amazon CloudFront
- AWS Secrets Manager
- Amazon CloudWatch

---

## Project Structure

```
PlacementPortal/

│

├── backend/

│ ├── app.py

│ ├── config.py

│ ├── database/

│ ├── middleware/

│ ├── routes/

│ ├── services/

│ ├── utils/

│ ├── validators/

│ └── requirements.txt

│

├── frontend/

│ ├── index.html

│ ├── login.html

│ ├── register.html

│ ├── admin.html

│ ├── css/

│ ├── js/

│ └── images/

│

└── README.md
```

---

## AWS Architecture

```
                Internet

                    │

                    ▼

            Amazon CloudFront

                    │

                    ▼

            Amazon S3 (Frontend)

                    │

                    ▼

          Amazon EC2 (Flask Backend)

                    │

                    ▼

         Amazon RDS MySQL Database

                    │

                    ▼

          AWS Secrets Manager

                    │

                    ▼

          Amazon CloudWatch
```

---

## Features

- Secure Password Hashing
- JWT Authentication
- Role Based Authentication
- Admin Login
- User Registration
- Logging
- Validation
- AWS Cloud Deployment

---

## Future Enhancements

- Company Login
- Job Posting
- Student Dashboard
- Resume Upload
- Placement Tracking
- Interview Resources
- Roadmaps
- Email Notifications

---

## Author

Balagangadhar Kosanam

B.Tech – CSE (IoT, Cyber Security including Blockchain Technology)
