from fastapi import APIRouter
from src.application.use_cases.get_user import GetUserUseCase
from src.infrastructure.repositories.user_repository_impl import UserRepositoryImpl

router = APIRouter()

@router.get("/users/{user_id}")
def get_user(user_id: str):
    repo = UserRepositoryImpl()
    use_case = GetUserUseCase(repo)
    return use_case.execute(user_id)
