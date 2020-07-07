# -*- coding: utf-8 -*-
from datetime import datetime


def year(request):
    year_now = datetime.now().year
    return locals()
