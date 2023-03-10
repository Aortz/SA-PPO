import mujoco_py
import argparse, glob, os
from PIL import Image
import imageio as io

def main():
    #supported formats
    formats = ["BMP", "DIB", "EPS", "GIF", "ICNS", "ICO", "IM", "JPG", "JPEG",
           "J2K", "J2P", "JPX", "MSP", "PCX", "PNG", "PPM", "SGI",
           "SPIDER", "TGA", "TIFF", "WebP", "XBM"]
    parser = argparse.ArgumentParser(description="Batch converter for bmp files")
    parser.add_argument('--outdir', default='.', help='Directory to save converted image files')
    parser.add_argument('--outformat', choices=formats,
                        help='Output image format required. The output file will be written with the same base-name as the input file, but with an extension reflecting the format')
    parser.add_argument('--infiles', nargs='+', help='File pattern of input image files, use *, ? and [] to specify patterns')
    # supported arguments: python simulation.py --outdir frames/walker/vanilla/4623 --outformat GIF --infiles frames/walker/vanilla/4623/*.bmp
    args = parser.parse_args()

    # array to store numpy array read in using imageio so that frames can be converted to gif
    infiles = []
    for name in args.infiles:
        # print(name)
        infiles.append(io.imread(name))
        # infiles += glob.glob(name)
    # print(infiles)

    if os.path.isdir(args.outdir): pass
    base = os.path.basename(args.outdir)
    f, ext = os.path.splitext(base)
    opath = os.path.join(args.outdir, '{}.{}'.format(f, args.outformat.lower()))
    print(opath)
    io.mimsave(opath, infiles, fps=25)

if __name__ == "__main__":
    main()