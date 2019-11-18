from datetime import datetime
import env_data


def print_error(error_code: object, description: object) -> object:
    timestamp = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    error = env_data.DOMAIN + " - - [" + str(timestamp) + "] \"EXCEPTION " + str(description) + "\" " + str(error_code)
    print(error)
