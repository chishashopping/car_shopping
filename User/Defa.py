from rest_framework.response import Response


class DefaultResponse(Response):
    """定义返回JSON数据的响应类"""

    def __init__(self, code=100000, message='操作成功',
                 data=None, status=None, template_name=None,
                 headers=None, exception=False, content_type=None):
        _data = {'code': code, 'message': message}
        if data:
            _data.update(data)
        super().__init__(_data, status, template_name,
                         headers, exception, content_type)