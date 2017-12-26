import socket


if socket.gethostname() == 'pharmacosphere':
    from .deploy import *
elif socket.gethostname() == 'vom-nb':
    from .user_radimir import *
elif socket.gethostname() == 'genius-K42Jv':
    from .user_genius import *
else:
    from .develop import *
