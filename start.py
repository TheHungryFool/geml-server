from geml.application import geml

"""Main application 

This is the starting point of the application. Here,
an instance of geml server is created. The server inherits from http.server module 
and serves HTTP requests.
"""

# create an instance of geml server
app = geml()

"""Supported modifications (not mandatory)

-- app.message(str): Displays the message on the console when the server starts
-- app.port: port over which the requests are served 
-- app.host: the address where the app is to be hosted
"""

if __name__ == '__main__':
    # start the app if invoked from the file directly
    app.start()

    # the start method can be called with parameters
    # Example: app.start('localhost', 2520)