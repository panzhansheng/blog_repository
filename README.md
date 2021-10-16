# blog_repository
This this the demo sample for DeepLearning in Action course in SCNU.
## Repository Pattern
Repository pattern, a simplifying abstraction over data storage, allowing us to decouple our model layer from the data layer. We'll present a concrete example of how this simplifying abstraction makes our system more testable by hiding the complexities of the database.
![](repo.png)

This demo project use inject package for dependency injection. First, we import inject, then inject should be configured:
```
import inject

def config_ioc(binder):
    blog_repository = BlogRepository()

    blog_serivce = BlogService()

    blog_bind = db.BlogSQL

    binder.bind(BlogRepository,blog_repository)

    binder.bind(BlogService,blog_serivce)

    binder.bind(db.BlogSQL,blog_bind)

inject.configure(config_ioc)

```
if you want to inject an instance:
```
blog_service = inject.instance(BlogService)
```

if you want to inject an object attribute:
```
class BlogService: 

    blog_repository = inject.attr(BlogRepository)

    def getall(self) -> typing.List[Blog]:
        list = self.blog_repository.all()
        return list

```


