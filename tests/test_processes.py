# Copyright (c) 2021 Johnathan P. Irvin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from time import sleep

from fastapi.testclient import TestClient
from pytest import fixture
from src import create_app


@fixture
def client() -> TestClient:
    """
    Fixture to create a test client.

    Returns:
        TestClient: Test client.
    """
    return TestClient(create_app())

def test_processes_get(client: TestClient):
    """
    Test to ensure the processes endpoint returns a 200.

    Args:
        client (TestClient): Test client.
    """
    response = client.get('/processes')

    assert response.status_code == 200

def test_processes_get_with_name(client: TestClient):
    """
    Test to ensure the processes endpoint returns a 200.
    Test also ensures the correct process is returned.

    Args:
        client (TestClient): Test client.
    """
    response = client.get('/processes?name=python3')

    assert response.status_code == 200
    assert b'"name":"python3"' in response.content 

def test_processes_get_with_name_and_pid(client: TestClient):
    """
    Test to ensure the processes endpoint returns a 200.
    Test also ensures the correct process is returned.

    Args:
        client (TestClient): Test client.
    """
    response = client.get('/processes?name=python3')

    assert response.status_code == 200
    assert b'"name":"python3"' in response.content 
    
    # Use a regular expression to the get the pid.
    pid = response.json()[0]['pid']
    response = client.get(f'/processes/{pid}')

    assert response.status_code == 200
    assert b'"name":"python3"' in response.content

    second_pid = response.json()['pid']
    assert pid == second_pid

def test_process_start_and_kill_pid(client: TestClient):
    """
    Test that a new process can be started and killed.

    Args:
        client (TestClient): Test client.
    """
    response = client.post('/processes/start?command=python3', allow_redirects=True)
    assert response.status_code == 200
    pid = response.json()['pid']

    response = client.delete(f'/processes/{pid}')
    
    assert response.status_code == 200

    response = client.get(f'/processes/{pid}')
    assert response.json()['status'] == 'zombie'

def test_process_and_kill_name(client: TestClient):
    """
    Test that a new process can be started and killed.

    Args:
        client (TestClient): Test client.
    """
    response = client.post('/processes/start?command=python3', allow_redirects=True)
    assert response.status_code == 200
    pid = response.json()['pid']

    response = client.delete('/processes?name=python3', allow_redirects=True)
    
    assert response.status_code == 200

    response = client.get(f'/processes/{pid}')
    assert response.json()['status'] == 'zombie'

def test_kill_all_processes(client: TestClient):
    """
    Test that all processes can be killed

    Args:
        client (TestClient): Test client.
    """
    response = client.post('/processes/start?command=python3', allow_redirects=True)
    assert response.status_code == 200
    pid = response.json()['pid']

    response = client.delete('/processes', allow_redirects=True)
    
    assert response.status_code == 200

    response = client.get(f'/processes/{pid}')
    assert response.json()['status'] == 'zombie'