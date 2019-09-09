class Frequentation:

    def __init__(self, zone, total_entree):
        self.zone = zone
        self.total_entree = total_entree

    def __str__(self):
        return '(zone=%s, total_entree=%s)' % (self.zone, self.total_entree)

    def __repr__(self):
        return '(zone=%s, total_entree=%s)' % (self.zone, self.total_entree)
