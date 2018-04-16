import pytest
from multiprocessing import Process
from threading import Thread
import server

@pytest.fixture(scope='module', autouse=True)
def server_setup():
    instance = server.create_server()
    process = Process(target=instance.serve_forever)

    yield process.start()
    process.terminate()