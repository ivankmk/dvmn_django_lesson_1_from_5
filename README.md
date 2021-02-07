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

To quickly fill the database, use the load_place management command, the argument for which is a list of links to json files with location data:

```python3 manage.py load_place http://website/file.json```

[Example of the json file with data](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json)

## Environment variable
Please create the file `.env` in the same folder as `manage.py` and save variables there as : `VARIABLE=value`.


## What this about?

The code done for educational purposes — this is the lesson from [Devman](https://dvmn.org).