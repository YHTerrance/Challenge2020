class EventManager:
    '''
    We coordinate communication between the Model, View, and Controller.
    '''
    def __init__(self):
        self.listeners = []

    def register_listener(self, listener):
        '''
        Adds a listener to our spam list.
        It will receive Post()ed events through it's notify(event) call.
        '''
        self.listeners.append(listener)

    def unregister_listener(self, listener):
        '''
        Remove a listener from our spam list.
        This is implemented but hardly used.
        Our weak ref spam list will auto remove any listeners who stop existing.
        '''
        pass

    def post(self, event):
        '''
        Post a new event to the message queue.
        It will be broadcast to all listeners.
        '''
        # # this segment use to debug
        # if not (isinstance(event, Event_EveryTick) or isinstance(event, Event_EverySec)):
        #     print( str(event) )
        for listener in self.listeners:
            listener.notify(event)


class BaseEvent:
    '''
    A superclass for any events that might be generated by
    an object and sent to the EventManager.
    '''
    name = 'Generic event'
    def __init__(self):
        pass

    def __str__(self):
        return self.name


class EventInitialize(BaseEvent):
    name = 'Initialize event'
    '''
    initialize and model stage change to STATE_MENU
    '''


class EventPickArena(BaseEvent):
    name = 'StageSelect Event'

    def __init__(self, stage):
        self.stage = stage


class EventPlay(BaseEvent):
    name = 'GamePlay event'
    '''
    game play and model stage change to STATE_PLAY
    '''


class EventStop(BaseEvent):
    name = 'GameStop event'
    '''
    game stop and model stage change to STATE_STOP
    '''


class EventContinue(BaseEvent):
    name = 'GameContinue event'
    '''
    game continue and model stage change to STATE_PLAY
    '''


class EventRestart(BaseEvent):
    name = 'GameRestart event'
    '''
    game restart and model stage change to STATE_MENU
    '''


class EventTimesUp(BaseEvent):
    name = "Time's Up event"


class EventQuit(BaseEvent):
    name = 'Quit event'


class EventEveryTick(BaseEvent):
    name = 'Tick event'


class EventPlayerMove(BaseEvent):
    name = 'PlayerMove event'

    def __init__(self, player_id, direction):
        self.player_id = player_id
        self.direction = direction

    def __str__(self):
        return f'{self.name} => player_id {self.player_id} move {self.direction}'


class EventPlayerJump(BaseEvent):
    name = 'PlayerJump event'

    def __init__(self, player_id):
        self.player_id = player_id

    def __str__(self):
        return f'{self.name} => player_id {self.player_id} jump'


class EventPlayerAttack(BaseEvent):
    name = 'PlayerAttack event'

    def __init__(self, player_id):
        self.player_id = player_id

    def __str__(self):
        return f'{self.name} => player_id {self.player_id} attack'


class EventPlayerRespawn(BaseEvent):
    name = 'PlayerRespawn event'

    def __init__(self, player_id):
        self.player_id = player_id

    def __str__(self):
        return f'{self.name} => player_id {self.player_id} respawn'


class EventPlayerDied(BaseEvent):
    name = 'PlayerDied event'

    def __init__(self, player_id):
        self.player_id = player_id

    def __str__(self):
        return f'{self.name} => player_id {self.player_id} died'


class EventPlayerItem(BaseEvent):
    name = 'Player press item button (contoller => model)'

    def __init__(self, player_id):
        self.player_id = player_id

    def __str__(self):
        return f'{self.name} => player_id {self.player_id}'


class EventPlayerPickItem(BaseEvent):
    name = 'Player pick item event (model => view)'

    def __init__(self, player_id, item_id):
        self.player_id = player_id
        self.item_id = item_id

    def __str__(self):
        return f'{self.name} => player_id {self.player_id} pick item {self.item_id}'


class EventToggleFullScreen(BaseEvent):
    name = 'ToggleFullScreen event'


class EventUseBananaPistol(BaseEvent):
    name = 'UseBananaPistol event'

    def __init__(self, peel_position, bullet_position, used_time):
        self.peel_position = peel_position # initial position, it'll be affected by gravity
        self.bullet_position = bullet_position # initial position, it'll fly
        self.used_time = used_time


class EventUseBigBlackHole(BaseEvent):
    name = 'UseBigBlackHole event'

    def __init__(self, black_hole_position, used_time):
        self.black_hole_position = black_hole_position
        self.used_time = used_time


class EventUseCancerBomb(BaseEvent):
    name = 'UseCancerBomb event'

    def __init__(self, cancer_bomb_position, used_time):
        self.bomb_position = cancer_bomb_position # initial position, it'll be affected by gravity
        self.used_time = used_time


class EventUseZapZapZap(BaseEvent):
    name = 'UseZapZapZap event'

    def __init__(self, player_position, used_time):
        self.player_position = player_position
        self.used_time = used_time


class EventUseBananaPeel(BaseEvent):
    name = 'UseBananaPeel event'

    def __init__(self, peel_position, used_time):
        self.peel_position = peel_position # initial position, it'll be affected by gravity
        self.used_time = used_time


class EventSlipOnBananaPeelSound(BaseEvent):
    name = 'SlipOnBananaPeelSound event'


class EventUseRainbowGrounder(BaseEvent):
    name = 'UseRainbowGrounder event'

    def __init__(self, player_position, used_time):
        self.player_position = player_position
        self.used_time = used_time


class EventUseInvincibleBattery(BaseEvent):
    name = 'UseInvincibleBattery event'

    def __init__(self, player_position, used_time):
        self.player_position = player_position
        self.used_time = used_time


class EventDeathRainTrigger(BaseEvent):
    # Call when the death rain box be touched
    name = 'Death rain trigger event (model => view)'

    def __init__(self, position, time):
        self.position = position
        self.time = time


class EventDeathRainStart(BaseEvent):
    # Call when going to rain
    name = 'Death rain event (view => model)'


class EventBombExplode(BaseEvent):
    name = 'BombExplode event'

    def __init__(self, position):
        self.position = position

class EventCutInStart(BaseEvent):
    name = 'Cut-in start event'

    def __init__(self, player_id, item_id):
        self.player_id = player_id
        self.item_id = item_id

    def __str__(self):
        return f'{self.name} => player_id {self.player_id} use item_id {self.item_id} with cut in'

class EventCutInEnd(BaseEvent):
    name = 'Cut-in end event'

class EventTypeSound(BaseEvent):
    name = 'Cut-in typing sound event'
