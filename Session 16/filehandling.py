f = open("C:\\Users\\Manu\\Desktop\\DG_Lectures\\Session 14-15\\mytextfile.txt", "r+b")

print(f.write(b"This is written"))
f.seek(-2, 1)
f.write(b"#")
f.close()

