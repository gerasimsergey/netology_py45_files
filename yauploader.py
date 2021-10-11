import os
import requests
from tokens import token


class YaUploader:
    BASE_URL = 'https://cloud-api.yandex.net/v1/disk'


    def __init__(self):
        self.token = token
        self.headers = {
            "Accept": "application/json",
            "Authorization": "OAuth " + self.token
        }

    def __get_url_to_upload(self, file_path):
        file_name =  os.path.basename(file_path)
        url = self.BASE_URL + '/resources/upload'
        headers = self.headers
        params = {'path': f'{file_name}', 'overwrite': 'true'}
        response = requests.get(url=url, headers=headers, params=params)
        return response.json().get('href')


    def upload(self, file_path):
        upload_url = self.__get_url_to_upload(file_path)
        with open(file_path, "rb") as file:
            response = requests.put(url=upload_url, data=file)
        response.raise_for_status()
        if response.status_code == 201:
            print('Done')