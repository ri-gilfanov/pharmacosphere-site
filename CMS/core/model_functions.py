def del_img_at_obj_del(sender, **kwargs):
    '''Удаление файла изображения при удалении объекта'''
    try:
        object_ = kwargs.get('instance')
        storage, path = object_.image.storage, object_.image.path
        storage.delete(path)
    except:
        pass


def del_img_at_obj_change(post_object):
    '''Замена файла изображения при изменении объекта'''
    try:
        pre_object = post_object.__class__.objects.get(id=post_object.id)
        if pre_object.image != post_object.image:
            pre_object.image.delete(save=False)
    except:
        pass
