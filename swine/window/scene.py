#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

from pyglet.graphics import Batch


class Scene(object):
    def __init__(self, window):
        self.window = window

        self.batch = Batch()
        self.batch_list: List[Batch] = [self.batch]

        self.object_list = []

        self.window.scene_list.append(self)
