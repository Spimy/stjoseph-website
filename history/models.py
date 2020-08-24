from django.db import models


class HistoryManager(models.Manager):
    def get_queryset(self):
        return super(HistoryManager, self).get_queryset().order_by('title')

    def sort(self):
        queryset = super(HistoryManager, self).get_queryset().order_by('title')
        not_nums_index = 0

        for query in queryset:
            if ord(query.title[0]) > 48 and ord(query.title[0]) < 57:
                not_nums_index += 1

        try:
            queryset.get(title__iexact='history')
        except:
            return queryset[not_nums_index:] + queryset[:not_nums_index]
        else:
            history = queryset.get(title__iexact='history')
            queryset.exclude(id=history.id)
            return [history] + queryset[not_nums_index:] + queryset[:not_nums_index]


class History(models.Model):

    title = models.CharField(max_length=10)
    description = models.TextField()
    objects = HistoryManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Histories'
