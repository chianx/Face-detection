# Criminal Identification System
***
## Problem Statement
***
Develop a desktop app to demonstrate application of Face Recognition technology in areas of criminal detection

## Solution
***
A **Criminal Identification System** is made to help any Law Enforcemnet Agency to identify and track criminals stored in their database easily and efficiently.
The application will use OpenCV Technology to identify faces of criminals in the data provided by the user. If any criminal is identified in surviellance video, the user is immediately notified with a text message on his phone number.

## Technologies used
***
- Python
- OpenCV
- MySQL
- Tkinter
- Twilio

## Features
***
- The most differenciating feature of my application is **SMS Notifation**.
- The app can even track a **Live CCTV** footage.
- Maintains Database
- Image Recognition
- Identification of Criminals in **Pre-Recorded Videos**.

## Data Flow Diagram
***![Data Flow Diahgram](https://user-images.githubusercontent.com/69694356/171285517-82c94401-b59d-4061-9df6-333dd3d8ac01.png)

## How to get started
***
### Prerequisites
- Python and pip must be installed.
- MySQL must be installed.

### Now, follow the following steps
- Download the project from github.
- Write the following commands in command prompt or trerminal of your choice :
 ```
  pip install Pillow
  pip install twilio
  pip install pymysql
  pip install opencv-python
  pip install opencv-contrib-python
  pip install tk
```
  *Make sure opencv-python and opencv-contrib-python have same versions, if not then download same versions otherwise the code will not work.
  *Make sure, you have all the other python libraries installed, if not, then install them using pip.
- Now, open MySQL Command Line, enter your password and write the following commands:
```
  create database criminaldb;
  create table criminaldata(id int primary key auto_increment, `name` varchar(20) not null, `father name` varchar(25),`mother name` varchar(25),
  gender varchar(6) not null, dob varchar(10), `blood group` varchar(5), `identity mark` varchar(30) not null, nationality varchar(15) not null,
  `religion` varchar(15) not null, `crimes` text not null);
```
- Then, to check the data in your database: 
  ```
  select * from criminaldata;
  ```
- Now, open dbHandler.py file and enter username and password of your MySQL Server in both the functions : insertData() as well as retrieveData() to connect your application to MySQL successfully.
- Create an account on twilio for free, and then you will be provided with : 
  - account_sid
  - auth_token
  - a phone number
- Enter these details along with your own phone number in sendMsg() function in twilioMsg.py file.
- Now, create a new folder named "face_samples" in the same folder or directory where other files of this project are saved
- Now, you are all set to go..... 
- RUN home.py file , a Tkinter screen will open
- Enter details of criminals and test this app
 **View my You Tube video to see how this app works -->**
 > https://www.youtube.com/watch?v=4CA4DF00h5A

## Have a look at this project
***




