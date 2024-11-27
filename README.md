# **DJANGO PROJECT - Folders & Files Structure**

<a href="https://ibb.co/Df0HCjT"><img src="https://i.ibb.co/m5fVqPg/Django-Project-Structure-Overview.png" alt="Django-Project-Structure-Overview" border="0"></a>

# **Setup Django Project Structure, by following these steps:**


## **STEP 1**

- After you cloned the repo, go inside the folder **django_porject_stucture** and remove **.git** folder, because later you might want to create github repository related to your own project name.

	- With the command:

```bash
	rm -rf .git
```
## **STEP 2**

- From the working directory **django_project_structure** you will change the folder name accordingly.

	- With the command:

```bash
	cd .. && mv django_project_structure your_project_name

```	

## **STEP 3**

- After, you need to go to  **your_project_name** folder.

	- With the command:
	
```bash 
	cd your_project_name
```
## **STEP 4**

- Create virtual environment with **venv**.

	- With the command:
```bash
	python3 -m venv .venv --prompt your_project_name
```
- Activate **venv**

	- With the command:

```bash
	source .venv/bin/activate
```

## **STEP 5**

- Install requirements.

	- With the command:

```bash
	make dev-install
```


## **STEP 6**

**Note:** Before you create the database, please make sure your **PostgreSQL** are runnning and you able to access **postgres** database with the username **postgres**
- Create your project database, by running the python script inside **create_DB_NAME.py** file.

	- With the command:
```bash
	python3 -m create_DB_NAME
```
**Note:** *this will prompt you to give the name of your database (you can name it as you wish).*


## **STEP 7**

- You might also would like to create the **`DB_USER`** ***(database username)*** and **`DB_PWD`** ***(database password)***

	- With the command:

```bash
	python3 -m create_DB_USER_n_DB_PWD
```

## **STEP 8** 

- Last but not least generate a **`SECRET_KEY`**, which later you will add to `.env` file.

	- To generate the Secret Key

		-  With the command:

```bash
	python3 -m generate_SECRET_KEY`
```

## **STEP 9**

- Once you have created and generated all the information in **STEP 6**, **STEP 7**, and **STEP 8** now you need to create **.env**

	- With the command

```bash
	nano .env
```

Copy paste the below text, and fill out the blanks with you own information:

```bash
SECRET_KEY=      
DB_NAME=
DB_USER=
DB_PWD=
DB_PORT=5432
DB_HOST=localhost
```

## **STEP 10**

- When you done, do a django migrate

	- With running the command:

```bash	
	make dev-m
```

- You can now, go a head run django server to check if it's working correcly before you create different apps.

	- With running the command:

```bash
	make
```
# **Extra Info**

 - To create an app, you need to go to **apps** folder.

 	-  With the commmand:

```bash
	cd apps
```

 - Within the folder, you create as many apps you want.

 	- With the command:

```bash
	python3 ../manage.py startapp appname
```

**Note:** change **appname** with your own app name.

## **For you who would like to have a better idea or understanding, please checkout **Eyong Kevin's** github**

 >  **https://github.com/Eyongkevin/django-boilerplate**