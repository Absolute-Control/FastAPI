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
from typing import List, Optional

from absolute_control import (get_all_processes, get_process_by_id,
                              get_processes_by_name, kill_all_processes,
                              kill_process_by_id, kill_processes_by_name,
                              open_process_using_command)
from fastapi import APIRouter
from src.models import Process

router = APIRouter(
    prefix="/processes",
    responses={
        "200": {"description": "Success"},
        "400": {"description": "Bad Request"},
        "404": {"description": "Not Found"},
    }
)

@router.get("/", response_model=List[Process])
async def get_processes(name: Optional[str] = None) -> List[Process]:
    """
    Get all processes.

    Args:
        name (Optional[str], optional): Filter by process name. Defaults to None.

    Returns:
        List[Process]: A list of processes.
    """
    if name:
        return get_processes_by_name(name)
        
    return get_all_processes()

@router.delete("/")
async def kill_processes(name: Optional[str] = None) -> None:
    """
    Kill all processes.

    Args:
        name (Optional[str], optional): Filter by process name. Defaults to None.
    """
    if name:
        return kill_processes_by_name(name)

    return kill_all_processes()

@router.get("/{id:int}", response_model=Process)
async def process_by_id(id: int) -> Optional[Process]:
    """
    Get a process by id.

    Args:
        id (int): The process id.

    Returns:
        Optional[Process]: The process.
    """
    return get_process_by_id(id)

@router.delete("/{id:int}")
async def kill_by_id(id: int) -> Optional[Process]:
    """
    Kill a process by id.

    Args:
        id (int): The process id.

    Returns:
        Optional[Process]: The process.
    """
    return kill_process_by_id(id)

@router.post("/start", response_model=Process)
async def open_using_command(command: str) -> Optional[Process]:
    """
    Open a process using a command.

    Args:
        command (str): The command to open the process.

    Returns:
        Optional[Process]: The process.
    """
    return open_process_using_command(command)
