# Select a large image and a large notepad file on your machine, 
# now apply all the data compression libraries available in python to compress the files one by one . 
# Show how much compression have to achieved (display size of original file and size of compressed file and the percentage of reduction also).  
# Then again decompress the files and show that it was a loss less compression. 
# Try all possible methods of hte libraries zlib, gzip, zipfile, lzma etc

from bz2 import compress
from zipfile import ZipFile
import zlib
import gzip
import lzma

txtfile = open('Text.txt', 'rb').read()

compressed_data = zlib.compress(txtfile, zlib.Z_BEST_COMPRESSION)
compression_ratio = (float(len(txtfile)) - float(len(compressed_data))) / float(len(txtfile))
print('TEXT FILE COMPRESSION : ')
print('    ZLIB Library :')
print('        Original File Size : ', len(txtfile))
print('        Compressed File Size : ', len(compressed_data))
print('        Compression Ratio : %d%%' % (100.0 * compression_ratio))  
decompressed_data = zlib.decompressobj().decompress(compressed_data)
decompression_ratio = (float(len(txtfile)) - float(len(decompressed_data))) / float(len(txtfile))
print('        Decompressed File Size : ', len(decompressed_data))
print('        Data Loss : %d%%' % (100.0 * decompression_ratio))
print()

compressed_data = gzip.compress(txtfile)
compression_ratio = (float(len(txtfile)) - float(len(compressed_data))) / float(len(txtfile))
print('    GZIP Library :')
print('        Original File Size : ', len(txtfile))
print('        Compressed File Size : ', len(compressed_data))
print('        Compression Ratio : %d%%' % (100.0 * compression_ratio))
decompressed_data = gzip.decompress(compressed_data)
decompression_ratio = (float(len(txtfile)) - float(len(decompressed_data))) / float(len(txtfile))
print('        Decompressed File Size : ', len(decompressed_data))
print('        Data Loss : %d%%' % (100.0 * decompression_ratio))  
print()

compressed_data = lzma.LZMACompressor().compress(txtfile)
compression_ratio = (float(len(txtfile)) - float(len(compressed_data))) / float(len(txtfile))
print('    LZMA Library :')
print('        Original File Size : ', len(txtfile))
print('        Compressed File Size : ', len(compressed_data))
print('        Compression Ratio : %d%%' % (100.0 * compression_ratio)) 
decompressed_data = lzma.LZMADecompressor().decompress(compressed_data)
decompression_ratio = (float(len(txtfile)) - float(len(decompressed_data))) / float(len(txtfile))
print('        Decompressed File Size : ', len(decompressed_data))
print('        Data Loss : %d%%' % (100.0 * decompression_ratio))
print() 

imgfile = open('image.jpg', 'rb').read()

compressed_data = zlib.compress(imgfile, zlib.Z_BEST_COMPRESSION)
compression_ratio = (float(len(imgfile)) - float(len(compressed_data))) / float(len(imgfile))
print('IMAGE FILE COMPRESSION : ')
print('    ZLIB Library :')
print('        Original File Size : ', len(imgfile))
print('        Compressed File Size : ', len(compressed_data))
print('        Compression Ratio : %d%%' % (100.0 * compression_ratio)) 
decompressed_data = zlib.decompressobj().decompress(compressed_data)
decompression_ratio = (float(len(imgfile)) - float(len(decompressed_data))) / float(len(imgfile))
print('        Decompressed File Size : ', len(decompressed_data))
print('        Data Loss : %d%%' % (100.0 * decompression_ratio))
print()

compressed_data = gzip.compress(imgfile)
compression_ratio = (float(len(imgfile)) - float(len(compressed_data))) / float(len(imgfile))
print('    GZIP Library :')
print('        Original File Size : ', len(imgfile))
print('        Compressed File Size : ', len(compressed_data))
print('        Compression Ratio : %d%%' % (100.0 * compression_ratio))  
decompressed_data = gzip.decompress(compressed_data)
decompression_ratio = (float(len(imgfile)) - float(len(decompressed_data))) / float(len(imgfile))
print('        Decompressed File Size : ', len(decompressed_data))
print('        Data Loss : %d%%' % (100.0 * decompression_ratio))
print()

compressed_data = lzma.LZMACompressor().compress(imgfile)
compression_ratio = (float(len(imgfile)) - float(len(compressed_data))) / float(len(imgfile))
print('    LZMA Library :')
print('        Original File Size : ', len(imgfile))
print('        Compressed File Size : ', len(compressed_data))
print('        Compression Ratio : %d%%' % (100.0 * compression_ratio))  
decompressed_data = lzma.LZMADecompressor().decompress(compressed_data)
decompression_ratio = (float(len(imgfile)) - float(len(decompressed_data))) / float(len(imgfile))
print('        Decompressed File Size : ', len(decompressed_data))
print('        Data Loss : %d%%' % (100.0 * decompression_ratio))
print()

print('ZIPFILE LIBRARY (TEXT + IMAGE) : ')
files = ['Text.txt', 'image.jpg']
zipfile = ZipFile('files.zip', 'w')
for f in files:
    zipfile.write(f)
zipfile.close()
compression_ratio = (float(len(imgfile) + len(txtfile)) - float(zipfile.getinfo('image.jpg').compress_size + zipfile.getinfo('Text.txt').compress_size)) / float(len(imgfile) + len(txtfile))
print('    ZIPFILE Library :')
print('        Original File Size : ', len(txtfile) + len(imgfile))
print('        Compressed File Size : ', int(zipfile.getinfo('image.jpg').compress_size + zipfile.getinfo('Text.txt').compress_size))
print('        Compression Ratio : %d%%' % (100.0 * compression_ratio))
decompressed_data = ZipFile('files.zip', 'r')
decompressed_data.extractall('ExtractedFiles')
decompression_ratio = (float(len(imgfile) + len(txtfile)) - int(zipfile.getinfo('image.jpg').compress_size + zipfile.getinfo('Text.txt').compress_size)) / float(len(imgfile) + len(txtfile))
print('        Decompressed File Size : ', zipfile.getinfo('image.jpg').compress_size + zipfile.getinfo('Text.txt').compress_size)
print('        Data Loss : %d%%' % (100.0 * decompression_ratio))
