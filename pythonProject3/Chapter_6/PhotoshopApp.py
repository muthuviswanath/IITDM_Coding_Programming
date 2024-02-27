class Photoshop:

    def openFile(self,File):
        File.file_behaviour()

class File:

    def __init__(self,filename):
        self.filename = filename
    def file_behaviour(self):
        pass

class JpegFile(File):
    def file_behaviour(self):
        print(f"Filename: {self.filename}")
        filext = self.filename.split(".")
        print(f"File Extension:.{filext[1]}")
        print("Openend as Flattened Image")
class PngFile(File):
    def file_behaviour(self):
        print(f"Filename: {self.filename}")
        filext = self.filename.split(".")
        print(f"File Extension:.{filext[1]}")
        print("Openend as Layer")
class GifFile(File):
    def file_behaviour(self):
        print(f"Filename: {self.filename}")
        filext = self.filename.split(".")
        print(f"File Extension:.{filext[1]}")
        print("Openend as multiple layers with timeline")
class PdfFile(File):
    def file_behaviour(self):
        print(f"Filename: {self.filename}")
        filext = self.filename.split(".")
        print(f"File Extension:.{filext[1]}")
        print("Openend as layers")

my_file = GifFile("MyPic.gif")
ps = Photoshop()
ps.openFile(my_file)
