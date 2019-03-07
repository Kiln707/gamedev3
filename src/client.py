from engine.application import Application

class Game(Application):
    pass

if __name__ == '__main__':
    app = Game.create_application()
    app.run()
