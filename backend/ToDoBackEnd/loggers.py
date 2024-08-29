def get_my_logger():
    import logging
    from logging.handlers import RotatingFileHandler
    import os

    current = os.path.abspath(os.path.abspath(__file__))
    my_logger = logging.getLogger("DATABASE LOGGER")
    my_logger.setLevel(logging.DEBUG)

    script = os.path.dirname(os.path.abspath(__file__))
    log_folder = os.path.join(script, 'database_logs')

    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    filename = f"database_log.log"
    location = os.path.join(log_folder, filename)
    file_path = os.path.join(current, location)

    my_handler = RotatingFileHandler(file_path, maxBytes=1024 * 1024, backupCount=5)
    my_handler.setLevel(logging.DEBUG)
    my_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    my_logger.addHandler(my_handler)

    return my_logger
