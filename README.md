# README

To begin create and activate the virtual environment if it doesn't already exist.

This creates the virtual environment

```
$ python3 -m venv venv
```

This activates the virtual environment

```
$ source venv/bin/activate
```

This installs the dependencies in the virtual environment

```
$ pip install -r requirements.txt
```

If you get an error: 
set the path

```
$ PATH="/usr/local/opt/icu4c/sbin:/usr/local/opt/icu4c/bin:$PATH"
```

Then run:

```
$ pip install pyicu

```

Then run this again:

```
$ pip install -r requirements.txt

```

---

In the future, you'll only have to activate the virtual environment with:
```
$ source venv/bin/activate
```
and 
```
$ source .env
```
to set the environment variables

---


```

