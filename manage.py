from app import create_app ,dp 
from app.models import user 

@manager.shell


def make_shell_context():
    return dict(app= app , db = db ,User = User)


if __name__ == '__main__':
    manager.run()