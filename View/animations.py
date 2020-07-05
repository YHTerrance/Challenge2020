'''
* How Animation works:

tick = 0
animations = []
while True:
    for ani in animations:
        if ani.expired:
            animations.remove(ani)

    animations.append(new_animation)

    for ani in animations:
        ani.draw(screen)

    tick += 1
'''
import os
import pygame as pg

from Events.EventManager import *
from Model.Model import GameEngine
from Model.GameObject.player import Player
from View.utils import scaled_surface, load_image
import Const

'''
VERY IMPORTANT !!!
VERY IMPORTANT !!!
VERY IMPORTANT !!!

Once you add a new class in this module, you have to add CLASS.init_convert()
in the init_otherobjects() function!
'''


class Animation_base():
    '''
    Base class of all animation.
    There will be a list (call it ANI) of all currently effective animations in main.py of view.
    To start an animation, you have to append the new Animation to ANI.
    Every animation in ANI should be drawn (if valid) or be discarded (if expired) in every tick.
    '''

    def __init__(self, delay_of_frames, **pos):
        self._timer = 0
        self.expired = False

    def update(self):
        pass

    # the "update" argument is for the purpose of GraphicalView.theworld_background in View/main.py
    def draw(self, screen, update=True):
        # draw first
        # update second
        pass

class Animation_raster(Animation_base):
    frames = tuple()

    @classmethod
    def init_convert(cls):
        cls.frames = tuple( _frame.convert_alpha() for _frame in cls.frames )

    def __init__(self, delay_of_frames, expire_time, **pos):
        self._timer = 0
        self.delay_of_frames = delay_of_frames
        self.frame_index_to_draw = 0
        self.expire_time = expire_time
        self.expired = False
        pos[next(iter(pos))] = pg.math.Vector2(pos[next(iter(pos))]) # turn tuple into vec2
        self.pos = pos

    def update(self):
        self._timer += 1

        if self._timer == self.expire_time:
            self.expired = True
        elif self._timer % self.delay_of_frames == 0:
            self.frame_index_to_draw = (self.frame_index_to_draw + 1) % len(self.frames)

        # update self.pos if needed
        # self.pos[ next(iter(self.pos)) ] = pg.math.Vector2(next_pos)
        # or
        # self.pos[ next(iter(self.pos)) ] += pg.math.Vector2(dx, dy)

    # the "update" argument is for the purpose of GraphicalView.theworld_background in View/main.py
    def draw(self, screen, update=True):
        screen.blit(
            self.frames[self.frame_index_to_draw],
            self.frames[self.frame_index_to_draw].get_rect(**self.pos),
        )

        if update: self.update()


class Animation_player_attack(Animation_raster):
    frames = tuple(
        scaled_surface(
            load_image(os.path.join(Const.IMAGE_PATH, 'electricattack.png')),
            0.1 + (_i * 0.002)
        )
        for _i in range(1, 7)
    )

    def __init__(self, player: Player):
        self._timer = 0
        self.delay_of_frames = 2
        self.frame_index_to_draw = 0
        self.expire_time = 2*len(self.frames)
        self.expired = False
        self.player = player

    def draw(self, screen, update=True):
        screen.blit(
            self.frames[self.frame_index_to_draw],
            self.frames[self.frame_index_to_draw].get_rect(center=(self.player.position.x , self.player.position.y - Const.ATTACK_ERROR)),
        )

        if update: self.update()

class Animation_player_attack_big(Animation_raster):
    frames = tuple(
        scaled_surface(
            load_image(os.path.join(Const.IMAGE_PATH, 'electricattack.png')),
            0.2 + (_i * 0.002)
        )
        for _i in range(1, 7)
    )

    def __init__(self, player: Player):
        self._timer = 0
        self.delay_of_frames = 2
        self.frame_index_to_draw = 0
        self.expire_time = 2*len(self.frames)
        self.expired = False
        self.player = player

    def draw(self, screen, update=True):
        screen.blit(
            self.frames[self.frame_index_to_draw],
            self.frames[self.frame_index_to_draw].get_rect(center=(self.player.position.x , self.player.position.y - 2*Const.ATTACK_ERROR)),
        )

        if update: self.update()

class Animation_Bomb_Explode(Animation_raster):
    frames = tuple(
        scaled_surface(
            pg.transform.rotate(load_image(os.path.join(Const.IMAGE_PATH, 'heart.png')), 2*_i),
                0.01*_i
            )
            for _i in range(1, 36)
    )

    def __init__(self, **pos):
        super().__init__(2, len(self.frames), **pos)


def init_animation():
    Animation_player_attack.init_convert()
    Animation_Bomb_Explode.init_convert()

