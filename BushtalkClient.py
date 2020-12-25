import PySimpleGUI as sg
from SimConnect import *
import requests
import logging
import sys

# Authentication Constants
DEV_MODE = False
URL_PREFIX = None
JWT_TOKEN = None
USER_ID = None
AUTH_STATUS = 'NOT LOGGED IN'
if DEV_MODE:
    URL_PREFIX = "http://localhost:8080"
else:
    URL_PREFIX = "https://bushtalkradio.com"

# SimConnect Constants
SIMCONNECT = None
SIMCONNECT_STATUS = 'OFF'
SIMCONNECT_REFRESH_RATE = 1000

sg.theme('Reddit')
LOGO = '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' \
       'VqaJRl/weabQMLOHQ7twAAAABJRU5ErkJggg=='


def login(_username, _password):
    """
    Log in to BUSHtalk Radio
    """
    global JWT_TOKEN
    global AUTH_STATUS
    global USER_ID

    try:

        logging.info("Logging in with username={} and password={}".format(_username, _password))

        login_response = requests.post(URL_PREFIX + '/api/authenticate', json={
            "password": _password,
            "username": _username})
        if login_response.status_code == 200:
            JWT_TOKEN = login_response.json()['id_token']
            USER_ID = login_response.json()['userId']
            AUTH_STATUS = 'LOGGED IN'
            logging.info("User {} obtained JWT token {}".format(_username, JWT_TOKEN))

        if login_response.status_code == 401:
            sg.Popup('Wrong password. Please try again.')
            logging.error('Password and username did not match')
            AUTH_STATUS = 'BAD CREDENTIALS'

    except Exception as e:
        logging.error("Could not reach server!")
        sg.Popup('There was a problem reaching the our servers!')


def init_simconnect():
    """
        Initialise SimConnect connection to MSFS2020
    """
    global SIMCONNECT
    global SIMCONNECT_STATUS
    try:
        SIMCONNECT = SimConnect()
        SIMCONNECT_STATUS = 'ON'
    except BaseException as e:
        SIMCONNECT_STATUS = 'OFF'
        logging.error("Could not connect to MSFS2020 {}".format(e))


def init_context():
    """
        First request we only send the username,
        the response will tell use what data to query
    """
    global SIMCONNECT_REFRESH_RATE
    request = {
        "USER_ID": USER_ID
    }
    init_context_response = requests.post(URL_PREFIX + "/api/track",
                                          json=request,
                                          headers={"Authorization": "Bearer " + JWT_TOKEN})
    response_json = init_context_response.json()
    SIMCONNECT_REFRESH_RATE = response_json['refresh_rate'] * 1000
    return response_json


def query_simconnect(data_to_query_keys, simconnect_data, simconnect_events):
    """
        Queries simconnect every few seconds
    """
    global SIMCONNECT_STATUS
    data_to_return = {
        "USER_ID": USER_ID
    }
    for key in data_to_query_keys['data_request']:
        try:
            var = simconnect_data.get(key)

            if type(var) is bytes:
                data = str(var, "utf-8")
                data_to_return[key] = data
            else:
                data_to_return[key] = var

        except Exception:
            logging.error("Could not get data by key {}".format(key))
            pass

    response = requests.post(URL_PREFIX + "/api/track",
                             json=data_to_return,
                             headers={"Authorization": "Bearer " + JWT_TOKEN})

    if response.status_code == 200:
        logging.info("SimConnect data successfully updated")
        # update query keys
        new_keys = response.json()
    else:
        logging.error("Could not send location data to SimConnect")
        SIMCONNECT_STATUS = 'ERROR'

    return new_keys


"""
APPLICATION START
"""
init_simconnect()

login_layout = [
    [sg.Image(data=LOGO)],
    [sg.Text('Username:', size=(8, 1), font=['Roboto', 10]), sg.Input(key='username', size=(25, 1))],
    [sg.Text('Password:', size=(8, 1), font=['Roboto', 10]), sg.Input(key='password', password_char='*', size=(25, 1))],
    # [sg.Text('SimConnect: ' + SIMCONNECT_STATUS, size=(13, 1), key='output_simconnect', font=['Roboto', 8]),
    #             sg.Text('BUSHtalk: ' + AUTH_STATUS, size=(13, 1), key='output_auth', font=['Roboto', 8])],
    [sg.Button('Log in'), sg.Button('Exit')],
    [sg.Text('This client is powered by Python-SimConnect', font=['Roboto', 8], text_color='grey')]
]

logged_in_layout = [
    [sg.Image(data=LOGO)],
    [sg.Text('You are logged in!', size=(15, 1), font=['Roboto', 12], text_color='blue')],
    [sg.Text(key='game_status', size=(23, 1), font=['Roboto', 12], text_color='blue')],
    [sg.Button('Log out')]
]

layout = [[sg.Column(login_layout, key='login-layout', element_justification='c'),
           sg.Column(logged_in_layout, key='logged-in-layout', element_justification='c', visible=False)]]

window = sg.Window('Bushtalk Client 1.0.2', layout, element_justification='c', icon=r'favicon.ico')

while True:
    event, values = window.read(timeout=SIMCONNECT_REFRESH_RATE)

    if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Log out':
        break

    if SIMCONNECT_STATUS == 'ON':
        window[f'game_status'].update('Flight Simulator: Running')
    else:
        window[f'game_status'].update('Flight Simulator: Not Running')

    if event == 'Log in':
        login(values['username'], values['password'])
        if AUTH_STATUS == 'LOGGED IN':
            init_simconnect()
            data_to_query_keys = init_context()
            simconnect_data = AircraftRequests(SIMCONNECT)
            simconnect_events = AircraftEvents(SIMCONNECT)
            window[f'login-layout'].update(visible=False)
            window[f'logged-in-layout'].update(visible=True)

    if AUTH_STATUS == 'LOGGED IN' and SIMCONNECT_STATUS == 'ON':
        query_simconnect(data_to_query_keys, simconnect_data, simconnect_events)

    # if logged in but simconnect isn't running, try to connect to simconnect every refresh
    if AUTH_STATUS == 'LOGGED IN' and SIMCONNECT_STATUS != 'ON':
        init_simconnect()
        if SIMCONNECT_STATUS == 'ON':
            data_to_query_keys = init_context()
            simconnect_data = AircraftRequests(SIMCONNECT)
            simconnect_events = AircraftEvents(SIMCONNECT)

window.close()
sys.exit()
