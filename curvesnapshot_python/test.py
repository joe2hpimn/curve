#
#  Copyright (c) 2020 NetEase Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

#!/usr/bin/env python
# coding=utf-8


import curvesnapshot

ret = curvesnapshot.Init("./client.conf");
print ret

user = curvesnapshot.CUserInfo_t()
user.owner = "gt"

seq = curvesnapshot.type_uInt64_t()

filestatus = curvesnapshot.type_uInt32_t()
curvesnapshot.CheckSnapShotStatus("/test", user, seq, filestatus)
print filestatus.value

ret = curvesnapshot.CreateSnapShot("/test", user, seq)
print ret

seq.value = 1
ret = curvesnapshot.DeleteSnapShot("/test", user, seq)
print ret

finfo = curvesnapshot.CFInfo_t()
ret = curvesnapshot.GetSnapShot("/test", user, seq, finfo)
print ret
print finfo.owner
print finfo.filename

offset = curvesnapshot.type_uInt64_t()
offset.value = 0
seq.value = 0
seginfo = curvesnapshot.CSegmentInfo_t();
ret = curvesnapshot.GetSnapshotSegmentInfo("/test", user, seq, offset, seginfo)
print ret
print seginfo.chunksize.value
print seginfo.chunkVecSize.value
for i in range(0, seginfo.chunkVecSize.value):
    print seginfo.chunkvec[i].lpid_.value
    print seginfo.chunkvec[i].cpid_.value
    print seginfo.chunkvec[i].cid_.value

idinfo = curvesnapshot.CChunkIDInfo_t()
idinfo.cid_.value = 1
idinfo.lpid_.value = 10000
idinfo.cpid_.value = 1

offset = curvesnapshot.type_uInt64_t()
len = curvesnapshot.type_uInt64_t()
offset.value = 0
len.value = 8*1024
buf = "tttttttt"*1024
ret = curvesnapshot.ReadChunkSnapshot(idinfo, seq, offset, len, buf)
print ret
print buf[0]
