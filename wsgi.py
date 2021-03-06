from service import app, web, loop
from service.db import setup_db
from service.api import api

tabledb, userdb = loop.run_until_complete(setup_db())
api['tabledb'] = tabledb
api['userdb'] = userdb

if __name__ == '__main__':
    web.run_app(app)
