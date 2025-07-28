from typing import List

import core.object.gui.CoverWin as CoverWin
import core.object.gui.MainWin as MainWin
import core.object.gui.page.Mask as Mask
import core.object.User as ObjectUser

class gui:
    cover_stack:List[CoverWin.CoverWin]=[]
    main_win:MainWin.Main=None
    mask:Mask.MaskFrame=None

User:ObjectUser.User
lanucherConfig:dict=None