import Image

#opens the images:
im11 = Image.open("/Volumes/Emilia/NowWorking/newProjet/images_trend/tasmax_ahccd_1950_to_2005trend_Sen.png")
im12 = Image.open("/Volumes/Emilia/NowWorking/newProjet/images_trend/tasmax_nrcan_canada_1950_to_2005trend_Sen.png")
im13 = Image.open("/Volumes/Emilia/NowWorking/newProjet/images_trend/tasmax_CanRCM4_ARC44_CanESM2_histo_anual_1950_to_2005trend_Sen.png")

im21 = Image.open("/Volumes/Emilia/NowWorking/newProjet/images_trend/tasmax_CanRCM4_NA44_CanESM2_histo_anual_1950_to_2005trend_Sen.png")
im22 = Image.open("/Volumes/Emilia/NowWorking/newProjet/images_trend/tasmax_CRCM5_NA44_CanESM2_histo_anual_1950_to_2005trend_Sen.png")
im23 = Image.open("/Volumes/Emilia/NowWorking/newProjet/images_trend/tasmax_CRCM5_NA44_MPI-ESM-LR_histo_anual_1950_to_2005trend_Sen.png")

im_size = im11.size

im11.thumbnail(im_size, Image.ANTIALIAS)
im12.thumbnail(im_size, Image.ANTIALIAS)
im13.thumbnail(im_size, Image.ANTIALIAS)

im21.thumbnail(im_size, Image.ANTIALIAS)
im22.thumbnail(im_size, Image.ANTIALIAS)
im23.thumbnail(im_size, Image.ANTIALIAS)


#creates a new empty image, RGB mode, and size 400 by 400.
new_im = Image.new('RGB', (im_size[0]*3,2*im_size[1]))

new_im.paste(im11, (0,0))
new_im.paste(im12, (im_size[0],0))
new_im.paste(im13, (2*im_size[0],0))

new_im.paste(im21, (0,im_size[1]))
new_im.paste(im22, (im_size[0],im_size[1]))
new_im.paste(im23, (2*im_size[0],im_size[1]))



new_im.save("/Volumes/Emilia/NowWorking/newProjet/images_trend/tasmax_1950_to_2005trend_Sen_panel.png", "PNG")
new_im.show()