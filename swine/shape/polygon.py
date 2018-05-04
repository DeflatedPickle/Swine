#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import pyglet

from swine import GameObject, Scene


class Polygon(GameObject):
    def __init__(self, scene, fill=True, point_total=0, x=0, y=0, layer=0, points=[], colours=[]):
        # type: (Scene, bool, int, int, int, int, list[int], list[str]) -> None
        GameObject.__init__(self, scene=scene)
        self._layer = layer
        self._scene = scene
        self._x = x
        self._y = y

        if isinstance(colours, list):
            while len(colours) < point_total:
                colours.append(colours[-1])

            colours = tuple(sum(colours, ()))
        elif isinstance(colours, tuple):
            colours *= point_total

        if fill:
            mode = pyglet.gl.GL_POLYGON
        else:
            mode = pyglet.gl.GL_LINE_LOOP

        self.batch = pyglet.graphics.Batch()
        self.batch.add(point_total, mode, None,
                       ('v2i', points),
                       ('c3B', colours))
        self._scene.batch_list.append(self.batch)

        self._scene.object_list.append(self)