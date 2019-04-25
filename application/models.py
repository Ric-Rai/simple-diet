from application import db, app


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def to_cache(cls, obj):
        try:
            for o in obj:
                cls.cache[o.id] = o
        except:
            cls.cache[obj.id] = obj

    @classmethod
    def from_cache(cls, identity):
        if identity in cls.cache:
            app.logger.info("from cache")
            return cls.cache[identity]
        obj = cls.query.get(identity)
        app.logger.info("to cache")
        cls.cache[obj.id] = obj
        return obj
