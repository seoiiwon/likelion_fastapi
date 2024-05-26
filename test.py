from api.models import Post, Comment
from datetime import datetime
from config.database import SessionLocal

db = SessionLocal()

# 게시물 데이터
def 게시물_작성():
    title = input("제목을 입력하세요 : ")
    story = input("내용을 입력하세요 : ")
    time = datetime.now()

    p = Post(subject=title, content=story, date=time)
    db.add(p)
    db.commit()


def 게시물_가져오기():
    idx = int(input("몇번째 글을 가져올까요?(0 입력시 전체 가져오기) : "))
    if idx == 0:
        all_posts = db.query(Post).all()
        for post in all_posts:
            print(f"id : {post.id} / 제목 : {post.subject} / 내용 : {post.content} / 작성일시 : {post.date}")
    else:
        post = db.get(Post, idx)
        print(f"id : {post.id} / 제목 : {post.subject} / 내용 : {post.content} / 작성일시 : {post.date}")


def 게시물_수정():
    idx = int(input("몇번째 글을 수정할까요? : "))
    target_post = db.get(Post, idx)
    what_to_do = int(input("무엇을 수정할까요? (1:제목, 2:내용) : "))

    if what_to_do == 1:
        target_post.subject = input("새 제목 : ")
    elif what_to_do == 2:
        target_post.content = input("새 내용 : ")

    db.commit()


def 게시물_삭제():
    idx = int(input("몇번째 글을 삭제할까요? : "))
    target_post = db.get(Post, idx)
    db.delete(target_post)
    db.commit()


# 댓글 데이터
def 댓글_작성():
    idx = int(input("몇번째 글에 댓글을 작성하시겠어요? : "))
    content = input("댓글을 작성해주세요 : ")

    p = db.get(Post, idx)
    c = Comment(post=p, content=content, date=datetime.now())
    db.add(c)
    db.commit()


def 댓글_조회():
    idx = int(input("몇번째 댓글을 조회하시겠어요?(0 입력시 전체 조회) : "))
    if idx == 0:
        all_comments = db.query(Comment).all()
        for comment in all_comments:
            print(f"id : {comment.id} / 내용 : {comment.content} / 작성일시 : {comment.date}")
    else:
        comment = db.get(Comment, idx)
        print(f"id : {comment.id} / 내용 : {comment.content} / 작성일시 : {comment.date}")


def 댓글의_게시물_조회():
    idx = int(input("몇번째 댓글의 게시글을 조회하시겠어요? : "))
    c = db.get(Comment, idx)
    print(f"id : {c.post.id} / 제목 : {c.post.subject} / 내용 : {c.post.content} / 작성일시 : {c.post.date}")


def 게시물의_댓글_조회():
    idx = int(input("몇번째 글의 댓글을 조회하시겠어요? : "))
    p = db.get(Post, idx)
    for comment in p.comments:
        print(f"id : {comment.id} / 내용 : {comment.content} / 작성일시 : {comment.date}")


def 댓글_삭제():
    idx = int(input("몇번째 댓글을 삭제하시겠어요? : "))
    c = db.get(Comment, idx)
    db.delete(c)
    db.commit()
    

while 1:
    upload_type = int(input("1 : 게시글 / 2 : 댓글 / 3 : 종료 : "))
    if upload_type == 1:
        mode = int(input("1 : 작성 / 2 : 가져오기 / 3 : 수정 / 4 : 삭제 / 5 : 돌아가기 : "))
        if mode == 1:
            게시물_작성()
        elif mode == 2:
            게시물_가져오기()
        elif mode == 3:
            게시물_수정()
        elif mode == 4:
            게시물_삭제()
        elif mode == 5:
            continue
        print()
    elif upload_type == 2:
        mode = int(input("1 : 작성 / 2 : 조회 / 3 : 댓글의 게시물 조회 / 4 : 게시물의 댓글 조회 / 5 : 삭제 / 6: 돌아가기 : "))
        if mode == 1:
            댓글_작성()
        elif mode == 2:
            댓글_조회()
        elif mode == 3:
            댓글의_게시물_조회()
        elif mode == 4:
            게시물의_댓글_조회()
        elif mode == 5:
            댓글_삭제()
        elif mode == 6:
            continue
        print()
    elif upload_type == 3:
        print()
        break