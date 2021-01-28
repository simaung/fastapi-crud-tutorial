from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def home():
    # some async operation could happen here
    # example: `notes = await get_all_notes()`
    return {"Hello":"World"}