import os

from counter.adapters.count_repo import CountInMemoryRepo, CountPostgresRepo
from counter.adapters.object_detector import TFSObjectDetector, FakeObjectDetector
from counter.domain.actions import CountDetectedObjects
from counter.domain.actions import ListDetectedObjects


def dev_count_action() -> CountDetectedObjects:
    return CountDetectedObjects(FakeObjectDetector(), CountInMemoryRepo())


def prod_count_action() -> CountDetectedObjects:
    tfs_host = os.environ.get('TFS_HOST', 'localhost')
    tfs_port = os.environ.get('TFS_PORT', 8501)
    countPostgresDB = get_postgres_db()
    return CountDetectedObjects(TFSObjectDetector(tfs_host, tfs_port, 'rfcn'),
                                countPostgresDB)


def get_count_action() -> CountDetectedObjects:
    env = os.environ.get('ENV', 'dev')
    count_action_fn = f"{env}_count_action"
    return globals()[count_action_fn]()


def dev_list_action() -> ListDetectedObjects:
    return ListDetectedObjects(FakeObjectDetector())


def prod_list_action() -> ListDetectedObjects:
    tfs_host = os.environ.get('TFS_HOST', 'localhost')
    tfs_port = os.environ.get('TFS_PORT', 8501)
    return ListDetectedObjects(TFSObjectDetector(tfs_host, tfs_port, 'rfcn'))


def get_list_action() -> ListDetectedObjects:
    env = os.environ.get('ENV', 'dev')
    count_action_fn = f"{env}_list_action"
    return globals()[count_action_fn]()


def get_postgres_db():
    host = os.environ.get('POSTGRES_HOST', 'localhost')
    port = os.environ.get('POSTGRES_PORT', 5432)
    db = os.environ.get('POSTGRES_DB', 'count_db')
    user = os.environ.get('POSTGRES_USER', 'count_user')
    password = os.environ.get('POSTGRES_PASSWORD', 'notsosecretpassword')

    return CountPostgresRepo(host, port, db, user, password)
