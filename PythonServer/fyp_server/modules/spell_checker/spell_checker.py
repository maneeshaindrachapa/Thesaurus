import requests
import modules.display_error.display_error as display_error

api_url = 'http://helabasa.projects.uom.lk/morphy/foma/spellCheck?word='

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"}


# main method for checkWord
def checkWord(input_word):
    # Api call
    response = requests.get(api_url + input_word, headers=header)
    try:

        response_data = response.json()['response_data']

        response_format = [input_word, response_data[0][2]]

        # 0 for wrong word 1 for correct word
        return 200, response_format
    except IndexError:
        display_error.print_error(404, "Error with spell checker")
        return 404, "Error with spell checker"
    except TypeError:
        display_error.print_error(404, "Error with spell checker")
        return 404, "Error with spell checker"
    except ConnectionError:
        display_error.print_error(404, "Error connection to URL")
        return 404, "Error connection to URL"


# print(checkWord('පුරාන'))