# How to develop on these templates

To develop on these templates you should set up a virtual environment and activate it.
For example:

```bash
virtualenv venv
source venv/bin/activate
```

Then you can install the required packages in that environment:

```bash
pip install -r requirements.txt
pip install -r dev-requirements.txt
```

If you ever need to update the dependencies or test dependencies you should update 
the `requirements.in` file or the `dev-requirements.in` file and run the command:

```
pip-compile requirements.in --upgrade
pip-compile dev-requirements.in --upgrade
```

To run the tests, flake8 and black you can use the makefile:

```bash
make test
```

Alternatively, you can manually execute the commands that are defined there as well.
