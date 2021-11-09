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
from typing import List

from fastapi import FastAPI
from uvicorn import run

from src.routers import processes


def create_app() -> FastAPI:
    """
    Create the application.

    Returns:
        FastAPI: The application.
    """
    app = FastAPI(
        title='Absolute Control',
        description='A fast, simple, and secure rest-based process manager.',
        version='0.0.1'
    )

    app.include_router(processes.router)

    return app

def main(argc: int, argv: List[str]):
    """
    Main entry point for the program.

    Args:
        argc (int): The number of arguments passed to the program.
        argv (List[str]): The list of arguments passed to the program.
    """    
    run(create_app, host='0.0.0.0', port=8000)
