"""
app root of the api endpoints
"""

from flask import Flask

import api.config.config
from api.view.routes import Urls


class Server:
    """Create flask object to start the server"""

    @staticmethod
    def create_app(config=None):
        """
        Method create a flask object
        :param config: None
        :return: app
        """
        app = Flask(__name__)
        app.config.update(config.__dict__ or {})
        Urls.generate(app)
        return app


APP = Server().create_app(config=api.config.config.DevelopmentConfig)


if __name__ == '__main__':
    APP.run()
