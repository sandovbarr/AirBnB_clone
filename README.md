![GitHub contributors](https://img.shields.io/github/contributors/sandovbarr/AirBnB_clone?color=success)
![GitHub stars](https://img.shields.io/github/stars/sandovbarr/AirBnB_clone?color=red)
![Twitter Follow](https://img.shields.io/twitter/follow/elhumanimal?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/SergioDiaz90?style=social)

<p align="center">
<img width="340" src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20200701%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200701T222646Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3c90e4dc7b1186f772d72fb9fb588debd7784890e60d85f345177c9c1c2c0ab1">

<h1 align="center">AirBnB Clone</h1>
This project is one of the first steps in the AirBnB clone which focuses on creating a console for editing, managing or managing the object-oriented programming of this platform.
</p>


### The console
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”.

This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console will be a tool to validate this storage engine

<p align="center">
<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20200701%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200701T222646Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c583817d8776b3009106b0bbe7441fb5cfd1111086e59dae48b5cb66f8f76053"></p>


### Funcionalities of command line

- Create new objects based in the class imported.
- Show an instance the an class with determineted ID.
- Destroy is for delete an intance created.
- Do all to show all instance create until now or with determinated class.
- Update it serves for add new information of attributes in an instance.
- Default this method for use updates for use other methods.

#### Super Class
- BaseModel
#### Usage
You have to clone this repo and execute ./console.py
``` bash
$ git clone https://github.com/sandovbarr/AirBnB_clone.git
$ ./console
```

### Contributing
Requests for changes are welcome. For major changes, first open a verification and meeting to discuss the change.

#### Project files
| File/folder | Description/functions |
|-------|-----------|
| **[README.md](./README.md)** | *All what you need to understand this project*|
| **[_ _init__.py](./models/__init__.py)** | Trasnform models-folder as a module and create a single instance of FileStorage |
| **[amenity.py](./models/amenity.py)** | first class for create objects or instance turns |
| **[baseModel.py](./models/base_model.py)** | first class for create objects or instance |
| **[city.py](./models/city.py)** | class than inherits from BaseModel Class |
| **[console.py](./console.py)** | *Use console for objects management* |
| **[state.py](./models/state.py)** | class than inherits from BaseModel Class |
| **[place.py](./models/place.py)** | class than inherits from BaseModel Class |
| **[review.py](./models/review.py)** | class than inherits from BaseModel Class |
| **[user.py](./models/user.py)** | class than inherits from BaseModel Class |
| *[engine](./models/engine)* | **Folder for engine files** |
| **[_ _init__.py](./models/engine/__init__.py)** |  Trasnform models-folder as a module and create a single instance |
| **[FileStorage.py](./models/engine/FileStorage.py)** | Class for management functions for proof the objects |
| *[tests](./models/tests)* | **Unittest module** |
| **[_ _init__.py](./models/engine/__init__.py)** | Trasnform tests-folder as |
| *[tests/tests_models](./models/tests/tests_models)* | **Folder for unittest** |
| **[test_amenity.py](./tests/test_models/test_amenity.py)** | Unittest file |
| **[test_baseModel.py](./tests/test_models/test_base_model.py)** | Unittest file |
| **[test_city.py](./tests/test_models/test_city.py)** | Unittest file |
| **[test_state.py](./tests/tests/test_models/test_test_state.py)** | Unittest file |
| **[test_place.py](./tests/test_models/test_test_place.py)** | Unittest file |
| **[test_review.py](./tests/test_models/test_test_review.py)** | Unittest file |
| **[test_user.py](./tests/test_models/test_test_user.py)** | Unittest file |
| *[tests/tests_models/test_engine](./models/tests/tests_models/test_engine)* | **Folder for unittest** |
| **[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py)** | Unittest file |


## Authors
Jairo Sandoval - [@sandovbarr](https://github.com/sandovbarr)<br>
Sergio Diaz - [@S3RG1O1994](https://github.com/S3RG1O1994)<br>
