from sqlalchemy.orm import Session
from datetime import datetime
from api.models import Post, Comment
# ========== import Schema ==========
from api.schema import CreatePostSchema, UpdatePostSchema, CreateCommentSchema

# ========== CREATE ==========
def create_post(db : Session, post : CreatePostSchema):
    post = Post(subject = post.subject,
                content = post.content,
                date = datetime.now())
    db.add(post)
    db.commit()

# ========== READ LIST ==========
def get_post_list(db : Session):
    post_list = db.query(Post).order_by(Post.date.desc()).all()
    return post_list

# ========== READ LIST BY JSON ==========
def get_post_list_by_json(db : Session):
    post_list = db.query(Post).all()
    post_json = []
    for post in post_list:
        post_detail = {
            "id" : post.id,
            "title" : post.subject,
            "content" : post.content,
        }
        post_json.append(post_detail)
    return post_json

# ========== READ DETAIL ==========
def get_post_detail(db : Session, post_id : int):
    post = db.query(Post).get(post_id)
    return post

# ========== UPDATE ==========
def update_post(db : Session, post_id : int, post_update : UpdatePostSchema):
    post = db.query(Post).filter(Post.id == post_update.post_id).first()
    if post:
        post.subject = post_update.subject
        post.content = post_update.content
        post.date = datetime.now()
        db.commit()
        return post
    return None   

# ========== DELETE ==========
def delete_post(db : Session, post : Post):
    db.delete(post)
    db.commit()


# ========== GET Comment ==========
def get_comment_list(db : Session, post_id : int):
    post = db.query(Post).get(post_id)
    return post.comments


# ========== CREATE Comment ==========
def create_comment(db: Session, post_id: int, comment_data: CreateCommentSchema):
    post = db.query(Post).get(post_id)
    comment = Comment(post=post, content=comment_data.content, date=datetime.now())
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment
