import hashlib
BLOCKSIZE=65536

fileToOpen='E:\\N=new_python\\new_dox.txt'
hasher=hashlib.md5()
with open(fileToOpen,'rb')as afile:
  buf=afile.read(BLOCKSIZE)
  while len(buf)>0:
      hasher.update(buf)
      buf=afile.read(BLOCKSIZE)
print(hasher.hexdigest())
