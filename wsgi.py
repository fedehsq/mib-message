"""
Message in a Bottle
Web Server Gateway Interface

This file is the entry point for
mib-users-ms microservice.
"""
from mib import create_app
# application instance
app = create_app()
#do_task.delay()

if __name__ == '__main__':
    app.run()
