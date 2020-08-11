# How to develop on these templates

To develop on these templates you should setup a virtual environment and activate it for example:

```bash
virtualenv venv
source venv/bin/activate
```

Then you can install the the required packages in that environment:

```bash
pip install -r requirements.txt
```

To run the tests, flake8 and black you can use the makefile:

```bash
make test
```

Or you can execute the commands that are defined in there manually.
