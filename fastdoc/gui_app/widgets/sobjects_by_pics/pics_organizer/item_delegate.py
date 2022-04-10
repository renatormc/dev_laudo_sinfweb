from PyQt5.QtWidgets import  QStyledItemDelegate, QStyleOptionViewItem, QSizeGrip
from PyQt5.QtCore import QSize

class ItemDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        option.decorationPosition = QStyleOptionViewItem.Top
        super(ItemDelegate, self).paint(painter, option, index)