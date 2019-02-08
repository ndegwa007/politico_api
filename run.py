"""file to run the server"""

import os
from api import create_app

config_name = os.getenv("APP_SETTINGS")
"""Gets the app settings defined in .env file"""

api = create_app(config_name)
"""configuration to be used"""

if __name__ == "__main__":
	api.run()
