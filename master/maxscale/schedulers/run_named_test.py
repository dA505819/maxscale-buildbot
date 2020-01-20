from buildbot.plugins import schedulers
from maxscale.config import constants
from . import common
from . import properties

RUN_TEST_PROPERTIES = [
    properties.build_name(),
    properties.build_target(),
    properties.build_box(),
    properties.backend_database(),
    properties.database_version(),
    properties.keep_virtual_machines(),
    properties.test_name(),
    properties.ci_url(),
    properties.smoke_tests(),
    properties.big_number_of_vms(),
    properties.backend_use_ssl(),
    properties.use_snapshots(),
    properties.do_not_revert_virtual_machines(),
    properties.test_template(),
    properties.configuration_to_clone(),
    properties.host(),
]

TRIGGERABLE_SCHEDULER = schedulers.Triggerable(
    name="run_named_test",
    builderNames=["run_named_test"],
    codebases=constants.MAXSCALE_CODEBASE,
)

MANUAL_SCHEDULER = schedulers.ForceScheduler(
    name="run_named_test_force",
    buttonName="Run tests",
    builderNames=["run_named_test"],
    codebases=properties.codebaseParameter(),
    properties=RUN_TEST_PROPERTIES
)

SCHEDULERS = [TRIGGERABLE_SCHEDULER, MANUAL_SCHEDULER]