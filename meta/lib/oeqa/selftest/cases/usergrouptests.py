#
# Copyright OpenEmbedded Contributors
#
# SPDX-License-Identifier: MIT
#

from oeqa.selftest.case import OESelftestTestCase
from oeqa.utils.commands import bitbake

class UserGroupTests(OESelftestTestCase):
    def test_group_from_dep_package(self):
        self.logger.info("Building creategroup2")
        bitbake(' creategroup2 creategroup1')
        bitbake(' creategroup2 creategroup1 -c clean')
        self.logger.info("Packaging creategroup2")
        self.assertTrue(bitbake(' creategroup2 -c package'))

    def _test_add_task_between_p_sysroot_and_package(self):
        self.logger.info("Cleaning sstate for useraddbadtask")
        self.logger.info("Building useraddbadtask")
        # fails due to bug #14961
        self.assertTrue(bitbake(' useraddbadtask -C fetch'))
