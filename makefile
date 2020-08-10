default: rewrite

rewrite:
	@sed -i 's/import hrpc_pb2 as hrpc__pb2/from . import hrpc_pb2 as hrpc__pb2/g' hyperspace_rpc/*.py && \
	sed -i 's/import schema_pb2 as schema__pb2/from . import schema_pb2 as schema__pb2/g' hyperspace_rpc/*.py

.PHONY: rewrite
