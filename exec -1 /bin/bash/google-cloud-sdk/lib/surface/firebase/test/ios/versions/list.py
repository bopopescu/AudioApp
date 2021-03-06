# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The 'gcloud firebase test ios versions list' command."""

from googlecloudsdk.api_lib.firebase.test import util
from googlecloudsdk.calliope import base


@base.ReleaseTracks(base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA)
class List(base.ListCommand):
  """List all iOS versions available for testing."""

  @staticmethod
  def Args(parser):
    """Method called by Calliope to register flags for this command.

    Args:
      parser: An argparse parser used to add arguments that follow this
          command in the CLI. Positional arguments are allowed.
    """
    parser.display_info.AddFormat("""
          table[box](
            id:label=OS_VERSION_ID:align=center,
            major_version:align=center,
            minor_version:align=center,
            tags.list().color(green=default,red=deprecated,yellow=preview)
          )
    """)
    base.URI_FLAG.RemoveFromParser(parser)

  def Run(self, args):
    """Run the 'gcloud firebase test ios versions list' command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation (i.e. group and command arguments combined).

    Returns:
      The list of iOS OS versions we want to have printed later.
    """
    catalog = util.GetIosCatalog(self.context)
    return catalog.versions
