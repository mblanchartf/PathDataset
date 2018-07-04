from gps.utils import get_maps_image, get_lat_lon_points, get_lat_lon_region
import time
import argparse
import cv2


# Arguments parser
parser = argparse.ArgumentParser(
        description='Extract images from GPX files')
optional = parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
required.add_argument('-tpath', '--tracks_path', required=True, type=str,
                      help='Path to the GPX tracks')
parser._action_groups.append(optional)

# Prepare general data
args = parser.parse_args()
tracks_path = args.tracks_path
zoom = 20

timestr = time.strftime("%Y%m%d%H%M%S_")

# Prepare GPS data
lat, lon = get_lat_lon_points(tracks_path)

# Extract images
for i in range(0, len(lat)-1):
    NW_lat_long, SE_lat_long = get_lat_lon_region(lat[i], lon[i],
                                                  offset=0.0002)
    result = get_maps_image(NW_lat_long, SE_lat_long, zoom)
    image_file = tracks_path + timestr + str(i) + '.png'
    result.save(image_file)
    img = cv2.imread(image_file)
    resized_image = cv2.resize(img, (300, 300))
    cv2.imwrite(image_file, resized_image)

print(str(i) + ' images created at: ' + tracks_path)
