from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtCore import Qt, QSize
from fastdoc.gui_app.widgets.types import ObjectPicUserData
 
def ajust_size_hint(item: QListWidgetItem, pic_size: QSize) -> None:
    user_data: ObjectPicUserData = item.data(Qt.UserRole)
    size = user_data.original_size
    h2 = pic_size.height()
    w = int((h2/size.height())*size.width())
    item.setSizeHint(QSize(w + 10, h2 + 50))
    