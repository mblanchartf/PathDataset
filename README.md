# Path dataset creation tool with OpenCV and GPXPY

This learning project pretends to create a dataset with "paths" images for future projects. From GPX files this tool extracts 300x300 images using Google Maps API. 

## Instructions

Join in a folder all the tracks you want to use.

Then run thepath_dataset.py script that has the following arguments: 

```bash
python path_dataset.py -h
usage: path_dataset.py [-h] -tpath TRACKS_PATH

Extract images from GPX files

required arguments:
  -tpath TRACKS_PATH, --tracks_path TRACKS_PATH
                        Path to the GPX tracks

optional arguments:
  -h, --help            show this help message and exit
```

### Examples

```bash
$ python path_dataset.py -tpath F:/Datasets/track/
218 images created at: F:/Datasets/track/
```

## Image examples

<img src=screenshots/20180704201644_36.png width=100% />
<img src=screenshots/20180704201644_37.png width=100% />
<img src=screenshots/20180704201644_38.png width=100% />
<img src=screenshots/20180704201644_39.png width=100% />
<img src=screenshots/20180704201644_40.png width=100% />
<img src=screenshots/20180704201644_41.png width=100% />
<img src=screenshots/20180704201644_42.png width=100% />
<img src=screenshots/20180704201644_43.png width=100% />
<img src=screenshots/20180704201644_44.png width=100% />
<img src=screenshots/20180704201644_45.png width=100% />
<img src=screenshots/20180704201644_46.png width=100% />
<img src=screenshots/20180704201644_47.png width=100% />
<img src=screenshots/20180704201644_48.png width=100% />
<img src=screenshots/20180704201644_49.png width=100% />
<img src=screenshots/20180704201644_50.png width=100% />
<img src=screenshots/20180704201644_51.png width=100% />
<img src=screenshots/20180704201644_52.png width=100% />
<img src=screenshots/20180704201644_53.png width=100% />
<img src=screenshots/20180704201644_54.png width=100% />
<img src=screenshots/20180704201644_55.png width=100% />
<img src=screenshots/20180704201644_56.png width=100% />
<img src=screenshots/20180704201644_57.png width=100% />


## Authors

* **Marc Blanchart** - *Learning project* - [MarcBlanchart](https://github.com/mblanchartf)

