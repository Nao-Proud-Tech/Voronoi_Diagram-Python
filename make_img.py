# ====================
# Library to Import
# ====================
import cv2
from matplotlib import pyplot as plt
import numpy as np
import math
import colorsys
import argparse
import random

from utils import get_cmap_ours, rand_ints_nodup

# ===========================
# Command Line Arguments
# ===========================
parser = argparse.ArgumentParser()

parser.add_argument('--data_num', type=int, help='Number of Data to Generate')
parser.add_argument('--width', type=int, help='Image Width')
parser.add_argument('--height', type=int, help='Image Height')
parser.add_argument('--type', type=int, help='Linking Component')
parser.add_argument('--line', action='store_true', help='Description of Area Line')
parser.add_argument('--point', action='store_true', help='Description of Random Points')
parser.add_argument('--cmap', type=str, default='jet', help='color map name')

args = parser.parse_args()

# =================
# VoronoiDiagram
# =================
def VoronoiDiagram(imgv, subdiv, pts, args):

    # Get Color Map
    Rs, Gs, Bs, As = get_cmap_ours(args.cmap)

    # voronoi split
    facets, centers = subdiv.getVoronoiFacetList([])

    # Get Random Table
    rand_table = list(range(256))
    random.shuffle(rand_table)

    ifacets = [f.astype(int) for f in facets]
    for i, p in enumerate(f.astype(int) for f in facets):

        # lighten the color
        cr = Rs[rand_table[i]] * 255
        cg = Gs[rand_table[i]] * 255
        cb = Bs[rand_table[i]] * 255

        # paint the area
        cv2.fillPoly(imgv, [p], (cr,cg,cb), lineType=args.type)

    if args.line:
        cv2.polylines(imgv, ifacets, True, (0, 0, 0), 1, lineType=args.type)

# ============================
# Random Point Generation
# ============================
def getRandom2DPoints(width, height, n):

    margin = 30
    entry_pts = np.random.randint(margin, max(height, width), (n*2, 2))
    pts = []
    for i, ep in enumerate(entry_pts):
        if ep[0] < margin or (width-margin) < ep[0]:
            continue
        if ep[1] < margin or (height-margin) < ep[1]:
            continue

        h = i * math.pi * 2.0 / n
        rgb = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        r = int(rgb[0] * 255)
        g = int(rgb[1] * 255)
        b = int(rgb[2] * 255)
        pts.append([ep[0],ep[1],(b,g,r)])
    return    pts
    
# ========================
# Main Function
# ========================
def main():

    # loop
    for i in range(args.data_num):
        # Random Point Generation
        point_num = 30
        rand_point_num = random.randint(2,point_num)
        pts = getRandom2DPoints(args.width, args.height, rand_point_num)
        imgv = np.zeros((args.height, args.width, 3), np.uint8)
        imgv.fill(255)

        # Plan Split
        subdiv = cv2.Subdiv2D((0, 0, args.width, args.height))
        for p in pts:
            subdiv.insert((p[0], p[1]))



        # Voronoi Diagram
        VoronoiDiagram(imgv, subdiv, pts, args)

        # Drawing Random Points
        if args.point:
            for p in pts:
                color = p[2]
                cv2.circle(imgv, (p[0],p[1]), 4, color, thickness=1, lineType=args.type)

        # Save Image
        cv2.imwrite(f'./data/voronoi_{i}.png', imgv)

if __name__ == '__main__':
    main()
