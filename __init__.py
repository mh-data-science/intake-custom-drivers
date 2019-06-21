from intake.source import base
from azure.datalake.store import lib, AzureDLFileSystem


class WritableTextFilesADLSource(base.DataSource):
    """
    A Azure Data Lake source that also implements a "write" method to write
    files to data lake.
    """

    name = 'writableadltext'
    partition_access = True
    version = '0.0.1dev'

    def __init__(self, tenant_id, client_id, client_secret, store_name, metadata=None):
        token = lib.auth(tenant_id=tenant_id,
                         client_id=client_id,
                         client_secret=client_secret)
        self.adl = AzureDLFileSystem(store_name=store_name, token=token)
        super(WritableTextFilesADLSource, self).__init__(
            metadata=metadata
        )

    def write(self, local_path, remote_path):
        print('writing')
        self.adl.put(local_path, remote_path)

    def read(self, path):
        with self.adl.open(path, 'rb') as f:
            data = f.read()
            print(data)

