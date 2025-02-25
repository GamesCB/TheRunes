import pygame


pygame.init()
pygame.mixer.init()



# дорожки/тайлы
snow_walk_left_front1 = pygame.image.load('sprites/snow walkway/1.png').convert_alpha()
snow_walk_left_front2 = pygame.image.load('sprites/snow walkway/2.png').convert_alpha()
snow_snowwalk1 = pygame.image.load('sprites/snow walkway/3.png').convert_alpha()
snow_snowwalk2 = pygame.image.load('sprites/snow walkway/4.png').convert_alpha()
snow_walk_right_front1 = pygame.image.load('sprites/snow walkway/5.png').convert_alpha()
snow_walk_right_front2 = pygame.image.load('sprites/snow walkway/6.png').convert_alpha()
snow_walk_right_bottom1 = pygame.image.load('sprites/snow walkway/7.png').convert_alpha()
snow_walk_right_bottom2 = pygame.image.load('sprites/snow walkway/8.png').convert_alpha()
snow_walk_left_bottom1 = pygame.image.load('sprites/snow walkway/9.png').convert_alpha()
snow_walk_left_bottom2 = pygame.image.load('sprites/snow walkway/10.png').convert_alpha()
triangle_left_bottom = pygame.image.load('sprites/snow walkway/a.png').convert_alpha()
triangle_right_bottom = pygame.image.load('sprites/snow walkway/l.png').convert_alpha()
triangle_left_top = pygame.image.load('sprites/snow walkway/c.png').convert_alpha()
triangle_right_top = pygame.image.load('sprites/snow walkway/b.png').convert_alpha()
tree1 = pygame.image.load('sprites/trees/t.png').convert_alpha()
tree2 = pygame.image.load('sprites/trees/d.png').convert_alpha()
drive_way_down = pygame.image.load('sprites/driveway/m.png').convert_alpha()
drive_way_top = pygame.image.load('sprites/driveway/g.png').convert_alpha()
drive_way_middle = pygame.image.load('sprites/driveway/q.png').convert_alpha()
stone = pygame.image.load('sprites/driveway/s.png').convert_alpha()
rail1 = pygame.image.load('sprites/driveway/r.png').convert_alpha()
rail2 = pygame.image.load('sprites/driveway/z.png').convert_alpha()
carpet = pygame.image.load('sprites/apartament/1.png').convert_alpha()
cafel = pygame.image.load('sprites/apartament/2.png').convert_alpha()
bath_floor = pygame.image.load('sprites/apartament/3.png').convert_alpha()
rail_middle = pygame.image.load('sprites/driveway/v.png').convert_alpha()

# улица
panel1 = pygame.image.load('sprites/houses/panel1.png').convert_alpha()
pyatorochka1 = pygame.image.load('sprites/houses/pyatorochka1.png').convert_alpha()
trash1 = pygame.image.load('sprites/street decoration/trash1.png').convert_alpha()
bench = pygame.image.load('sprites/street decoration/bench.png').convert_alpha()
panel2 = pygame.image.load('sprites/houses/panel2.png').convert_alpha()
lamp_post1 = pygame.image.load('sprites/street decoration/lamp_post1.png').convert_alpha()
lamp_post2 = pygame.image.load('sprites/street decoration/lamp_post2.png').convert_alpha()
wall1 = pygame.image.load('sprites/street decoration/wall1.png').convert_alpha()
plyr = pygame.image.load('sprites/player/street/walk_left/plyr1_left.png').convert_alpha()
fence_wall = pygame.image.load('sprites/street decoration/fence_wall.png').convert_alpha()
pyatorochka2 = pygame.image.load('sprites/houses/pyatorochka2.png').convert_alpha()
panel1_above = pygame.image.load('sprites/houses/panel1_above.png').convert_alpha()
snow_walk1 = pygame.image.load('sprites/snow walkway/snow_walk1.png').convert_alpha()
road_cone = pygame.image.load('sprites/street decoration/road_cone.png').convert_alpha()
wall2 = pygame.image.load('sprites/street decoration/wall2.png').convert_alpha()
panel1_above_rotate = pygame.image.load('sprites/houses/panel1_above_rotate.png').convert_alpha()
drive_way_left = pygame.image.load('sprites/driveway/w.png').convert_alpha()
drive_way_right = pygame.image.load('sprites/driveway/y.png').convert_alpha()
drive_way1 = pygame.image.load('sprites/driveway/drive_way1.png').convert_alpha()
train_station = pygame.image.load('sprites/street decoration/train_station.png').convert_alpha()
road_sign_stop = pygame.image.load('sprites/street decoration/road_sign_stop.png').convert_alpha()
bare_tree1 = pygame.image.load('sprites/trees/bare tree1.png').convert_alpha()
bare_tree2 = pygame.image.load('sprites/trees/bare tree2.png').convert_alpha()
panel2_above = pygame.image.load('sprites/houses/panel2_above.png').convert_alpha()
snow_tree1 = pygame.image.load('sprites/trees/snow_tree1.png').convert_alpha()
snow_tree2 = pygame.image.load('sprites/trees/snow_tree2.png').convert_alpha()
snow_tree3 = pygame.image.load('sprites/trees/snow_tree3.png').convert_alpha()
snow_tree4 = pygame.image.load('sprites/trees/snow_tree4.png').convert_alpha()
snow_tree5 = pygame.image.load('sprites/trees/snow_tree5.png').convert_alpha()
rail_way_sign = pygame.image.load('sprites/street decoration/rail_way_sign.png').convert_alpha()
barbed_wire = pygame.image.load('sprites/street decoration/barbed wire.png').convert_alpha()
ghost1 = pygame.image.load('sprites/ghosts/eye1.png').convert_alpha()
snow_stone = pygame.image.load('sprites/street decoration/snow_stone.png').convert_alpha()
train_texture = pygame.image.load('sprites/street decoration/train.png').convert_alpha()
garages = pygame.image.load('sprites/street decoration/garages.png').convert_alpha()
snowdrift1 = pygame.image.load('sprites/street decoration/snowdrift1.png').convert_alpha()
snowdrift2 = pygame.image.load('sprites/street decoration/snowdrift2.png').convert_alpha()
shop_open1 = pygame.image.load('sprites/houses/shop1.png').convert_alpha()
bus = pygame.image.load('sprites/street decoration/bus.png').convert_alpha()



# квартира и подъезд
bed = pygame.image.load('sprites/apartament/bed.png').convert_alpha()
computer = pygame.image.load('sprites/apartament/computer.png').convert_alpha()
tutorial_sheet = pygame.image.load('sprites/apartament/tutorial_sheet.png').convert_alpha()
balcony = pygame.image.load('sprites/apartament/balcony.png').convert_alpha()
wall1_ap = pygame.image.load('sprites/apartament/wall1.png').convert_alpha()
upper = pygame.image.load('sprites/apartament/upper.png').convert_alpha()
upper_right = pygame.image.load('sprites/apartament/upper_right.png').convert_alpha()
exit_door = pygame.image.load('sprites/apartament/door.png').convert_alpha()
wall2_ap = pygame.image.load('sprites/apartament/wall2.png').convert_alpha()
shower = pygame.image.load('sprites/apartament/shower.png').convert_alpha()
wall_bathroom = pygame.image.load('sprites/apartament/wall_bathroom.png').convert_alpha()
rail_way_long = pygame.image.load('sprites/driveway/rail_way_long.png').convert_alpha()
computer_on = pygame.image.load('sprites/apartament/computer_on.png').convert_alpha()


tile_porch = pygame.image.load('sprites/apartament/t.png').convert_alpha()
wall_porch = pygame.image.load('sprites/porch/wall.png').convert_alpha()
roof_porch = pygame.image.load('sprites/porch/roof.png').convert_alpha()
roof_rotate_porch = pygame.image.load('sprites/porch/roof_rotate.png').convert_alpha()
porch_img = pygame.image.load('sprites/porch/porch_img.png').convert_alpha()
door2_porch = pygame.image.load('sprites/porch/door2_porch.png').convert_alpha()
ledder = pygame.image.load('sprites/porch/ledder.png').convert_alpha()
door3_porch = pygame.image.load('sprites/porch/door3_porch.png').convert_alpha()
tile_porch_dark = pygame.image.load('sprites/porch/t_dark.png').convert_alpha()
carpet_porch = pygame.image.load('sprites/porch/carpet.png').convert_alpha()
portal = pygame.image.load('sprites/porch/portal.png').convert_alpha()

# иконки и прочее
battery_icon_low = pygame.image.load('sprites/icons/low_battery_icon.png').convert_alpha()
battery_icon_low_ready = pygame.image.load('sprites/icons/low_battery_icon_ready.png').convert_alpha()
battery_icon_medium = pygame.image.load('sprites/icons/medium_battery_icon.png').convert_alpha()
battery_icon_medium_ready = pygame.image.load('sprites/icons/medium_battery_icon_ready.png').convert_alpha()
battery_icon_high = pygame.image.load('sprites/icons/high_battery_icon.png').convert_alpha()
battery_icon_high_ready = pygame.image.load('sprites/icons/high_battery_icon_ready.png').convert_alpha()
mouse_cursor = pygame.image.load('sprites/icons/mouse_cursor.png').convert_alpha()
light = pygame.image.load('sprites/icons/light.png').convert_alpha()
achievement_texture = pygame.image.load('sprites/achievements/golden_cup.png').convert_alpha()
toasty = pygame.image.load('sprites/ach/toasty.png').convert_alpha()
key = pygame.image.load('sprites/ach/key.png').convert_alpha()
LENIN = pygame.image.load('sprites/ghosts/LENIN.png').convert_alpha()
eye1 = pygame.image.load('sprites/ghosts/eye1.png').convert_alpha()
eye2 = pygame.image.load('sprites/ghosts/eye2.png').convert_alpha()
smile = pygame.image.load('sprites/porch/smile.png').convert_alpha()
scull = pygame.image.load('sprites/icons/scull.png').convert_alpha()
health_bar = pygame.image.load('sprites/icons/health_bar.png').convert_alpha()

# кнопки
btn_retry = pygame.image.load('sprites/buttons/btn_retry.png').convert_alpha()
btn_menu = pygame.image.load('sprites/buttons/btn_menu.png').convert_alpha()
btn_on = pygame.image.load('sprites/buttons/btn_on.png').convert_alpha()
btn_off = pygame.image.load('sprites/buttons/btn_off.png').convert_alpha()
btn_OK = pygame.image.load('sprites/buttons/OK.png').convert_alpha()
btn_NO = pygame.image.load('sprites/buttons/NO.png').convert_alpha()
btn_E = pygame.image.load('sprites/buttons/btn_E.png').convert_alpha()

# дримкор
dream_house1_r = pygame.image.load('sprites/dreamcore/house_right.png').convert_alpha()
dream_house1_f = pygame.image.load('sprites/dreamcore/house_front.png').convert_alpha()
hand = pygame.image.load('sprites/ach/hand.png').convert_alpha()
signboard = pygame.image.load('sprites/dreamcore/signboard.png').convert_alpha()


# достижения
death_by_train_icon = pygame.image.load('sprites/achievements/death by train.png').convert_alpha()
toasty_ach = pygame.image.load('sprites/achievements/toasty_ach.png').convert_alpha()
better_stay_at_home = pygame.image.load('sprites/achievements/better_stay_at_home.png').convert_alpha()
texture_ach = pygame.image.load('sprites/achievements/golden_cup.png').convert_alpha()
train_ending = pygame.image.load('sprites/achievements/train_ending.png').convert_alpha()
they_are_wathing_you = pygame.image.load('sprites/achievements/they_are_wathing_you.png').convert_alpha()
pt1 = pygame.image.load('sprites/achievements/pt1.png').convert_alpha()
pt2 = pygame.image.load('sprites/achievements/pt2.png').convert_alpha()
thief = pygame.image.load('sprites/achievements/thief.png').convert_alpha()
USSR = pygame.image.load('sprites/achievements/USSR.png').convert_alpha()
silent = pygame.image.load('sprites/achievements/silent.png').convert_alpha()
key_ach = pygame.image.load('sprites/achievements/key.png').convert_alpha()
hell_rune = pygame.image.load('sprites/achievements/hell rune.png').convert_alpha()
reload_ach = pygame.image.load('sprites/achievements/reload.png').convert_alpha()
rune_of_life = pygame.image.load('sprites/achievements/rune_of_life.png').convert_alpha()
god_rune = pygame.image.load('sprites/achievements/god rune.png').convert_alpha()
god_rune_item = pygame.image.load('sprites/ach/god rune item.png').convert_alpha()
dead_end = pygame.image.load('sprites/achievements/dead end.png').convert_alpha()
once_upon_a_time_ach = pygame.image.load('sprites/achievements/once upon a time.png').convert_alpha()
the_end = pygame.image.load('sprites/achievements/the end.png').convert_alpha()
all_or_nothing = pygame.image.load('sprites/achievements/all or nothing.png').convert_alpha()
all_achievements = pygame.image.load('sprites/achievements/all achievements.png').convert_alpha()
skilly = pygame.image.load('sprites/achievements/skilly.png').convert_alpha()
rosy = pygame.image.load('sprites/achievements/rosy.png').convert_alpha()

# вооружение
stratch = pygame.image.load('sprites/weap/stratch.png').convert_alpha()
teleport_mouse = pygame.image.load('sprites/icons/teleport mouse.png').convert_alpha()
fire_ball_mouse = pygame.image.load('sprites/icons/fire ball mouse.png').convert_alpha()
heal_mouse = pygame.image.load('sprites/icons/heal mouse.png').convert_alpha()
inventory = pygame.image.load('sprites/weap/inventory.png').convert_alpha()
cell_used = pygame.image.load('sprites/icons/icon_used_inv.png').convert_alpha()

# подсказки
attack_helper = pygame.image.load('sprites/helpers/taverna/attack.png').convert_alpha()
