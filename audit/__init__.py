from flask import request_started, session


class Audit(object):

    LOG_TEMPLATE = 'Audit: user=[%s], request=[%s], session=[%s]'

    def __init__(self, app):
        try:
            # check if the client has Flask-Login
            from flask.ext.login import current_user
            request_started.connect(self.audit, app)
        except:
            request_started.connect(self.anon_audit, app)
 
    def anon_audit(sender, **extra):
        sender.logger.info(TEMPLATE % ('anon', request, session))

    def audit(sender, **extra):
        id = current_user.get_id()
        if id:
            sender.logger.info(TEMPLATE % (current_user, request, session))
        else:
            sender.logger.info(TEMPLATE % ('anon', request, session))


       
