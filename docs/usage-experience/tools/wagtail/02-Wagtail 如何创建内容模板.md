
# 02-Wagtail 如何创建内容模板


## 简介

定义一个也没模板本质上是继承一个 `Page` 模型

在 Wagtail 中创建一个页面模板需要遵循以下步骤：

1. **创建模型**：首先，您需要创建一个继承自 `Page` 的自定义页面模型。这可以通过创建一个新的 Python 类来实现，该类应该定义页面的字段和内容结构。例如：

```python
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class CustomPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
```

2. **创建模板**：接下来，您需要创建一个与自定义页面模型相关联的模板文件。默认情况下，Wagtail 使用模板路径 `templates` 下的 `page` 目录来查找页面模板。您可以创建一个名为 `custom_page.html` 的模板文件，用于渲染自定义页面的内容。

3. **链接模板和模型**：最后，您需要将自定义页面模型与创建的模板文件进行关联。这可以通过在自定义页面模型中指定 `template` 属性来实现，例如：

```python
class CustomPage(Page):
    # ... 其他字段和内容结构

    template = "page/custom_page.html"
```

通过遵循以上步骤，您就可以在 Wagtail 中成功创建一个页面模板，并将其与自定义页面模型相关联。这样一来，您就可以使用自定义页面模型来创建新的页面，并使用指定的模板来呈现页面内容。
## 参考
