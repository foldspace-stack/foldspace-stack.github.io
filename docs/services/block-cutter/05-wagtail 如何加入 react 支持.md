

# django 模版渲染

模版渲染使用 
https://github.com/Frojd/django-react-templatetags/tree/develop

```python
from django.shortcuts import render

def menu_view(request):
    return render(request, 'myapp/index.html', {
        'menu_data': {
            'example': 1,
        },
    })
```

html

```html
{% load react %}
<html>
    <head>...</head>

    <body>
        <nav>
            {% react_render component="Menu" props=menu_data %}
        </nav>
    </body>

    <!-- Your js includes should be included here, example:
    <script type="text/javascript" src="/static/myapp/js/react-and-react-dom.js"></script>
    <script type="text/javascript" src="/static/myapp/js/my-components.js"></script>
    -->
    {% react_print %}
</html>
```

# 组件编写


https://storybook.js.org/tutorials/intro-to-storybook/react/en/get-started/

使用 stroybook 编写无头组件 



![](attachments/Pasted%20image%2020240719204749.png)



修改 `main.js`

![](attachments/Pasted%20image%2020240719204845.png)


# 参考
1. https://tw-elements.com/docs/standard/integrations/react-integration/
2. https://dev.to/hexnickk/django-templates-with-react-4hko
3. https://github.com/Frojd/django-react-templatetags/tree/develop