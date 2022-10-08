# Academy-website

## Overview: 
This project (CMS website) is one of my hobby projects. This project is meant to create for the educational academy. The technology used is HTML, CSS and JavaScript for frontend and Django for backend.

## Description:
This project contains different pages which are listed below.

1. User (Teacher) registration page
2. User (Teacher) login page
3. User (Teacher) profile page
4. Student Attendance page

Now we will see it one by one.

### Registration page:
This page is to register teacher so that he/she can login and mark and edit attendance. This is basically a form which contain different validations checks that are password must be greater than 7 and must contain number, alphabet and special character. The form also check that the person is already registered or not. If the user is already login he will not see this page he will be directed to user profile. Alert are used for messages.
### Login page:
This page is used for login if the member is already login this page will not appear instead the user will be directed to user profile. Alert are used for messages.
### User profile page:
This page contains the data of teacher also the marked attendances with attendances statistics. The teacher can edit the already marked attendance. 

If the teacher is already marked today attendance and he go to the attendance page, he will be notified that you have marked the attendance if you want to edit it you can go to your profile by clicking this button and on your profile hit edit so that you can edit today attendance. 

Once 24 hours complete no one can edit previous day attendance. 
The teacher can also search attendance by data if he wants to see the attendance statistics of specific day.

### Student Attendance page:
This page includes the data of the students and the option to mark their attendance. If teacher skip some student’s attendance skipped rows will be appear red.

Once the teacher mark attendance he needs to logout from website.

### Database schema:
The database used in this project is MySQL. There are total three tables used other tables are by default from Django. The three tables are student, teacher, and student_attendance.
- Student table contain information of all students. which contain fields of id, student_name, student_father_name, student_cnic and student_dob.
- Teacher table contain information of teacher. which contain fields of id, teacher responsibility and the table is related to Django auth_user table using foreign key.
- Student_attendance table contain information of student attendance. which contain fields of id, date, update_on_date, status and the table is related to student table using foreign key.



