# Lab 1 E-Commerce


## a. Objective

The overall objective of the lab is to create an e-commerce website. But, the first lab has the following objectives:
1. To install and create suitable running and compiling environments
2. To create superuser, users and run the server
3. To add modules and verify CRUD operation

## b. Introduction

We use different frameworks and environments for this lab. We have used VS Code as the IDE and Python/Django as the framework. An E-commerce website is a website that helps customers and sellers in buying/selling their products on the online platform. It is one of the best modern ways of business. E-commerce websites simplify the buying process of goods and services. We will be creating an e-commerce website for this lab report.

Additionally, we also need to know about the languages. Python is the most popular programming language with easy understanding and efficient structure. We use Django, a web-based open-source framework of Python. Django comes with many inbuilt models which makes us easier to focus on the writing part of the application. And VS Code is one of the most versatile IDE out there. 

Git is also used in this lab for source control. We can also use Github Desktop for commit'ing and push'ing the code into a repository on GitHub. That repository when made public can be shared with anyone .


## c. Procedure
We did the following steps in this lab:

**1. Initializing environment**

We downloaded the software and environments required for the project. Those were:
* Python
* Pip
* Sqlite
* DBeaver
* Django
* VS Code
* Github account

We had some of them already and set up the remaining. The software could be different in the case of different operating systems with the same functionality. We checked if everything was working as it should.

**2. Migrating and creating users**

After the environment setup, we started the project and migrated files.

Syntax: 
*django-admin startproject ecommerce_barun
cd ecommerce_barun
python manage.py migrate*

We ran the server if it was working. Then, we got the link for the server as 127.0.0.1:8000. Again, we verified the admin side using 127.0.0.1:8000/admin. We were able to create a superuser and other users.
Syntax: *python manage.py runserver* 

**3. Database verification and CRUD operations**

Then, we added a module product_module and migrated files to the database. Now, we were able to do CRUD operations on the server.
Syntax: *python manage.py startapp product_module
…….
python manage.py runserver*

**4. Source Control**

Finally, we used Git for source control. We created a repository with the name ecommerce_barun and created a markdown file “lab1.md” which is this document. Then, we committed and pushed the code and folder to the repository. The repository is now available at:
https://github.com/thebarunsharma/ecommerce_barun/

## d. Output

1. Installation of python| pip
![alt text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/08ad10ce-8f45-400d-ba2e-50dbf565aeea/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220519T134824Z&X-Amz-Expires=86400&X-Amz-Signature=e026c27806c4549ad3049e442f91b8773335ee01e8df4042794450ccb9acca45&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

2. Creation of project folder
![alt text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/98e6e486-a865-49ff-9ebd-6e0315f52d6b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220519T135152Z&X-Amz-Expires=86400&X-Amz-Signature=ef1863075e5395dca061b59048a29c84ff3c4dc7a88deb91d6add30da379f8b2&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
4. Migration
![alt text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/09951f63-4415-4d38-8a43-3747047343ae/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220519T135130Z&X-Amz-Expires=86400&X-Amz-Signature=a037ff5ff05587fbfee9581d05834776d97e44dcecccb4d5306ff3715e9ffb2e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)


5. Creating superuser
![alt text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9a7fd7a5-3ee5-40f6-9710-cf514481a934/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220519T135113Z&X-Amz-Expires=86400&X-Amz-Signature=02ab6fc16671fb191b282c3da55887ca1c55e12dde9450412f9330bb355f4df3&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
5. Running server
![alt text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/78f40bd7-92d6-4735-9631-854046a1e1ef/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220519T135230Z&X-Amz-Expires=86400&X-Amz-Signature=28c577eb260b0e95a508c993f3007decf732635bc502fac0a192279f5ca32bc6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
![alt text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6fefcb8c-3e4b-4311-8480-7fd4bef9388b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220519T135331Z&X-Amz-Expires=86400&X-Amz-Signature=91e17a8e0b44b92d76f579c4dc2859b670f1fd72dc920cab57b1455f81983198&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
6. Logging In
![alt text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f6abd733-4320-4763-993c-f163b07d228f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220519T135046Z&X-Amz-Expires=86400&X-Amz-Signature=13dc03f54ab4b94781578494469b590af2d28475dde03b3068a0be7631340515&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

8. CRUD operation
![alt text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7da75c7b-668d-43de-bc3a-9494f1a17621/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220519T135022Z&X-Amz-Expires=86400&X-Amz-Signature=c5eef90445349d6f447f3e7882f1228f7655c1f72eecef1d1208b50f55a3a1a5&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

10. Git initialization
![alt text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/463198b6-a56a-4c0f-8f88-15b2ba2cf956/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220519T134951Z&X-Amz-Expires=86400&X-Amz-Signature=d3f28cc6e9ee12e75626501e7621862c05de0fa9fb8c37b710005ad59d609d23&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

## e. Conclusion 

The first lab of e-commerce taught us many things. Initial setup helped us create environments and setup efficiently. Then, we knew how to start a project using Django. Knowledge about running the server was also obtained. We knew how to do CRUD operations on the server. Finally, we also knew more about source control using Git and Github. Making a repository on Github and sharing it made our code easily accessible. 



