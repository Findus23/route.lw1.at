gtfs-realtime.proto:
	curl -O https://raw.githubusercontent.com/google/transit/refs/heads/master/gtfs-realtime/proto/gtfs-realtime.proto

gtfs_realtime_pb2.py gtfs_realtime_pb2.pyi:
	 protoc --python_out=. --pyi_out=. gtfs-realtime.proto
