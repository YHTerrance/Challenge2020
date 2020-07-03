import pygame as pg

from Events.EventManager import EventManager
from Model.Model import GameEngine
from Controller.Controller import Controller
from View.View import GraphicalView
import API.interface

def main():
    pg.init()
    ev_manager = EventManager()
    model      = GameEngine(ev_manager)
    controller = Controller(ev_manager, model)
    view       = GraphicalView(ev_manager, model)
    interface  = API.interface.Interface(ev_manager, model)
    
    model.run()


if __name__ == "__main__":
    main()
