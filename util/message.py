import logging


def initialize():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s  - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )


def error_conn(db_properties):
    msg = 'Failed to connect to: {hostname}:{port}, {db}'.format(
        hostname=db_properties.hostname,
        port=db_properties.port,
        db=db_properties.db
    )
    initialize()
    logging.warning(msg)


def warning_no_schema(db_properties, schema):
    msg = 'Warning no schema [{schema}] at {hostname}:{port}, {db}'.format(
        schema=schema,
        hostname=db_properties.hostname,
        port=db_properties.port,
        db=db_properties.db
    )
    initialize()
    logging.warning(msg)


def info_start():
    initialize()
    logging.info('Preparing to migrate.....')


def info_database_connected():
    initialize()

    logging.info('Connected to all database successfully.')
    logging.info('Starting to migrate......')


def info_migrated_completed():
    initialize()

    logging.info('Migrated database successfully. :)')