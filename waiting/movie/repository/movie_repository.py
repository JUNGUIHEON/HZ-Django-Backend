from abc import abstractmethod, ABC

class MovieRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, movieName, movieReleaseDate, movieFilmRating, movieGenre, movieCountry,
               movieRunningTime, movieSummary, moviePrice, movieImage):
        pass