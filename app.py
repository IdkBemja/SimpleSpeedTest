from flask_app import app

from flask_app.controllers import url_controller
from flask_app.utils import perform_speedtest


if __name__ == "__main__":
    app.run(host='0.0.0.0')
