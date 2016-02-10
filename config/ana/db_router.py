

class AnaDBRouter(object):

    def db_for_read(self, model, **hints):
        """
        Attempts to read ana models go to ana_db.
        """
        if model._meta.app_label == 'ana':
            return 'ana_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write ana models go to ana_db.
        """
        if model._meta.app_label == 'ana':
            return 'ana_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the ana app is involved.
        """
        if obj1._meta.app_label == 'ana' or obj2._meta.app_label == 'ana':
            return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the ana app only appears in the 'ana_db'
        database.
        """
        if app_label == 'ana':
            return db == 'ana_db'
        return None
