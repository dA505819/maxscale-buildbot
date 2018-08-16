from maxscale.builders import MAXSCALE_BUILDERS
from maxscale.config import environment
from maxscale.schedulers import MAXSCALE_SCHEDULERS
from maxscale.services import MAXSCALE_SERVICES
from maxscale.auth import MAXSCALE_AUTH
from maxscale.change_source import MAXSCALE_POLLERS
from maxscale import workers

# This is the dictionary that the buildmaster pays attention to. We also use
# a shorter alias to save typing.
c = BuildmasterConfig = {}

# WORKERS

c['workers'] = workers.workerConfiguration()
c['protocols'] = {'pb': {'port': 9989}}

# CHANGESOURCES

if not environment.is_development():
    c['change_source'] = MAXSCALE_POLLERS

# SCHEDULERS

c['schedulers'] = MAXSCALE_SCHEDULERS

# BUILDERS

c['builders'] = MAXSCALE_BUILDERS

# BUILDBOT SERVICES

c['services'] = MAXSCALE_SERVICES

# PROJECT IDENTITY

c['title'] = "MaxScale CI"
c['titleURL'] = "https://github.com/mariadb-corporation/maxscale-buildbot"
c['buildbotURL'] = "https://maxscale-ci.mariadb.com/"
if environment.is_development():
    c['buildbotURL'] = "http://localhost:8010/"

# Web intefrace configuration
c['www'] = dict(
    port="tcp:8010:interface=127.0.0.1",
    plugins=dict(waterfall_view={}, console_view={}, grid_view={}),
)
# Do not enable authentication or authorization during the development
if not environment.is_development():
    c['www'].update(dict(
        auth=MAXSCALE_AUTH['auth'],
        authz=MAXSCALE_AUTH['authz']))

# DB URL

c['db'] = {
    'db_url': "sqlite:///state.sqlite",
}

# Configure privacy settings, http://docs.buildbot.net/latest/manual/cfg-global.html#buildbotnetusagedata
c['buildbotNetUsageData'] = 'basic'
