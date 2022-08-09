import psycopg2
from configure import host, dbname, user, password

host = host
dbname = dbname
user = user
password = password

value = input('Pleas, input your value from 1 to 100: ')
type = input('Pleas, input the type - "characters" or "episodes": ')

if 1 <= int(value) < 101 and type == 'characters' or type == 'episodes':
    if type == 'characters':
        # Construct connection string
        try:
            # connect to exist database
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=dbname
            )

            connection.autocommit = True

            postgreSQL_select_Query = """select * from characters where num_of_episods BETWEEN 5 and 100 ORDER BY num_of_episods DESC"""

            with connection.cursor() as cursor:

                cursor.execute(postgreSQL_select_Query)
                character_records = cursor.fetchall()

                if len(character_records) > 10:
                    i = 0
                    for row in character_records:
                        if i == 10:
                            break
                        else:
                            print(f'Name: {row[1]}, Number of episodes: {row[8]}')
                            i += 1


        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")


    if type == 'episodes':

        try:
            # connect to exist database
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=dbname
            )

            connection.autocommit = True

            postgreSQL_select_Query = f"""select * from characters where id = {value}"""

            with connection.cursor() as cursor:

                cursor.execute(postgreSQL_select_Query)

                character_records = cursor.fetchall()
                data_epi_names = character_records[0][9]
                clear_data_epi_name = data_epi_names.replace('{', '').replace('}', '').replace('"', '').split(',')

                if len(clear_data_epi_name) > 10:
                    for episode_name in clear_data_epi_name[0:11]:
                        print(episode_name.strip())
                else:
                    for episode_name in clear_data_epi_name:
                        print(episode_name.strip())

        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")

else:
    print('Not correct data input')
    print('Pleas try again')