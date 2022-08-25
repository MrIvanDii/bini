import psycopg2
import configure
from configure import *

def get_name_and_episodes(value):

    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=configure.host,
            user=configure.user,
            password=configure.password,
            database=configure.dbname
        )
        connection.autocommit = True

        postgreSQL_select_Query = f'SELECT name, num_of_episods FROM characters WHERE num_of_episods BETWEEN {value} AND 100 ORDER BY num_of_episods DESC LIMIT 10'

        with connection.cursor() as cursor:

            cursor.execute(postgreSQL_select_Query)
            character_records = cursor.fetchall()

            for i in character_records:
                print(f'Name: {i[0]}, Number of episodes: {i[1]}')

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

def get_name_of_episodes_by_char_id(value):

    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=configure.host,
            user=configure.user,
            password=configure.password,
            database=configure.dbname
        )
        connection.autocommit = True

        postgreSQL_select_Query = f'SELECT name_of_episods FROM characters WHERE id = {value}'

        with connection.cursor() as cursor:

            cursor.execute(postgreSQL_select_Query)
            episodes_records = cursor.fetchall()
            list_of_epi_names = episodes_records[0][0].replace('{', '').replace('}', '').replace('"', '').split(',')

            if len(list_of_epi_names) > 10:
                for episode_name in list_of_epi_names[0:11]:
                    print(episode_name.strip())
            else:
                for episode_name in list_of_epi_names:
                    print(episode_name.strip())


    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")


if __name__ == '__main__':
    value = input('Pleas, input your value from 1 to 100: ')
    type = input('Pleas, input the type - "characters" or "episodes": ')

    if type == 'characters':
        get_name_and_episodes(value)
    else:
        get_name_of_episodes_by_char_id(value)
