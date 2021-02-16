## Zenatix -  Assignment for FSD L1 @Zenatix

Stack used Python=3.8, Django=3.1.6

Postman collection - `https://www.getpostman.com/collections/f513a6328afa03ad3698`
Postman documentation - `https://documenter.getpostman.com/view/2862393/TWDTMz42`

##### Steps to run from github
1. Clone the repo `git clone https://github.com/kumarprafful/bakery-management-system`
2. Run `docker-compose up`
3. Create superuser - `docker exec -it <container_id> python manage.py createsuperuser`

or

2. Create and activate a virtual environment.
3. Run `pip install -r requirements.txt`
5. Run the migrations `python manage.py migrate`
7. Meanwhile run the Django server using `python manage.py runserver`

### Summary
Completed all the tasks except one bonus task of discounting rules by admin.