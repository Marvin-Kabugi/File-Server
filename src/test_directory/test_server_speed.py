import os
import time
import pytest
import threading

from ..search import SearchAlgorithms
from ..helper_functions import load_test_file, measure_execution_time
from ..server import main
from ..client import Client
from ..file import FileReader

    
REREAD_ON_QUERY = False


@pytest.mark.parametrize(
    "filename,port",
    [
        ('10000.txt', 65411),
        ('50000.txt', 65445),
        ('150000.txt', 65446),
        ('250000.txt', 65447),
        ('350000.txt', 65448),
        ('500000.txt', 65449),
        ('750000.txt', 65450),
        ('1000000.txt', 65452),
    ]
)
def test_files(filename, port):
    HOST = "127.0.0.1"
    search_algorithm = SearchAlgorithms()
    path, ssl_settings = load_test_file()
    path = os.path.join(path, filename)
    print(path)
    file = FileReader(path, REREAD_ON_QUERY)

    # Start the server in a separate thread
    server = threading.Thread(target=main, args=(path, ssl_settings, search_algorithm, file, measure_execution_time, (HOST, port)))
    server.start()
    # Wait for the server to start
    time.sleep(3)
    # Run the client logic in the main thread
    client = Client(HOST, port)
    sm = client.send_message('4;0;1;28;0;5;3;0;\x00')

    assert sm == "STRING EXISTS\n"

# def test_10000_txt():
#     HOST = "127.0.0.1"
#     PORT = 65440
#     search_algorithm = SearchAlgorithms()
#     path, ssl_settings = load_test_file()
#     path = os.path.join(path, '10000.txt')
#     print(path)
#     file = FileReader(path, REREAD_ON_QUERY)

#     # Start the server in a separate thread
#     server = threading.Thread(target=main, args=(path, ssl_settings, search_algorithm, file, measure_execution_time, (HOST, PORT)))
#     server.start()
#     # Wait for the server to start
#     time.sleep(3)

#     # Run the client logic in the main thread
#     client = Client(HOST, PORT)
#     sm = client.send_message('4;0;1;28;0;5;3;0;\x00')
#     print(sm)
#         # Wait for the server thread to complete

#     assert sm == "STRING EXISTS\n"

# def test_50000_txt():
#     HOST = "127.0.0.1"
#     PORT = 65445
#     search_algorithm = SearchAlgorithms()
#     path, ssl_settings = load_test_file()
#     path = os.path.join(path, '50000.txt')
#     print(path)
#     file = FileReader(path, REREAD_ON_QUERY)

#     # Start the server in a separate thread
#     server = threading.Thread(target=main, args=(path, ssl_settings, search_algorithm, file, measure_execution_time, (HOST, PORT)))
#     server.start()
#     # Wait for the server to start
#     time.sleep(3)

#     # Run the client logic in the main thread
#     client = Client(HOST, PORT)
#     sm = client.send_message('4;0;1;28;0;5;3;0;\x00')
#         # Wait for the server thread to complete

#     assert sm == "STRING EXISTS\n"

# def test_150000_txt():
#     HOST = "127.0.0.1"
#     PORT = 65446
#     search_algorithm = SearchAlgorithms()
#     path, ssl_settings = load_test_file()
#     path = os.path.join(path, '150000.txt')
#     print(path)
#     file = FileReader(path, REREAD_ON_QUERY)

#     # Start the server in a separate thread
#     server = threading.Thread(target=main, args=(path, ssl_settings, search_algorithm, file, measure_execution_time, (HOST, PORT)))
#     server.start()
#     # Wait for the server to start
#     time.sleep(3)

#     # Run the client logic in the main thread
#     client = Client(HOST, PORT)
#     sm = client.send_message('4;0;1;28;0;5;3;0;\x00')
#         # Wait for the server thread to complete

#     assert sm == "STRING EXISTS\n"


# def test_250000_txt():
#     HOST = "127.0.0.1"
#     PORT = 65447
#     search_algorithm = SearchAlgorithms()
#     path, ssl_settings = load_test_file()
#     path = os.path.join(path, '250000.txt')
#     print(path)
#     file = FileReader(path, REREAD_ON_QUERY)

#     # Start the server in a separate thread
#     server = threading.Thread(target=main, args=(path, ssl_settings, search_algorithm, file, measure_execution_time, (HOST, PORT)))
#     server.start()
#     # Wait for the server to start
#     time.sleep(3)

#     # Run the client logic in the main thread
#     client = Client(HOST, PORT)
#     sm = client.send_message('4;0;1;28;0;5;3;0;\x00')
#         # Wait for the server thread to complete

#     assert sm == "STRING EXISTS\n"


# def test_350000_txt():
#     HOST = "127.0.0.1"
#     PORT = 65448
#     search_algorithm = SearchAlgorithms()
#     path, ssl_settings = load_test_file()
#     path = os.path.join(path, '350000.txt')
#     print(path)
#     file = FileReader(path, REREAD_ON_QUERY)

#     # Start the server in a separate thread
#     server = threading.Thread(target=main, args=(path, ssl_settings, search_algorithm, file, measure_execution_time, (HOST, PORT)))
#     server.start()
#     # Wait for the server to start
#     time.sleep(3)

#     # Run the client logic in the main thread
#     client = Client(HOST, PORT)
#     sm = client.send_message('4;0;1;28;0;5;3;0;\x00')
#         # Wait for the server thread to complete

#     assert sm == "STRING EXISTS\n"


# def test_500000_txt():
#     HOST = "127.0.0.1"
#     PORT = 65449
#     search_algorithm = SearchAlgorithms()
#     path, ssl_settings = load_test_file()
#     path = os.path.join(path, '500000.txt')
#     print(path)
#     file = FileReader(path, REREAD_ON_QUERY)

#     # Start the server in a separate thread
#     server = threading.Thread(target=main, args=(path, ssl_settings, search_algorithm, file, measure_execution_time, (HOST, PORT)))
#     server.start()
#     # Wait for the server to start
#     time.sleep(3)

#     # Run the client logic in the main thread
#     client = Client(HOST, PORT)
#     sm = client.send_message('4;0;1;28;0;5;3;0;\x00')
#         # Wait for the server thread to complete

#     assert sm == "STRING EXISTS\n"


# def test_750000_txt():
#     HOST = "127.0.0.1"
#     PORT = 65450
#     search_algorithm = SearchAlgorithms()
#     path, ssl_settings = load_test_file()
#     path = os.path.join(path, '750000.txt')
#     print(path)
#     file = FileReader(path, REREAD_ON_QUERY)

#     # Start the server in a separate thread
#     server = threading.Thread(target=main, args=(path, ssl_settings, search_algorithm, file, measure_execution_time, (HOST, PORT)))
#     server.start()
#     # Wait for the server to start
#     time.sleep(3)

#     # Run the client logic in the main thread
#     client = Client(HOST, PORT)
#     sm = client.send_message('4;0;1;28;0;5;3;0;\x00')
#         # Wait for the server thread to complete

#     assert sm == "STRING EXISTS\n"


# def test_1000000_txt():
#     HOST = "127.0.0.1"
#     PORT = 65452
#     search_algorithm = SearchAlgorithms()
#     path, ssl_settings = load_test_file()
#     path = os.path.join(path, '1000000.txt')
#     print(path)
#     file = FileReader(path, REREAD_ON_QUERY)

#     # Start the server in a separate thread
#     server = threading.Thread(target=main, args=(path, ssl_settings, search_algorithm, file, measure_execution_time, (HOST, PORT)))
#     server.start()
#     # Wait for the server to start
#     time.sleep(3)

#     # Run the client logic in the main thread
#     client = Client(HOST, PORT)
#     sm = client.send_message('4;0;1;28;0;5;3;0;\x00')
#         # Wait for the server thread to complete

#     assert sm == "STRING EXISTS\n"


