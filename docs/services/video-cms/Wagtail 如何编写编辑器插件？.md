
# 简介

# 扩展块对象

# 扩展编辑器工具栏

正常编辑器 有个工具栏  在上方
![](attachments/Pasted%20image%2020240420194843.png)

```python
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList

class BlogPage(Page):
    # field definitions omitted

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
    ]
    sidebar_content_panels = [
        SnippetChooserPanel('advert'),
        InlinePanel('related_links', label="Related links"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(sidebar_content_panels, heading='Sidebar content'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])
```



# 参考

1. https://docs.wagtail.org/en/stable/extending/extending_draftail.html
2. https://github.com/gnu4cn/wagtailCMS-tutorial/blob/master/advanced_topics/customisation/extending_draftail.md
3. https://docs.wagtail.org/en/v2.13.5/advanced_topics/customisation/extending_draftail.html
4. https://dev.to/lb/adding-a-react-component-in-wagtail-admin-3e
5. https://docs.wagtail.org/en/v2.12/advanced_topics/customisation/extending_draftail.html?highlight=react#creating-new-entities
6. https://docs.wagtail.org/en/v2.12/advanced_topics/customisation/admin_templates.html#extending-clientside-components
7. 