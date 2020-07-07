# flask / mongodb backend


## Windows setup

```bash
pip uninstall virtualenv
pip uninstall pipenv

pip install pipenv
pipenv --version
```


## Development
### Install
```bash
pipenv install
```

### Start app
```bash
python run app.py
```

### Test curls
```
# get
curl --request GET http://localhost:5000/api/movies

curl --request GET http://localhost:5000/api/movies/5f0422426b8f7ff5da3c156e

# delete
curl --request DELETE http://localhost:5000/api/movies/5f0422426b8f7ff5da3c156e

# add
curl
  --header "Content-type: application/json"
  --request POST
  --data '{
      "name": "The Shawshank Redemption",
      "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
      "genres": ["Drama"]
  }' http://localhost:5000/api/movies

curl
  --header "Content-type: application/json"
  --request POST
  --data '{
      "name": "The Godfather ",
      "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
      "genres": ["Crime", "Drama"]
  }' http://localhost:5000/api/movies

# update
curl
  --header "Content-type: application/json"
  --request PUT
  --data '{
      "name": "The Shawshank Redemption",
      "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
      "genres": ["Comedy"]
  }' http://localhost:5000/api/movies/5f0421df6b8f7ff5da3c156d


```



