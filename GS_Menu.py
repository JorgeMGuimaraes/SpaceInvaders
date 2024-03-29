#Region Preprocessor
#from GameStateBehavior import GameStateBehavior
import  DisplayUtils    as      dsman
from    enum            import  Enum
from    PPlay.gameimage import  *
from    PPlay.keyboard  import  *
from    PPlay.mouse     import  *
from    GameStates      import  *
from    Button          import  *
#End Region

class SubMenus(Enum):
    NewGame         = 1
    MainMenu        = 2
    Dificuldades    = 4
    Rankings        = 8
    Exit            = 512

class GS_Menu():
    #Region Fields
    game_images     = []
    buttons_parent  = []
    #End Region
    #Region Constructors
    def __init__(self, game):
        self.game       = game
        self.janela     = self.game.janela
        self.mouse      = self.janela.get_mouse()
        self.teclado    = self.janela.get_keyboard()
        self.is_running = True
        self.min_time   = 0.5
        return
    #End Region
    #Region Methods
    def on_state_enter(self):
        self.set_menu_images()
        self.set_menu_buttons()
        self.timer = 0
        return
    
    def on_state_exit(self):
        self.is_running = False
        self.buttons_parent.clear()
        self.game_images.clear()
        return

    def process_inputs(self):
        #if self.teclado.key_pressed("ESC"): self.game_mngr.is_playing = False
        return

    def update(self):
        if self.is_running:
            self.timer  += self.janela.delta_time()
            clicked     = self.mouse.is_button_pressed(1)
            for btn in self.buttons_parent:
                btn.on_mouse_over(self.mouse.get_position())
                if self.timer >= self.min_time:
                    tmp_state = btn.on_mouse_click(clicked)
                    if tmp_state is not None:
                        self.game.change_state(tmp_state)
        return

    def render(self):
        dsman.drawStack(self.game_images)
        self.janela.update()
        return
    
    def set_menu_images(self):
        bg     = GameImage("Assets/images/bg.png")
        logo   = GameImage("Assets/logo.png")
        logo.x = (self.janela.width / 2) - (logo. width / 2)
        logo.y = 25.0
        self.game_images.append(bg)
        self.game_images.append(logo)
        return 
    
    def set_menu_buttons(self):
        x_tela      = self.janela.width * 0.5
        y_tela      = self.janela.height * 0.5
        dist_btn    = 70
        self.buttons_parent.append(Button("Assets/images/Btn_01.png", "Assets/images/Btn_hover_01.png", x_tela, y_tela, GameStates.Running))
        y_tela      += dist_btn
        self.buttons_parent.append(Button("Assets/images/Btn_03.png", "Assets/images/Btn_hover_03.png", x_tela, y_tela, GameStates.Dificuldades))
        y_tela      += dist_btn
        self.buttons_parent.append(Button("Assets/images/Btn_05.png", "Assets/images/Btn_hover_05.png", x_tela, y_tela, GameStates.Ranking))
        y_tela      += dist_btn
        self.buttons_parent.append(Button("Assets/images/Btn_07.png", "Assets/images/Btn_hover_07.png", x_tela, y_tela, GameStates.Exit))
        for b in self.buttons_parent: self.game_images.append(b.game_image)
        return
    #End Region