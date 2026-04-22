from src.domain.repositories.user_repository import UserRepository

class UserRepositoryImpl(UserRepository):

    def get_by_id(self, user_id: str):
        # DB logic goes here
        return {"id": user_id}

    def save(self, user):
        # DB insert logic
        pass
