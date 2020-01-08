# Python Function to get a list of files in a directory (requires glob package)
def listDirfiles(dir):
# requires glob package
   return glob.glob(str(dir + "/*"))
