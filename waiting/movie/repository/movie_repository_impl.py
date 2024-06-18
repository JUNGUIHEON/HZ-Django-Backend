import os

from waiting import settings
from movie.entity.models import Movie
from movie.repository.movie_repository import MovieRepository


class MovieRepositoryImpl(MovieRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        return Movie.objects.all().order_by('registeredDate')

    def create(self, movieName, movieReleaseDate, movieFilmRating, movieGenre, movieCountry,
               movieRunningTime, movieSummary, moviePrice, movieImage):

        # uploadDirectory = os.path.join(
        #     settings.BASE_DIR,
        #     '../../../../ui/lecture/first/src/assets/images/uploadImages'
        # )
        # if not os.path.exists(uploadDirectory):
        #     os.makedirs(uploadDirectory)
        #
        # imagePath = os.path.join(uploadDirectory, productImage.name)
        # with open(imagePath, 'wb+') as destination:
        #     for chunk in productImage.chunks():
        #         destination.write(chunk)

        movie = Movie(
            movieName=movieName,
            movieReleaseDate=movieReleaseDate,
            movieFilmRating=movieFilmRating,
            movieGenre=movieGenre,
            movieCountry=movieCountry,
            movieRunningTime=movieRunningTime,
            movieSummary=movieSummary,
            moviePrice=moviePrice,
            movieImage=movieImage.name
        )
        movie.save()
        return movie
