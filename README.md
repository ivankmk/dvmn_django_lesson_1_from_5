# Where to go 🐻
Website about intersting places in Moscow
[Demo](https://ivankmk.pythonanywhere.com/)

!['Main page'](extra/screen.png)


## Running

- Install dependencies `pip install -r requirements.txt`
- Go to the folder `cd where-to-go` 
- Create the file `.env` with variables ```DEBUG```,  ```STATIC_DIR``` and ```SECRET_KEY```
- Initiate DB`python3 manage.py migrate`
- Run the server `python3 manage.py runserver`


## Environment variable
Please create the file `.env` in the same folder as `manage.py` and save variables there as : `VARIABLE=value`.


## What this about?

The code done for educational purposes — this is the lesson from [Devman](https://dvmn.org).