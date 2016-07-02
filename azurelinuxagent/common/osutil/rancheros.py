#
# Copyright 2014 Microsoft Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Requires Python 2.4+ and Openssl 1.0+
#

import os
import re
import pwd
import shutil
import socket
import array
import struct
import fcntl
import time
import base64
import azurelinuxagent.common.logger as logger
import azurelinuxagent.common.utils.fileutil as fileutil
import azurelinuxagent.common.utils.shellutil as shellutil
import azurelinuxagent.common.utils.textutil as textutil
from azurelinuxagent.common.osutil.default import DefaultOSUtil

class RancherOSUtil(DefaultOSUtil):
    def __init__(self):
        super(RancherOSUtil, self).__init__()

    def is_dhcp_enabled(self):
        return True

    def get_dhcp_pid(self):
        ret= shellutil.run_get_output("pidof dhcpcd")
        return ret[1] if ret[0] == 0 else None

    def restart_if(self, ifname, retries=3, wait=5):
        logger.warn("Skipped restart_if")
        pass
