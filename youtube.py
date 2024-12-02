import time

class User:
    users = {}                                          # база всех пользователей
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        User.users[nickname] = {'password': self.password, 'age': self.age}

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    all_videos = {}     # все видео на платформе

    def __init__(self):
        self.videos = {}                # собственные видео пользователя
        self.current_user = None        # хронится только ник пользователя, все остальные данные о нем хранятся в User.users

    def log_in(self, nickname, password):
        if nickname in User.users.keys() and (hash(password) == User.users[nickname]['password']):
            self.current_user == nickname

    def register(self, nickname, password, age):
        if nickname not in User.users.keys():
            self.current_user = User(nickname, password, age).nickname
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        self.current_user = None

    def add(self, *videos:Video):
        for i in videos:
            if i.title not in UrTube.all_videos.keys():
                UrTube.all_videos[i.title] = {'duration': i.duration, 'time_now': i.time_now, 'adult_mode': i.adult_mode}
                self.videos[i.title] = {'duration': i.duration, 'time_now': i.time_now, 'adult_mode': i.adult_mode}

    def get_videos(self, word):
        video = []
        for i in UrTube.all_videos.keys():
            if word.lower() in i.lower():
                video.append(i)
        return video

    def watch_video(self, name):
        if name in UrTube.all_videos.keys():
            if self.current_user is None:
                print("Войдите в аккаунт, чтобы смотреть видео")
                return 1
            if User.users[self.current_user]['age'] < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return 1
            for i in range(1, UrTube.all_videos[name]['duration'] + 1):
                time.sleep(1)
                print(i, end = ' ')
            print( "Конец видео")


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)


# Добавление видео

ur.add(v1, v2)



# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))



# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
#print(User.users['vasya_pupkin']['age'])

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')



# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)



# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')