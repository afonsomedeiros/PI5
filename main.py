import bottle
from api import create_app as mount_api
from app import create_app as mount_app
from CONST import ROOT_PATH


core = mount_app()

core.mount("/api/", mount_api())

bottle.TEMPLATE_PATH.insert(0, f"{ROOT_PATH}/app/views/")

core.run(debug=True, reloader=True)
#application = core