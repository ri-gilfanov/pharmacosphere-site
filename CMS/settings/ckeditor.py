
CKEDITOR_JQUERY_URL = '/static/jquery-3.1.1.min.js'


CKEDITOR_UPLOAD_PATH = 'images/'

# Группировка изображений по папкам пользователей и разграниченный доступ,
# названия папок по полю username
CKEDITOR_RESTRICT_BY_USER = True

# Бэкенд для создания миниатюрок изображений
CKEDITOR_IMAGE_BACKEND = 'pillow'

# Просмотр изображений с группировкой по папкам
CKEDITOR_BROWSE_SHOW_DIRS = True

# Загрузка файлов, отличных от изображений
CKEDITOR_ALLOW_NONIMAGE_FILES = False


CKEDITOR_CONFIGS = {
        'dflt_config': {
        'resize_dir': 'both',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Source','Maximize','ShowBlocks','DocProps','Preview',],
            ['Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo',],
            ['Find','Replace','-','SelectAll','-','SpellChecker',],
            ['Link','Unlink','Anchor'],
            ['Image', 'Youtube', 'Table',],
            '/',
            ['Format'],
            ['Bold','Italic','Underline'],
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            ['NumberedList','BulletedList','-','Outdent','Indent'],
            ['Subscript','Superscript','-','Blockquote',],
            ['RemoveFormat'],
        ],
        'width': '100%',
        'format_tags': 'p;h2;h3;h4;h5;h6;pre;address;div',
        'allowedContent': False,  # разрешение на вставку скриптов
        'contentsCss': ['/sf/core/common.css', ],
        'extraPlugins': 'youtube',
    },
}
AWS_QUERYSTRING_AUTH = False
