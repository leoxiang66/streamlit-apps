import sthelper as helper
from mypages import (
welcome,
home
)


session = helper.OpenSession(
    current_page='welcome',
    page_map=dict(
        welcome = welcome,
        home = home
    )
)

session.render()

