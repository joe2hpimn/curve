#!/bin/sh

home=/curve/deploy/local/chunkserver
#home=.
conf=${home}/conf
log=${home}/log
bin=/curve/bazel-bin/src/chunkserver
#bin=.

${bin}/chunkserver -bthread_concurrency=18 -raft_max_segment_size=8388608 -raft_sync=true -minloglevel=0 -conf=${conf}/chunkserver.conf.2 > ${log}/chunkserver.log.2 2>&1 &