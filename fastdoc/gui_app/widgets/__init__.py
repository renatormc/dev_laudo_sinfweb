from typing import TYPE_CHECKING, Type
from .stext import SText
from .scombo_box import SComboBox
from .sdate import SDate
from .sfolder_pics import SFolderPics
from .sobjects_by_pics import SObjetctsByPics
from .scheck_box import SCheckBox
from .sspin_box import SSpinBox
from .sarray import SArray

if TYPE_CHECKING:
    from .swidget import SWidget

__widgets__: list[Type['SWidget']] = [
    SText,
    SComboBox,
    SDate,
    SFolderPics,
    SObjetctsByPics,
    SCheckBox,
    SSpinBox,
    SArray
]
