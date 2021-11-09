# Absolute Control FastAPI

## Introduction

This is a restful implementation of the Absolute Control python library using FastAPI.

## Usage

Inside of a python environment, run the following commands to install and run the application.
```bash
pip install -r requirements.txt
python run.py
```

If you prefer to use docker, you can run the following commands to run the application.
```bash
docker build -t api --target RUN .
docker run api
```

If you would like to pull from docker hub, you can use the following image.
```
royaldog/absolute-control-fastapi:tagname
```

## Testing

To test the library you can use the `./run_tests.py` script. It is highly recommended to use the docker image. These tests could shut down your system and cause harm.

Using docker, you can run the tests.
```bash
docker build -t tests --target TEST .
docker run tests
```

You should not run these tests on your system, but if you have a death wish, you can run them.
```bash
pip install pytest coverage
python run_tests.py
```

## License

This project is licensed under the MIT license.

## Contribution

This project is open source. You can contribute to the project by making a pull request or by sending an email to [Johnny Irvin](mailto:irvinjohnathan@gmail.com)