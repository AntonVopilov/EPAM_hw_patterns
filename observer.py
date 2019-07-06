class MyTubeUser:

    def __init__(self, user_name: str):
        self._name = user_name

    def update(self, message: str):
        print(message)


class MyTubeChannel:
    subscribers = []

    def __init__(self, channel_name: str, channel_owner: MyTubeUser):
        self.name = channel_name
        self.owner = channel_owner

    def subscribe(self, user: MyTubeUser):
        self.subscribers.append(user)

    def publish_video(self, video: str):
        for user in self.subscribers:
            message = f'Dear {user._name}, there is new video on \'{self.name}\' channel: \'{video}\''
            user.update(message)

    def publish_playlist(self, playlist: dict):
        playlist_name, videos_list = playlist.popitem()
        for user in self.subscribers:
            message = f'Dear {user._name}, there is new playlist on \'{self.name}\' channel: \'{playlist_name}\''
            user.update(message)


if __name__ == '__main__':
    matt = MyTubeUser('Matt')
    john = MyTubeUser('John')
    erica = MyTubeUser('Erica')
    dogs_life = MyTubeChannel('All about dogs', matt)
    dogs_life.subscribe(john)
    dogs_life.subscribe(erica)
    dogs_nutrition_videos = ['What do dogs eat?', 'Which Pedigree pack to choose?']
    dogs_nutrition_playlist = {'Dogs nutrition': dogs_nutrition_videos}
    for video in dogs_nutrition_videos:
        dogs_life.publish_video(video)
    dogs_life.publish_playlist(dogs_nutrition_playlist)
