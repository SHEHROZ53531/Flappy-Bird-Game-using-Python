import pygame as pg
pg.init()
class Bird(pg.sprite.Sprite):
    def __init__(self,scale_factor):
        pg.mixer.init() 
        self.flap_sound = pg.mixer.Sound('sfx/flap.wav')
        
        super(Bird,self).__init__()
        self.img_list = [pg.transform.scale_by(pg.image.load("assets/birdup.png").convert_alpha(),scale_factor),
                        pg.transform.scale_by(pg.image.load("assets/birddown.png").convert_alpha(),scale_factor)]
        
        self.image_index = 0
        self.image = self.img_list[self.image_index]
        self.rect = self.image.get_rect(center=(100,100))
        self.y_speed =0
        self.gravity = 10
        self.flap_speed = 250
        self.animation_counter = 0
        self.update_on = False


    def update(self,dt):
        if self.update_on:
         self.playAnimation()
         self.applyGravity(dt)

         if self.rect.y <=0 and self.flap_speed==250:
            self.rect.y=0
            self.flap_speed=0
            self.y_speed=0
         elif self.rect.y >0 and self.flap_speed==0:    
            self.flap_speed=250
        

    def applyGravity(self,dt):
        self.y_speed += self.gravity*dt
        self.rect.y  += self.y_speed

    def flap(self,dt):
        self.y_speed = -self.flap_speed*dt 
        self.flap_sound.play() 

    def playAnimation(self):
        if self.animation_counter == 5:
            self.image = self.img_list[self.image_index]
            if self.image_index == 0: self.image_index=1
            else: self.image_index=0
            self.animation_counter=0

        self.animation_counter += 1   

    def resetposition(self):
        self.rect.center = (100,100)  # to reset  bird position
        self.y_speed = 0
        self.animation_counter=0




        
