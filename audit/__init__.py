from flask import request_started, request, session, json


TEMPLATE = 'Audit: user=[%s], request=[%s], session=[%s], ip_address=[%s], request_url=[%s], params=[%s]'

class Audit(object):

    def __init__(self, app):
        try:
            # check if the client has Flask-Login
            from flask.ext.login import current_user
            request_started.connect(audit_user, app)
        except:
            request_started.connect(audit_anon, app)


def audit_user(sender, **extra):
    from flask.ext.login import current_user
    id = current_user.get_id()
    ip_addr = request.remote_addr
    request_url = request.url
    params = json.dumps(request.form)

    if id:
        log(sender, current_user, request, session, ip_addr, request_url, params)
    else:
        log(sender, 'anon', request, session, ip_addr, request_url, params)


def audit_anon(sender, **extra):
    log(sender, 'anon', request, session, ip_addr, request_url, params)


def log(sender, who, request, session, ip_addr, request_url, params):
    sender.logger.info(TEMPLATE % (who, request, session, ip_addr, request_url, params))