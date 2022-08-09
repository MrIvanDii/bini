import config
from config import host, dbname, user, password
import ramapi
import psycopg2
from ramapi import Base
from ramapi import Character
import requests

host = config.host
dbname = config.dbname
user = config.user
password = config.password

#Get_The_Number_Of_Pages
Char_num_pages = ramapi.Character.get_page(1)['info']['pages']  # 42
Loc_num_pages = ramapi.Location.get_all()['info']['pages']  # 7
Epi_num_pages = ramapi.Episode.get_all()['info']['pages']  # 3

#Data_previos
CHARACTERS = 826
LOCATIONS = 126
EPISODES = 51

#Data_up_to_day
CHAR = ramapi.Character.get_all()['info']['count']
LOC = ramapi.Location.get_all()['info']['count']
EPI = ramapi.Episode.get_all()['info']['count']

#Check_data_for_updates
if CHARACTERS == CHAR and LOCATIONS == LOC and EPISODES == EPI:
    print('DATA OK')
else:
    print('[INFO] Update of data. Pleas waite...')

    #Filling_The_Characters_DB
    for num_of_page in range(1, Char_num_pages + 1):
        print(num_of_page)

        #Fill_The_DB
        try:
            #Connect_To_Exist_Database
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=dbname
            )

            connection.autocommit = True

            #Character
            char_page_data = ramapi.Character.get_page(num_of_page)['results']
            for element in char_page_data:
                char_id = element['id']
                char_name = element['name']
                char_status = element['status']
                char_species = element['species']
                char_type = element['type']
                char_gender = element['gender']
                char_origin = element['origin']['name']
                char_location = element['location']['name']
                num_of_episods = len(element['episode'])
                percentage_of_episods = str(int(100 / 51 * len(element['episode'])))
                links_for_episodes = element['episode']

                list_of_epi_names = []
                for page in links_for_episodes:
                    epi_name = requests.get(page).json()['name']
                    list_of_epi_names.append(epi_name)

                sorted_list_of_epi_names = sorted(list_of_epi_names)

                with connection.cursor() as cursor:
                    cursor.execute(
                        """INSERT INTO characters(id, name, status, species, type, gender, origin, location, num_of_episods, name_of_episods, percentage_of_episods) 
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
                            char_id, char_name, char_status, char_species, char_type, char_gender, char_origin,
                            char_location,
                            num_of_episods, sorted_list_of_epi_names, percentage_of_episods)
                    )
                    print(f"Character Data successfully uploaded")

        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")


    #Filling_The_Locations_DB
    for num_of_page in range(1, Loc_num_pages + 1):

        try:
            #Connect_To_Exist_Database
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=dbname
            )

            connection.autocommit = True

            #Location
            locations_data = ramapi.Location.get_page(num_of_page)['results']
            for location in locations_data:
                loc_id = location['id']
                loc_name = location['name']
                loc_type = location['type']
                loc_url = location['url']

                with connection.cursor() as cursor:
                    cursor.execute(
                        """INSERT INTO location(id, name, type, url)
                            VALUES(%s, %s, %s, %s)""", (loc_id, loc_name, loc_type, loc_url)
                    )
                    print(f"Location Data successfully uploaded")

        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")


    #Filling_The_Episodes_DB
    for num_of_page in range(1, Epi_num_pages + 1):

        try:
            #Connect_To_Exist_Database
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=dbname
            )

            connection.autocommit = True

            #Episodes
            episodes_data = ramapi.Episode.get_page(num_of_page)['results']
            for episod in episodes_data:
                epi_id = episod['id']
                epi_name = episod['name']
                epi_num = episod['episode']
                epi_date = episod['air_date']

                with connection.cursor() as cursor:
                    cursor.execute(
                        """INSERT INTO episodes(id, name, episode, air_date)
                            VALUES(%s, %s, %s, %s)""", (epi_id, epi_name, epi_num, epi_date)
                    )
                    print(f"Episodes Data successfully uploaded")

        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)

        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")
