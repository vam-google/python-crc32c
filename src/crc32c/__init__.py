# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# NOTE: ``__config__`` **must** be the first import because it (may)
#       modify the search path used to locate shared libraries.
import crc32c.__config__
import crc32c._crc32c_cffi


def extend(*args, **kwargs):
    return crc32c._crc32c_cffi.lib.crc32c_extend(*args, **kwargs)


def value(*args, **kwargs):
    return crc32c._crc32c_cffi.lib.crc32c_value(*args, **kwargs)
