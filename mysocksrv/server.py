import socket
import threading

class client_thread():


    def __init__(self, socket, address):
        self._socket = socket
        self._address = address
        self._thread = threading.Thread()

    def _process(socket, address):
        print(f'Client thread for CXN from {address} starting')
        
        #TODO: store recieved data in a thread-safe datastore


