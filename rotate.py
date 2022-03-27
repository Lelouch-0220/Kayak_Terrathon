from PIL import Image 
colorImage= Image.open("./image0.jpg")
rotated=colorImage.rotate(13)
width, height= rotated.size
x=675
left=x
right=width-x
top=x
bottom=height-x
L1=(right-left)/8
H1=(bottom-top)/8
count=64
fopname="./image1.jpg"
colorImage= Image.open(fopname)
rotated=colorImage.rotate(13)
width, height= rotated.size
x=675
left=x
right=width-x
top=x
bottom=height-x
L1=(right-left)/8
H1=(bottom-top)/8
count=0	
for i in range(8):
	for j in range(8):
		ls=j*L1
		ds=i*H1
		L=x+ls
		T=x+ds
		rotated_t= rotated.crop((L,T,L+L1,T+H1))
		f_name= "imagee" + str(count) + ".jpg"
		rotated_t.save(f_name)
		count=count+1
