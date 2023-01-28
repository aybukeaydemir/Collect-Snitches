# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 01:56:26 2022

@author: melifay
"""

"""
Grup 8-1 
Aybüke Aydemir
Başak Topçuoğlu
Berkay Caplık
"""

from graphics import Canvas
# import os
# os.system('pip install Pillow')
import random
import time

canvas_size_x = 900
canvas_size_y = 480
size_snitch = 50
location_snitch_y = random.randint (0, canvas_size_y - size_snitch)
speed_snitchs = 20
score = 0
snitchs = []

canvas = Canvas(canvas_size_x, canvas_size_y)
canvas.set_canvas_title("Collect Snitchs")

background = canvas.create_image_with_size(0, 0, canvas_size_x, canvas_size_y, "background1.jpg")
harry = canvas.create_image_with_size(90, 205, 70, 70, "harry.png")
bina = canvas.create_image_with_size(-50, -50, 150, 590, "bina1.png")
score_table = canvas.create_text(800, 430, "Score :"+str(score) )
canvas.set_font(score_table, "Courier", 20)
canvas.set_color(score_table, "black")


def create_background():
    background = canvas.create_image_with_size(0, 0, canvas_size_x, canvas_size_y, "background1.jpg")
    return background

def create_harry():
    harry = canvas.create_image_with_size(90, 205, 70, 70, "harry.png")
    return harry

def create_bina():
    bina =canvas.create_image_with_size(-50, -50, 150, 590, "bina1.png")
    return bina

def create_score_table(score):
    score_table = canvas.create_text(800, 430, "Score :"+str(score) )
    canvas.set_font(score_table, "Courier", 20)
    canvas.set_color(score_table, "black")
    return score_table

def create_snitch(location_snitch_y):
    snitch = canvas.create_image_with_size(canvas_size_x - size_snitch, location_snitch_y, size_snitch, size_snitch, "snitch.png")
    snitchs.append(snitch)
    return snitch

    
        
def check_collisions_harry(canvas,harry,background,score,score_table):
    if len(canvas.coords(harry))>1:
        harry_coords = canvas.coords(harry)
        harry_x_left = harry_coords[0]
        harry_y_top = harry_coords[1]
        colliding_list = canvas.find_overlapping(harry_x_left+10,harry_y_top, harry_x_left+10,harry_y_top+50)
        for collider in colliding_list:
            if collider != background and collider != harry:
                canvas.delete(collider)
                canvas.delete(score_table)
                score += 1
                score_table=create_score_table(score)
        return score , score_table

def check_collisions_bina(canvas ,bina, background, score, snitchs, harry):
        colliding_list = canvas.find_overlapping(0 , 0 , 50, canvas_size_y)
        for collider in colliding_list:
            if collider != background and collider != bina:
                time.sleep(0.5)
                canvas.delete_all()
                background = create_background()
                game_over = canvas.create_text(450, 200,'Game Over')
                canvas.set_font(game_over, "Courier", 50)
                canvas.set_color(game_over, "red")
                show_score = canvas.create_text(460, 250, 'Your Score :'+str(score))
                canvas.set_font(show_score, "Courier", 25)
                canvas.set_color(show_score, "red")
                
                
                canvas.wait_for_click()
                canvas.delete_all()
                score = 0
                snitchs = []
                background = create_background()
                harry = create_harry()
                bina = create_bina()
                canvas.wait_for_click()

        return score, snitchs, background, harry,bina


canvas.wait_for_click()

while True:
    #ilk snitch i oluşturma
    if len(snitchs) == 0:
        location_snitch_y = random.randint(0, canvas_size_y - size_snitch)
        snitch = create_snitch(location_snitch_y)      
        
    #mouse hareketinin y sini alma
    mouse_y = canvas.get_mouse_y()
    y = min(max(mouse_y, 0),canvas_size_y - 70)   
    
    #snitch sayısı 0dan fazla ise harry ye hareket kazandırıyor
    canvas.moveto(harry, 90, y) 
    
    #snitchleri sola doğru hareket ettiriyor.
    for i in range(len(snitchs)):
        canvas.move(snitchs[i], - speed_snitchs, 0)
    
    #snitchler canvasın 1/3 ve 2/3 lük x kısmına geldikçe yeni bir snitch yolluyor
    
    ucte_biri = (canvas_size_x)/3
    if  canvas.get_left_x(snitch) == (ucte_biri)-10 or canvas.get_left_x(snitch) == 2*(ucte_biri)+ 10:
            location_y = random.randint(0, canvas_size_y - size_snitch)
            snitch = create_snitch(location_y) 
    
    #snitchlerin harry ye ve binaya çarpma durumunu kontrol ediyor
    score, score_table = check_collisions_harry(canvas,harry,background, score,score_table)
    score, snitchs, background , harry, bina = check_collisions_bina(canvas ,bina, background, score, snitchs, harry)
    
    
    time.sleep(0.05)
    canvas.update()

canvas.maicolorloop()








