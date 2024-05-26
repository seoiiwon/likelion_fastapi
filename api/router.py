from fastapi import APIRouter, Depends, Request, status, HTTPException, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from api import crud, schema, models
# ========== import from database ==========
from config.database import get_db

router = APIRouter(prefix="/api",)
templates = Jinja2Templates(directory="templates")

# 01. CREATE 

# ========== READ HTML ==========
@router.get("/post/create", response_class=HTMLResponse)
async def post_create_html(request : Request):
    return templates.TemplateResponse(name="post_create.html", request=request)

# ========== CREATE POST ==========
@router.post("/post/create", status_code=status.HTTP_204_NO_CONTENT)
async def post_create(post_create : schema.CreatePostSchema, db : Session=Depends(get_db)):
    crud.create_post(db=db, post=post_create)


# 02. READ

# ========== READ POST LIST HTML ==========
@router.get("/post/list", response_class=HTMLResponse)
async def post_list_html(request: Request, db: Session = Depends(get_db)):
    post_list_all = crud.get_post_list(db)
    return templates.TemplateResponse(name="post_list.html", context={"request": request, "post_list_all": post_list_all})

# ========== READ POST LIST JSON ==========
@router.get("/post/list/json", status_code=status.HTTP_200_OK)
def post_list_by_json(db : Session=Depends(get_db)):
    post_json = crud.get_post_list_by_json(db)
    return JSONResponse(post_json)

# ========== READ POST DETAIL HTML ==========
@router.get("/post/detail/{post_id}", response_class=HTMLResponse)
async def post_detail_html(request : Request, post_id : int, db : Session=Depends(get_db)):
    post = crud.get_post_detail(db, post_id=post_id)
    return templates.TemplateResponse(name="post_detail.html", context={"request" : request, "post" : post})


# 03. UPDATE

# ========== READ POST UPDATE HTML =========== 
@router.get("/post/update/{post_id}", response_class=HTMLResponse)
def post_update_html(request : Request, post_id : int, db : Session=Depends(get_db)):
    post = crud.get_post_detail(db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="글을 찾을 수 없습니다.")
    return templates.TemplateResponse(name="post_update.html", context={"request" : request, "post" : post})

# ========== UPDATE POST ===========
@router.put("/post/update/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def post_update(post_id: int, post_update: schema.UpdatePostSchema, db: Session = Depends(get_db)):
    post = crud.update_post(db=db, post_id=post_id, post_update=post_update)
    if post:
        return {"message": "성공적으로 업데이트되었습니다."}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="해당 포스트를 찾을 수 없습니다.")


# 04. DELETE

# ========== DELETE POST ==========
@router.delete("/post/delete/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def post_delete(post_id : int, db : Session=Depends(get_db)):
    post = crud.get_post_detail(db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="해당 포스트를 찾을 수 없습니다.")
    crud.delete_post(db=db, post=post)


# 05. Comment List
# @router.get("/comment/list/{post_id}", response_class=HTMLResponse)
# async def comment_list_html(request : Request, post_id : int, db : Session=Depends(get_db)):
#     comment_list_all = crud.get_comment_list(db, post_id=post_id)
#     return templates.TemplateResponse(name="comment_list.html", context={"request" : request, "comment_list_all" : comment_list_all})

@router.get("/comment/list/{post_id}", response_class=HTMLResponse)
async def comment_list_html(request: Request, post_id: int, db: Session = Depends(get_db)):
    comment_list_all = crud.get_comment_list(db, post_id=post_id)
    return templates.TemplateResponse(name="comment_list.html", context={"request": request, "comment_list_all": comment_list_all, "post_id": post_id})


@router.post("/comment/list/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def comment_create(post_id: int, content: str = Form(...), db: Session = Depends(get_db)):
    comment_data = schema.CreateCommentSchema(content=content)
    crud.create_comment(db=db, post_id=post_id, comment_data=comment_data)
    return RedirectResponse(url=f"/api/comment/list/{post_id}", status_code=status.HTTP_303_SEE_OTHER)
