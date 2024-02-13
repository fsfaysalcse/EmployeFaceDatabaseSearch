# Employee Face Search

![title](https://img001.prntscr.com/file/img001/4P9PThYlQnSzjgmiEF0pVQ.png)

### Overview

This is a simple face detection application. It is a part of a complete employee management system. This application is
used to detect the face of the employee and store the face data in the database. The server will be used to store the
face data and the client will be used to detect the face of the employee. The server is built with Flask and the client
is built with Python and OpenCV.

Here Android Client Source Code
repository: [Employee Face Search Android](https://github.com/fsfaysalcse/EmployeeFaceSearch/tree/main)

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/fsfaysalcse/FaceUnlockFlask.git
    ```

2. Install the required packages
    ```sh
       pip install -r requirements.txt
   ```
3. Configure Database
   ```sh
   # Open the app.py file and change the database configuration
   # Change the database configuration
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
   ```   
4. Run the server
   ```sh
   python app.py
   ```

Congratulations! You have successfully installed the server.

### Usage

---

#### Add Employee Data

**Add Employee** Data by sending a POST request to the server. You can use the following command to send a POST request
to
the server. The server will store the employee data in the database.

```sh
curl --location 'http://127.0.0.1:9090/upload' \
--form 'name="Mohammad Kaif"' \
--form 'email="kaif@gmail.com"' \
--form 'photo=@"/Users/fsfaysalcse/Desktop/Screenshot at Feb 13 7-39-20 AM.png"'
```

#### Detect Employee Face

**Detect Employee** Face by sending a POST request to the server. You can use the following command to send a POST
request to the server. The server will detect the employee face and return the employee data.

```sh
curl --location 'http://127.0.0.1:9090/search' \
--form 'photo=@"/Users/fsfaysalcse/Downloads/WhatsApp Image 2024-02-08 at 5.15.28 PM (1).jpeg"'
```

---
Note: You can use the client application to detect the employee face. The client application is built with Python and
OpenCV. You can find the client Android application in the following repository.
Android Client Repository: [Employee Face Search Android](https://github.com/fsfaysalcse/EmployeeFaceSearch/tree/main)


**Ask Me Anything , I'm here to help you :) →**

[![LinkedIn Connect](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/fsfaysalcse/)[![Twitter: Follow](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/fsfaysalcse)[![Facebook Follow](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/fsfaysalcse/)[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:fsfoysal15@gmail.com?subject=From%20GitHub&body=Hi,%20there.%20Found%20you%20from%20GitHub.)


