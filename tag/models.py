from painless.models.mixins import OrganizedMixin


class Tag(OrganizedMixin):
    class Meta:
        ordering = [ '-title' ]
        verbose_name = "tag"
        verbose_name_plural = "tags"
     
    
    def __str__(self):
        return self.title
 

