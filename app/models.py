from . import dp 


class User (dp.model):

    __tablename__ = 'users'
    id = dp.Column(dp.integer,primary_key = True)
    username = db.Column(dp.string(255))


    def __repr__(self):
        return f'User{self.username}'

        