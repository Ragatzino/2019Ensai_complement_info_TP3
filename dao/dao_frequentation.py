import connection


class DaoFrequentation:
    def create(self, frequentation):
        connexion = connection.get_connection()
        with connexion.cursor() as cur:
            try:
                cur.execute(
                    "insert into frequentation(zone, total_entree) values (%s,%s)", (frequentation.zone, frequentation.total_entree))
                connexion.commit()
            except ValueError as e:
                connexion.rollback()
            finally:
                connexion.close()
