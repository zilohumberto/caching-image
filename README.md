# caching-image


# Load Image Service 
    - load all image from the api and storage into a redis cache service
    - those images are storage from camera, author, tags and id (to search purpose) 

# Get Image Service 
    -  generate a dict with the query params from the user request
    -  call serach engine to look into redis cache into camera tags and author key
    -  if the query param match with any of this list is added to a raw result
    -  all raw result load the complete data from redis by id (avoiding repeated ids)

# Search engine
    - Just look into redis list for key
    - Keys availabes are: camera, author, tag

# In redis is store:
    - by id: all image information
    - by camera-<name>: list of ids 
    - by author-<name>: list of ids
    - by tag-<name>: list of ids 

# Vars


# Request example
    - /search?tag=%23whataview

# Response example
```json
    [
      {
        "author": "Notable Medium",
        "camera": "Polaroid OneStep 2",
        "cropped_picture": "http://interview.agileengine.com/pictures/cropped/697082.jpg",
        "full_picture": "http://interview.agileengine.com/pictures/full_size/697082.jpg",
        "id": "c647b64d79f9fce52e0b",
        "tags": "#wonderfulday #photooftheday #greatview #whataview #nature #beauty #natureisbeautiful "
      },
      ...
    ]
```