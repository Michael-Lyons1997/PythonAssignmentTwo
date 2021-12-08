import platform

where = platform.uname().release.find("aws")

if where == -1:
    # Local.
    config = {
        "host": "127.0.0.1",
        "database": "visitorsDB",
        "user": "visitor",
        "password": "visitorpasswd",
    }
else:
    # Not on PA.
    config = {
        "host": "C00217557.mysql.pythonanywhere-services.com",
        "database": "C00217557$default",
        "user": "C00217557",
        "password": "mysqlpassword",
    }
