# Copyright 2017 Google Inc. All Rights Reserved.
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
"""The command group for keys."""

from __future__ import absolute_import
from __future__ import unicode_literals
from googlecloudsdk.api_lib.cloudkms import base as cloudkms_base
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.kms import flags
from googlecloudsdk.core import resources


class Keys(base.Group):
  """Create and manage keys.

  A key represents a logical key that can be used for cryptographic
  operations.
  """

  @classmethod
  def Args(cls, parser):
    if cls.ReleaseTrack() != base.ReleaseTrack.ALPHA:
      # These flags are automatically added in declarative commands and
      # currently all declarative commands are ALPHA.
      flags.AddKeyRingFlag(parser)
      flags.AddLocationFlag(parser)
    parser.display_info.AddUriFunc(
        cloudkms_base.MakeGetUriFunc(flags.CRYPTO_KEY_COLLECTION))