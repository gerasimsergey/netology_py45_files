import os
from hero import smartest_superhero
from yauploader import YaUploader


if __name__ == '__main__':
    #  Герои
    # print(smartest_superhero())

    # # Загрузка
    path_to_file = os.path.join(os.getcwd(), 'recipes.txt')
    uploader = YaUploader()
    uploader.upload(path_to_file)
