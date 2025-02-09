from abc import ABC, abstractmethod


class File(ABC):
    @abstractmethod
    def accept(self, visitor: "Visitor"):
        pass


class TextFile(File):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def accept(self, visitor: "Visitor"):
        visitor.visit_text_file(self)

    def get_size(self):
        return self.size


class ImageFile(File):
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def accept(self, visitor: "Visitor"):
        visitor.visit_image_file(self)

    def get_dimensions(self):
        return self.width, self.height


class ArchiveFile(File):
    def __init__(self, name, files):
        self.name = name
        self.files = files

    def accept(self, visitor):
        visitor.visit_archive_file(self)
        for file in self.files:
            file.accept(visitor)

    def get_files(self):
        return self.files


class FileVisitor(ABC):
    @abstractmethod
    def visit_text_file(self, text_file):
        pass

    @abstractmethod
    def visit_image_file(self, image_file):
        pass

    @abstractmethod
    def visit_archive_file(self, archive_file):
        pass


class TotalSizeVisitor(FileVisitor):
    def __init__(self):
        self.total_size = 0

    def visit_text_file(self, text_file: TextFile):
        self.total_size += text_file.get_size()

    def visit_image_file(self, image_file: ImageFile):
        width, height = image_file.get_dimensions()
        self.total_size += width * height

    def visit_archive_file(self, archive_file: FileVisitor):
        pass

    def get_total_size(self):
        return self.total_size


class ThumbnailCreatorVisitor(FileVisitor):
    def visit_text_file(self, text_file: TextFile):
        print(f"Skipping thumbnail creation for text file: {text_file.name}")

    def visit_image_file(self, image_file: ImageFile):
        print(f"Creating thumbnail for image: {image_file.name}")

    def visit_archive_file(self, archive_file: FileVisitor):
        print(f"Skipping thumbnail creation for archive: {archive_file.name}")


class CompressionVisitor(FileVisitor):
    def visit_text_file(self, text_file: TextFile):
        print(f"Compressing text file: {text_file.name}")

    def visit_image_file(self, image_file: ImageFile):
        print(f"Compressing image file: {image_file.name}")

    def visit_archive_file(self, archive_file: FileVisitor):
        print(f"Compressing archive: {archive_file.name}")


text_file = TextFile("report.txt", 1024)
image_file = ImageFile("photo.jpg", 800, 600)
archive_file = ArchiveFile("backup.zip", [text_file, image_file])

size_visitor = TotalSizeVisitor()
thumbnail_visitor = ThumbnailCreatorVisitor()
compression_visitor = CompressionVisitor()

print("Calculating total size:")
archive_file.accept(size_visitor)
print("Creating thumbnails:")
image_file.accept(thumbnail_visitor)
print("Compressing files:")
archive_file.accept(compression_visitor)

print('Total size')
total_size = size_visitor.get_total_size()
print(total_size)