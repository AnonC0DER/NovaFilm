from django.db import models
import uuid

# Create your models here.
# Movies
class HomePageModel(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey('Director', on_delete=models.CASCADE, default=None)
    release_date = models.CharField(max_length=70, default='None')
    short_intro = models.TextField(max_length=700)
    IMDb_RATING = models.CharField(max_length=50, default=None)
    genre = models.ManyToManyField('Genre')
    poster = models.ImageField(upload_to='Posters/')
    movie_page_poster = models.ImageField(upload_to='Posters/MoviePage/', null=True, blank=True)
    summary = models.TextField(max_length=1600)
    trailer = models.CharField(max_length=650, null=True, blank=True)
    download_link_1080 = models.CharField(max_length=650, null=True, blank=True)
    download_link_720 = models.CharField(max_length=650, null=True, blank=True)
    download_link_480 = models.CharField(max_length=650, null=True, blank=True)
    page_view = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']    


# Serial
class Serial(models.Model):
    Serial_name = models.CharField(max_length=200)
    director = models.ForeignKey('Director', on_delete=models.CASCADE, default=None)
    release_date = models.CharField(max_length=70, default='None')
    short_intro = models.TextField(max_length=700)
    IMDb_RATING = models.CharField(max_length=50, default=None)
    genre = models.ManyToManyField('Genre')
    poster = models.ImageField(upload_to='Posters/')
    seriel_page_poster = models.ImageField(upload_to='Posters/SerialPage/', null=True, blank=True)
    summary = models.TextField(max_length=1600)
    trailer = models.CharField(max_length=650, null=True, blank=True)
    page_view = models.IntegerField(default=1)
    seasons = models.ManyToManyField('Season', default=None)
    episodes = models.ManyToManyField('Episode', default=None)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.Serial_name

    class Meta:
        ordering = ['-created']



# Season - Serial
class Season(models.Model):
    season_name = models.CharField(max_length=50, default='S01 - Serial Name')
    Episodes = models.ManyToManyField('Episode', default=None)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.season_name
    


# Episode - Serial
class Episode(models.Model):
    chose_season = models.ForeignKey('Season', on_delete=models.CASCADE, default=None, null=True, blank=True)
    episode_number = models.CharField(max_length=50, default='E01 - Serial Name')
    download_link1080 = models.CharField(max_length=650, null=True, blank=True)
    download_link720 = models.CharField(max_length=650, null=True, blank=True)
    download_link480 = models.CharField(max_length=650, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.episode_number



# Genres
class Genre(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name



# Directors
class Director(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name



# Comments
class comments(models.Model):
    movie_page = models.ForeignKey(HomePageModel, on_delete=models.CASCADE, null=True, related_name='comments')
    name = models.CharField(max_length=200, default='Guest')
    body =  models.TextField(max_length=650, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


# Comments
class comments_serial(models.Model):
    serial_page = models.ForeignKey(Serial, on_delete=models.CASCADE, null=True, related_name='comments_serial')
    name = models.CharField(max_length=200, default='Guest')
    body =  models.TextField(max_length=650, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name



