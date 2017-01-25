# Copyright 2017 Cloudbase Solutions Srl
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Config options available for the Azure metadata service."""

from oslo_config import cfg

from cloudbaseinit.conf import base as conf_base


class AzureOptions(conf_base.Options):

    """Config options available for the Azure metadata service."""

    def __init__(self, config):
        super(AzureOptions, self).__init__(config, group="azure")
        self._options = [
            cfg.StrOpt(
                "transport_cert_store_name",
                default="Windows Azure Environment",
                help="Certificate store name for transport certificates"),
        ]

    def register(self):
        """Register the current options to the global ConfigOpts object."""
        group = cfg.OptGroup(self.group_name, title='Azure Options')
        self._config.register_group(group)
        self._config.register_opts(self._options, group=group)

    def list(self):
        """Return a list which contains all the available options."""
        return self._options
