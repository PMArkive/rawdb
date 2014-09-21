
import struct
from six import StringIO

__all__ = ['BinaryIO']


class StructReaders:
    """Cached built structs
    """
    int8 = struct.Struct('b')
    uint8 = struct.Struct('B')
    int16 = struct.Struct('h')
    uint16 = struct.Struct('H')
    int32 = struct.Struct('i')
    uint32 = struct.Struct('I')


class BinaryIO(StringIO):
    """Reader and Writer for binary data.

    This provides useful methods for reading and writing specific binary
    types.

    To use a file handle, use BinaryIO.adapter(handle)

    Parameters
    ----------
    data : string
        Binary string to be used
    """
    def __init__(self, data=''):
        StringIO.__init__(self, data)

    def readUInt8(self):
        return StructReaders.uint8.unpack(self.read(1))

    def writeUInt8(self, value):
        self.write(StructReaders.uint8.pack(value))

    def readInt8(self):
        return StructReaders.int8.unpack(self.read(1))

    def writeInt8(self, value):
        self.write(StructReaders.int8.pack(value))

    def readUInt16(self):
        return StructReaders.uint16.unpack(self.read(2))

    def writeUInt16(self, value):
        self.write(StructReaders.uint16.pack(value))

    def readInt16(self):
        return StructReaders.int16.unpack(self.read(2))

    def writeInt16(self, value):
        self.write(StructReaders.int16.pack(value))

    def readUInt32(self):
        return StructReaders.uint32.unpack(self.read(4))

    def writeUInt32(self, value):
        self.write(StructReaders.uint32.pack(value))

    def readInt32(self):
        return StructReaders.int32.unpack(self.read(4))

    def writeInt32(self, value):
        self.write(StructReaders.int32.pack(value))

    @staticmethod
    def adapter(handle):
        """Create a BinaryIOAdapter around a file handle"""
        return BinaryIOAdapter(handle)


class BinaryIOAdapter(BinaryIO):
    """Adapter for file handles

    Allows all of the BinaryIO methods to be used without a stringio object
    """
    def __init__(self, handle):
        BinaryIO.__init__(self)
        self.handle = handle

    def read(self, size=-1):
        return self.handle.read(size)

    def write(self, value):
        self.handle.write(value)

    def seek(self, offset, whence=0):
        self.handle.seek(offset, whence)

    def tell(self):
        return self.handle.tell()

