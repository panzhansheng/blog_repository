import inject
import typing
from models.Blog import Blog
from repositories.blog_repository import BlogRepository


class BlogService: 

    blog_repository = inject.attr(BlogRepository)

    def getall(self) -> typing.List[Blog]:
        list = self.blog_repository.all()
        return list
