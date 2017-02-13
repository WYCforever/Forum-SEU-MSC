# coding=utf-8

class PostModal:
     def __init__(self, post_id, author_id, title, content, create_time, update_time, viewCount, saveCount, replyCount, is_solved):
         self.post_id = post_id
         self.author_id = author_id
         self.title = title
         self.content = content
         self.create_time = create_time
         self.update_time = update_time
         self.viewCount = viewCount
         self.saveCount = saveCount
         self.replyCount = replyCount
         self.is_solved = is_solved

class ReplyModal:
    def __init__(self, reply_id, author_id, content, create_time, update_time, likeCount, commentCount, bePicked):
        self.reply_id = reply_id
        self.author_id = author_id
        self.content = content
        self.create_time = create_time
        self.update_time = update_time
        self.likeCount = likeCount
        self.commentCount = commentCount
        self.bePicked = bePicked

class PostReplyRecord:
    def __init__(self, post_id, reply_id):
        self.post_id = post_id
        self.reply_id = reply_id

class CommentModal:
    def __init__(self, comment_id, author_id, content, create_time, likeCount):
        self.comment_id = comment_id
        self.author_id = author_id
        self.content = content
        self.create_time = create_time
        self.likeCount = likeCount

class PostCommentRecord:
    def __init__(self, post_id, comment_id):
        self.post_id = post_id
        self.comment_id = comment_id

class ReplyCommentRecord:
    def __init__(self, reply_id, comment_id):
        self.reply_id = reply_id
        self.comment_id = comment_id

class CommentCommentRecord:
    def __init__(self, comment_parent_id, comment_child_id):
        self.comment_parent_id = comment_parent_id
        self.comment_child_id = comment_child_id

class viewRecord:
    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id

class saveRecord:
    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id

class likePostRecord:
    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id

class likeReplyRecord:
    def __init__(self, user_id, reply_id):
        self.user_id = user_id
        self.reply_id = reply_id

class likeCommentRecord:
    def __init__(self, user_id, comment_id):
        self.user_id = user_id
        self.comment_id = comment_id
