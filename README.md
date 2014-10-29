# Audit Plugin

Add this dependency to ```requirements.txt```:

    lraudit==0.1.1

Initialise in your Flask app like so to get tagged auditing:

    from audit import Audit

    app = Flask(__name__)
    Audit(app)

# Example

Here's an example of a non-logged-in user asking for the app root, then logging in, then going to the ```/registration``` endpoint:

    --------------------------------------------------------------------------------
    127.0.0.1 - - [05/Aug/2014 20:59:24] "GET /login?next=%2F HTTP/1.1" 200 -
    --------------------------------------------------------------------------------
    INFO in __init__ [/home/opyate/.virtualenvs/casework-frontend/src/audit/audit/__init__.py:32]:
    Audit: user=[anon], request=[<Request 'http://localhost:8000/login' [POST]>], session=[<SecureCookieSession {u'_id': 'cb3471d019b91e1b4fe2a65ab521c757'}>]
    --------------------------------------------------------------------------------
    127.0.0.1 - - [05/Aug/2014 20:59:32] "POST /login HTTP/1.1" 302 -
    --------------------------------------------------------------------------------
    INFO in __init__ [/home/opyate/.virtualenvs/casework-frontend/src/audit/audit/__init__.py:32]:
    Audit: user=[{'id': '1', 'email': 'test@example.org'}], request=[<Request 'http://localhost:8000/' [GET]>], session=[<SecureCookieSession {u'_fresh': True, u'user_id': u'1', u'_id': 'cb3471d019b91e1b4fe2a65ab521c757'}>]
    --------------------------------------------------------------------------------
    127.0.0.1 - - [05/Aug/2014 20:59:32] "GET / HTTP/1.1" 200 -
    --------------------------------------------------------------------------------
    INFO in __init__ [/home/opyate/.virtualenvs/casework-frontend/src/audit/audit/__init__.py:32]:
    Audit: user=[{'id': '1', 'email': 'test@example.org'}], request=[<Request 'http://localhost:8000/registration' [GET]>], session=[<SecureCookieSession {u'_fresh': True, u'user_id': u'1', u'_id': 'cb3471d019b91e1b4fe2a65ab521c757'}>]
    --------------------------------------------------------------------------------
    127.0.0.1 - - [05/Aug/2014 20:59:35] "GET /registration HTTP/1.1" 200 -


The downstream log viewer can now track this particular user's session throughout by filtering on ```cb3471d019b91e1b4fe2a65ab521c757```, which is the session cookie regardless of being logged in or not.

### Using these utilities

**Add the following to your requirements.txt**

```
lraudit==0.1.1
```

### Push new versions to PYPI public repository

Note this code is currently hosted on PYPI. The LR may want to run their own PYPI repo in LR envs and host this and other LR packages there. An easy way to do this is use [localshop](https://github.com/mvantellingen/localshop).

The travis build will push tagged versions of this package to pypy (currently using my account - this should be transferred to an LR dev/webops person, or as mentioned above pushed to your own pypi)

##### When you want to push a new version

* Set version number in setup.py
```
git tag [version number] -m "update version"
git push --tags origin master
```

