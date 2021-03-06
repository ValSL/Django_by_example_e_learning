from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import pdb


class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        # pdb.set_trace()
        if getattr(model_instance, self.attname) is None:
            print(self.attname)
            # no current value
            try:
                qs = self.model.objects.all()
                print(qs)
                if self.for_fields:
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    print(query)
                    qs = qs.filter(**query)
                    print(qs)
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:  # эта ошибка срабатывает скорее всего на строке last_item = qs.latest(self.att)
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)
