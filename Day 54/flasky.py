# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
#
# @app.route("/bye")
# def say_bye():
#     return "Bye"
#
#
# # if __name__ = "__main__":
# #     app.run()

import time


def decorator_function(function):
    def wrapper_function():
        function()

    return wrapper_function()


def say_hello():
    time.sleep(2)
    print("Hello")


def say_bye():
    print("Bye")


def say_greeting():
    print("Eat sit")


say_hello()
