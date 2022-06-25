from typing import List

import psycopg2

from counter.domain.models import ObjectCount
from counter.domain.ports import ObjectCountRepo


class CountInMemoryRepo(ObjectCountRepo):

    def __init__(self):
        self.store = dict()

    def read_values(self, object_classes: List[str] = None) -> List[ObjectCount]:
        if object_classes is None:
            return list(self.store.values())

        return [self.store.get(object_class) for object_class in object_classes]

    def update_values(self, new_values: List[ObjectCount]):
        for new_object_count in new_values:
            key = new_object_count.object_class
            try:
                stored_object_count = self.store[key]
                self.store[key] = ObjectCount(key, stored_object_count.count + new_object_count.count)
            except KeyError:
                self.store[key] = ObjectCount(key, new_object_count.count)


class CountPostgresRepo(ObjectCountRepo):

    def __init__(self, host, port, database, user, password):
        self.connection = psycopg2.connect(f"dbname='{database}' user='{user}' host='{host}' port='{port}' password='{password}'")

    def read_values(self, object_classes: List[str] = None) -> List[ObjectCount]:
        cur = self.connection.cursor()
        cur.execute("SELECT object_class, observed_count FROM item_count")
        results = cur.fetchall()
        return [ObjectCount(r[0],r[1]) for r in results]

    def update_values(self, new_values: List[ObjectCount]):
        cur = self.connection.cursor()
        for new_value in new_values:
            cur.execute(f"INSERT INTO item_count (object_class, observed_count)"
                        f" values('{new_value.object_class}', {new_value.count}) "
                        f"ON CONFLICT (object_class) DO "
                        f"UPDATE SET observed_count = item_count.observed_count + excluded.observed_count;")
            self.connection.commit()